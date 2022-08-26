#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = int(input("Digite o seu sexo: 1-Homem ou 2-Mulher \n"))
if sexo < 1 or sexo > 2:
    print("Sexo inválido")
else:
    altura = float(input("Digite a sua altura: "))
    if sexo == 1:
        pesoIdeal = (72.7 * altura) - 58
        print(f"O seu peso ideal é {pesoIdeal:.2f}")
    else:
        pesoIdeal = (62.1 * altura) - 44.7
        print(f"O seu peso ideal é {pesoIdeal}")