dia1 = int(input("Digite o dia da primeira data: "))
mes1 = int(input("Digite o mês da primeira data: "))
ano1 = int(input("Digite o ano da primeira data: "))

dia2 = int(input("Digite o dia da segunda data: "))
mes2 = int(input("Digite o mês da segunda data: "))
ano2 = int(input("Digite o ano da segunda data: "))

verificar_ano_recente = ano1 - ano2
verificar_mes_recente = mes1 - mes2
verificar_dia_recente = dia1 - dia2

verificar_dias = (dia1 < 1 or dia1 > 31) or (dia2 < 1 or dia2 > 31)
verificar_meses = (mes1 < 1 or mes1 > 12) or (mes2 < 1 or mes2 > 12)
verificar_anos = ano1 > 2022 or ano2 > 2022

if(verificar_dias or verificar_meses or verificar_anos):
    print("Datas inválidas.")
elif(verificar_ano_recente > 0):
    print(f"A data {dia1}/{mes1}/{ano1} é a mais recente.")
elif(verificar_mes_recente > 0 and verificar_ano_recente >= 0):
    print(f"A data {dia1}/{mes1}/{ano1} é a mais recente.")
elif(verificar_dia_recente > 0 and verificar_mes_recente >= 0 and verificar_ano_recente >= 0):
    print(f"A data {dia1}/{mes1}/{ano1} é a mais recente.")
elif(verificar_dia_recente == 0 and verificar_mes_recente == 0 and verificar_ano_recente == 0):
    print("As datas são identicas.")
else:
    print(f"A data {dia2}/{mes2}/{ano2} é a mais recente.")