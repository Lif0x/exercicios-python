#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Insira o ano: "))

if(ano % 400 == 0 or ano % 4 == 0):
    print("Esse ano é bissexto.")
else:
    print("Esse ano não é bissexto.")