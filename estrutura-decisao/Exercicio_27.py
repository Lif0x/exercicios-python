#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25.00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtdMaca = float(input("Digite a quantidade de KG de maçãs: "))
qtdMorango = float(input("Digite a quantidade de KG de morangos: "))

if qtdMorango <= 5:
    precoMorango = 2.5
else:
    precoMorango = 2.2

if qtdMaca <= 5:
    precoMaca = 1.8
else:
    precoMaca = 1.5

valorTotal = (qtdMaca * precoMaca) + (qtdMorango * precoMorango)
totalKgs = qtdMaca + qtdMorango

if(valorTotal > 25 or totalKgs > 8):
    valorTotal = valorTotal - (valorTotal * 0.1)

print(f"O valor total a ser pago é : R${valorTotal}")