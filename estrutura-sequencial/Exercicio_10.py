#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperaturaCelsius = float(input("Digite a temperatura em Celsius: "))
temperaturaFahr = (temperaturaCelsius * 9/5) + 32
print(f"A temperatura convertida em Fahrenheit é de {temperaturaFahr} ")