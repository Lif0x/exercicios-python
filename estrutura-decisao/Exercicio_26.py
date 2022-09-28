#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro
#   Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipoCombustivel = input("Escolha o tipo de combustível. A - Álcool ou G - Gasolina: ").upper()

if(tipoCombustivel != "A" and tipoCombustivel != "G"):
    print("Opção inválida.")
else:
    qtdLitros = float(input("Digite a quantidade de litros: "))

    if(tipoCombustivel == "A"):
        precoCombustivel = 1.9
        if qtdLitros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
    else:
        precoCombustivel = 2.5
        if qtdLitros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
    
    total = (precoCombustivel * qtdLitros) * (1 - desconto)
    print(f"O total a pagar é: {total}")
