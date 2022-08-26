#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raioCirculo = float(input("Digite o raio do círculo em cm: "))
areaCirculo = math.pi * raioCirculo**2
print(f"A área do círculo em cm é {areaCirculo}")