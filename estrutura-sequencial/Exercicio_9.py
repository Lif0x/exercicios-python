#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

temperaturaFahr = float(input("Digite a temperatura em Fahrenheit: "))
temperaturaCelsius = 5 * ((temperaturaFahr - 32) / 9)
print(f"A temperatura convertida em Celsius é de {temperaturaCelsius}")