#Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = num1
if(num2 > maior):
    maior = num2
elif(num3 > maior):
    maior = num3
print(f"O maior número é {maior}")