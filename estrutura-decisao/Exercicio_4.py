#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite um letra: "))
vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
if(letra in vogais):
    print(f"A letra {letra} é uma vogal.")
elif(letra in consoantes):
    print(f"A letra {letra} é uma consoante.")
else:
    print("Letra inválida.")