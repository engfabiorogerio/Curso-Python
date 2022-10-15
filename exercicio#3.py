# 3) Se o produto que vc quer avaliar custa xReais. Qual será o valor do
# mesmo com um desconto de x%

print('Precificando valores')

produto = input('Informe o produto a ser analisado: ')
preco = input('Informe o valor do produto: ')
desconto = input('Informe o desconto para o cliente: ')

valor_final = (float(preco) * float(desconto)) / 100

print(f'O valor final do produto {produto} eh de {valor_final} reais')
