#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#   File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#   Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#   Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipoCarne = int(input('''
    Digite a carne a ser comprada:
    1 - Filé Duplo
    2 - Alcatra
    3 - Picanha

    Digite: '''))
qtdCarne = float(input("Digite a quantidade (em KG): "))
formaPagamento = int(input("Vai utilizar o cartão Tabajara? 1 - Sim ou 0 - Não: "))
desconto = 0

if tipoCarne == 1:
    nomeCarne = "Filé Duplo"
    if qtdCarne <= 5:
        precoCarne = 4.9
    else:
        precoCarne = 5.8
elif tipoCarne == 2:
    nomeCarne = "Alcatra"
    if qtdCarne <= 5:
        precoCarne = 5.9
    else:
        precoCarne = 6.8
elif tipoCarne == 3:
    nomeCarne = "Picanha"
    if qtdCarne <= 5:
        precoCarne = 6.9
    else:
        precoCarne = 7.8

valorTotal = precoCarne * qtdCarne

if formaPagamento == 1:
    tipoPagamento = "Cartão Tabajara"
    desconto = valorTotal * 0.05
    valorTotal = valorTotal - desconto
else:
    tipoPagamento = "Outros"

print(f'''
    ----------Cupom fiscal----------

    Tipo de carne: {nomeCarne}
    Quantidade (em KG): {qtdCarne:.2f}
    Tipo de pagamento: {tipoPagamento}
    Valor do Desconto: {desconto:.2f}
    Valor a pagar: {valorTotal:.2f}

    --------------------------------
''')
