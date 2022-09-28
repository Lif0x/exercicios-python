#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

telVitima = int(input("Telefonou para a vítima? 1(Sim) ou 0(Não): "))
localCrime = int(input("Esteve no local do crime? 1(Sim) ou 0(Não): "))
moraPertoVitima = int(input("Mora perto da vítima? 1(Sim) ou 0(Não): "))
deviaVitima = int(input("Devia para a vítima? 1(Sim) ou 0(Não): "))
trabalhouVitima = int(input("Já trabalhou com a vítima? 1(Sim) ou 0(Não): "))

respostas = telVitima + localCrime + moraPertoVitima + deviaVitima + trabalhouVitima

if(respostas < 2):
    print("\nInocente")
elif(respostas == 2):
    print("\nSuspeita")
elif(respostas <= 4):
    print("\nCúmplice")
elif respostas == 5:
    print("\nAssassino")