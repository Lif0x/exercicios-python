#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
#   isto é, considere latas cheias.

import math

metrosQuadrados = float(input("Digite a quantidade de metros quadrados: "))
litrosDeTinta = metrosQuadrados / 6
ApenasLatasDeTinta = math.ceil(litrosDeTinta / 18)
ApenasGaloesDeTinta = math.ceil(litrosDeTinta / 3.6)
valorTotalLatas = ApenasLatasDeTinta * 80
valorTotalGaloes = ApenasGaloesDeTinta * 25
latasAmbos = int(litrosDeTinta // 18)
litrosGaloesRestantesAmbos = litrosDeTinta % 18
galoesAmbos = math.ceil(litrosGaloesRestantesAmbos / 3.6)
valorTotalAmbos = (latasAmbos * 80) + (galoesAmbos * 25)

print(f"\nSerão necessárias {ApenasLatasDeTinta} latas de tinta para pintar {metrosQuadrados} m² e o valor total é de R$ {valorTotalLatas}")
print("\nOu")
print(f"\nSerão necessários {ApenasGaloesDeTinta} galões de tinta para pintar {metrosQuadrados} m² e o valor total é de R$ {valorTotalGaloes}")
print("\nOu")
print(f"\nSerão necessários {latasAmbos} latas e {galoesAmbos} galões para pintar {metrosQuadrados} m² e o valor total é de R$ {valorTotalAmbos}")