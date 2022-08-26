#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

metrosQuadrados = float(input("Digite a quantidade de metros quadrados: "))
litrosDeTinta = metrosQuadrados / 3
latasDeTinta = math.ceil(litrosDeTinta / 18)
valorTotal = latasDeTinta * 80

print(f"\nSerão necessárias {latasDeTinta} latas de tinta para pintar {metrosQuadrados} m²")
print(f"O valor total a ser pago é de R$ {valorTotal}")