#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

valorPorHora = float(input("Digite o valor ganho por hora: "))
quantidadeHoras = float(input("Digite a quantidade de horas trabalhadas: "))
salarioTotal = valorPorHora * quantidadeHoras
print(f"O salário do mês atual é {salarioTotal}")