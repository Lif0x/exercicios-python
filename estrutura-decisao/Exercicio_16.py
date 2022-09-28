#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#   Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#   Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

valA = float(input("Digite o valor de A: "))

if valA == 0:
    print("Essa equação não é do segundo grau.")
else:
    valB = float(input("Digite o valor de B: "))
    valC = float(input("Digite o valor de C: "))
    delta = (valB**2) - (4 * valA * valC)

    if delta < 0:
        print("A equação não possuí raizes reais.")
    elif delta == 0:
        raiz = -valB / (2 * valA)
        print(f'''
            Delta = 0
            Raiz = {raiz}
        ''')
    else:
        raiz1 = (-valB + math.sqrt(delta)) / (2 * valA)
        raiz2 = (-valB - math.sqrt(delta)) / (2 * valA)
        print(f'''
            Delta = {delta}
            Raizes = {raiz1} e {raiz2}
        ''')