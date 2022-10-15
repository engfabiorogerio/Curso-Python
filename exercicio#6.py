# 6) Converso de dolares para reais

print("Conversor de moedas")

dolar_qtd = input('Informe a quantidade de dolares: ')
cotacao_dolar = input('Informe a cotacao do dia: ')
valor_convert = float(dolar_qtd) / float(cotacao_dolar)

print(f' {dolar_qtd} valem {valor_convert} reais.')
