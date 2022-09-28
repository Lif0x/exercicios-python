#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Digite um número inteiro menor que 1000: "))

centenas = num // 100
valorAposCentenas = num % 100
dezenas = valorAposCentenas // 10
valorAposDezenas = valorAposCentenas % 10
unidades = valorAposDezenas
cent = "Centena"
deze = "Dezena"
uni = "Unidade"

if centenas > 1:
    cent = "Centenas"
if dezenas > 1:
    deze = "Dezenas"
if unidades > 1:
    uni = "Unidades"

if centenas == 0 and dezenas == 0:
    print(f"{unidades} {uni}")
elif centenas == 0:
    print(f"{dezenas} {deze} e {unidades} {uni}")
else:
    print(f"{centenas} {cent}, {dezenas} {deze} e {unidades} {uni}")