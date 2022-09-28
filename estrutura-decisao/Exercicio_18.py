#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia1 = int(input("Digite o dia da primeira data: "))
mes1 = int(input("Digite o mês da primeira data: "))
ano1 = int(input("Digite o ano da primeira data: "))

verificar_dias = (dia1 < 1 or dia1 > 31)
verificar_meses = (mes1 < 1 or mes1 > 12)
verificar_anos = ano1 < 0

if(verificar_dias or verificar_meses or verificar_anos):
    print("Datas inválidas.")
else:
    print("A data é válida.")