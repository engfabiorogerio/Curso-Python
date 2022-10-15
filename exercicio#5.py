# 5) Conversão de reais para Dolar

print("Concersor de moeda")

reais_qtd = input('Informe a quantidade de reais: ')
cotacao_dolar = input('Informe a cotacao do dia: ')
valor_convert = float(reais_qtd) / float(cotacao_dolar)

print(f' {reais_qtd} proporcionam a compra de {valor_convert} dolares.')
