#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num3 > num2:
    inverte = num3
    num3 = num2
    num2 = inverte

if num2 > num1:
    inverte = num2
    num2 = num1
    num1 = inverte

if num3 > num2:
    inverte = num3
    num3 = num2
    num2 = inverte

print(f"{num1} - {num2} - {num3}")