#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58

alturaPessoa = float(input("Digite a sua altura (em M): "))
pesoIdeal = (72.7 * alturaPessoa) - 58
print(f"O seu peso ideal é {pesoIdeal} Kg")