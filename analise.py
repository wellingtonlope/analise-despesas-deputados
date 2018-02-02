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
        self.telefone = None
        self.transporte = None
        self.viagem = None
        self.escritorio = None
        self.marketing = None
        self.seguranca = None
        self.alimentacao = None
        self.hospedagem = None
        self.outros = None
        self.total = None


deputados = []

categorias_gastos = deputados_roraima.txtDescricao.unique()

for numero_carteira in deputados_roraima.nuCarteiraParlamentar.unique():
    deputado = Deputado()
    deputadodf = deputados_roraima.query('nuCarteiraParlamentar == {}'.format(numero_carteira))
    print('Deputado {}'.format(deputadodf['txNomeParlamentar'].unique()[0]))
    deputado.nome = deputadodf['txNomeParlamentar'].unique()[0]
    deputado.total = 0
    for categoria_gasto in categorias_gastos:
        print('{}'.format(categoria_gasto))
        valor_categoria = deputadodf.query('txtDescricao == "{}"'.format(categoria_gasto))
        total_categoria = 0
        for valor in valor_categoria['vlrDocumento']:
            print(valor)
            total_categoria += float(valor.replace(',', '.'))
        deputado.total += total_categoria
        print('Total: {}'.format(str(total_categoria).replace('.', ',')))
    print('Total deputado: {}'.format(str(deputado.total).replace('.', ',')))
    deputados.append(deputado)

for d in deputados:
    print(d.nome)
    print(d.total)