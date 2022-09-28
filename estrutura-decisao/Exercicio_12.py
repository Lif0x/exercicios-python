#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        #Salário Bruto: (5 * 220)        : R$ 1100,00
        #(-) IR (5%)                     : R$   55,00
        #(-) INSS ( 10%)                 : R$  110,00
        #FGTS (11%)                      : R$  121,00
        #Total de descontos              : R$  165,00
        #Salário Liquido                 : R$  935,00

valorHora = float(input("Digite o valor da hora: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
salario = valorHora * horasTrabalhadas

if (salario <= 900):
    descontoIR = 0
elif (salario <= 1500):
    descontoIR = 0.05
elif (salario <= 2500):
    descontoIR = 0.1
else:
    descontoIR = 0.2

IR = salario * descontoIR
INSS = salario * 0.1
FGTS = salario * 0.11
SINDICATO = salario * 0.03
descontos = IR + INSS + SINDICATO
salarioLiquido = salario - descontos

print(f'''
    Salário bruto: R$ {salario}
    IR: R$ {IR}
    INSS: R$ {INSS}
    FGTS: (Valor pago pela empresa) R$ {FGTS}
    Sindicato: R$ {SINDICATO}
    Total de descontos: R$ {descontos}
    Salário líquido: R$ {salarioLiquido}
''')
