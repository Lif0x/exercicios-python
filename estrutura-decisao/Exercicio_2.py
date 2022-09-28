#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Digite um número: "))
if(num > 0):
    print("Esse número é positivo.")
elif(num == 0):
    print("Esse número é neutro.")
else:
    print("Esse número é negativo.")