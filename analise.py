# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-

import pandas as pd

df = pd.read_csv('ano_2017_rr.csv', sep=';')

# deputados_roraima = df.query('sgUF == "RR"')
# deputados_roraima.to_csv('ano_2017_rr.csv', encoding='utf-8', sep=';', index=False)

# txNomeParlamentar
# txtDescricao == categoria
# nuCarteiraParlamentar
# vlrDocumento == o que foi gasto

deputados_roraima = df

class Deputado:

    def __init__(self):
        self.nome = None
        self.telefone = 0
        self.transporte = 0
        self.viagem = 0
        self.escritorio = 0
        self.marketing = 0
        self.seguranca = 0
        self.alimentacao = 0
        self.hospedagem = 0
        self.outro = 0
        self.total = 0

def categoria(deputado, categoria, valor):
    if categoria == 'TELEFONIA':
        deputado.telefone += valor
    elif categoria == 'COMBUSTÍVEIS E LUBRIFICANTES.' or categoria == 'LOCAÇÃO OU FRETAMENTO DE VEÍCULOS AUTOMOTORES' or categoria == 'SERVIÇO DE TÁXI, PEDÁGIO E ESTACIONAMENTO':
        deputado.transporte += valor
    elif categoria == 'Emissão Bilhete Aéreo' or categoria == 'PASSAGENS AÉREAS' or categoria == 'PASSAGENS TERRESTRES, MARÍTIMAS OU FLUVIAIS' or categoria == 'LOCAÇÃO OU FRETAMENTO DE AERONAVES':
        deputado.viagem += valor
    elif categoria == 'MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE PARLAMENTAR':
        deputado.escritorio += valor
    elif categoria == 'DIVULGAÇÃO DA ATIVIDADE PARLAMENTAR.':
        deputado.marketing += valor
    elif categoria == 'SERVIÇO DE SEGURANÇA PRESTADO POR EMPRESA ESPECIALIZADA.':
        deputado.seguranca += valor
    elif categoria == 'FORNECIMENTO DE ALIMENTAÇÃO DO PARLAMENTAR':
        deputado.alimentacao += valor
    elif categoria == 'HOSPEDAGEM ,EXCETO DO PARLAMENTAR NO DISTRITO FEDERAL.':
        deputado.hospedagem += valor
    else:
        deputado.outro += valor
    return deputado

def porcentagem(valor, total):
    return valor / total * 100.0

deputados = []

categorias_gastos = deputados_roraima.txtDescricao.unique()

for numero_carteira in deputados_roraima.nuCarteiraParlamentar.unique():
    deputado = Deputado()
    deputadodf = deputados_roraima.query('nuCarteiraParlamentar == {}'.format(numero_carteira))
    deputado.nome = deputadodf['txNomeParlamentar'].unique()[0]
    deputado.total = 0
    for categoria_gasto in categorias_gastos:
        valor_categoria = deputadodf.query('txtDescricao == "{}"'.format(categoria_gasto))
        total_categoria = 0
        for valor in valor_categoria['vlrDocumento']:
            deputado = categoria(deputado, categoria_gasto, float(valor.replace(',', '.')))
            total_categoria += float(valor.replace(',', '.'))
        deputado.total += total_categoria
    deputados.append(deputado)

for deputado in deputados:
    print(deputado.nome)
    print('Telefone: {:.2f}%'.format(porcentagem(deputado.telefone, deputado.total)))
    print('Transporte: {:.2f}%'.format(porcentagem(deputado.transporte, deputado.total)))
    print('Viagem: {:.2f}%'.format(porcentagem(deputado.viagem, deputado.total)))
    print('Escritorio: {:.2f}%'.format(porcentagem(deputado.escritorio, deputado.total)))
    print('Marketing: {:.2f}%'.format(porcentagem(deputado.marketing, deputado.total)))
    print('Segurança: {:.2f}%'.format(porcentagem(deputado.seguranca, deputado.total)))
    print('Alimentação: {:.2f}%'.format(porcentagem(deputado.alimentacao, deputado.total)))
    print('Hospedagem: {:.2f}%'.format(porcentagem(deputado.hospedagem, deputado.total)))
    print('Outros: {:.2f}%'.format(porcentagem(deputado.outro, deputado.total)))
    print('Total de dinheiro gasto: R$ {:.2f}'.format(deputado.total))
    print()

