#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo:
#       + Salário Bruto : R$
#       - IR (11%) : R$
#       - INSS (8%) : R$
#       - Sindicato ( 5%) : R$
#       = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido.

valorPorHora = float(input("Digite o valor ganho por hora (em R$): "))
horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valorPorHora * horasTrabalhadas
qtdPagamentoIR = salarioBruto * 0.11
qtdPagamentoInss = salarioBruto * 0.08
qtdPagamentoSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - qtdPagamentoIR - qtdPagamentoInss - qtdPagamentoSindicato

print(f"\nO seu salário bruto é de R$ {salarioBruto:.2f}")
print(f"O valor descontado para o imposto de renda é de R$ {qtdPagamentoIR}")
print(f"O valor descontado para o INSS é de R$ {qtdPagamentoInss}")
print(f"O valor descontado para o sindicato é de R$ {qtdPagamentoSindicato}")
print(f"O seu salário líquido é de R$ {salarioLiquido:.2f}")

