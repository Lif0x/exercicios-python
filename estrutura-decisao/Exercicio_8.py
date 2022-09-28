#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a 
#decisão é sempre pelo mais barato.

preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))
menor = preco1
if(preco2 < menor):
    menor = preco2
if(preco3 < menor):
    menor = preco3
print(f"O menor preço é {menor}")