#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Digite F ou M: ")).upper()
if(sexo == "F"):
    print("F - Feminino")
elif(sexo == "M"):
    print("M - Masculino")
else:
    print("Sexo inválido")