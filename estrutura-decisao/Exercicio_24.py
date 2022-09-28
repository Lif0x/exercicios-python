#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = input("Digite uma operação [+, -, / ou *]: ")
parOuImpar = "O número do resultado é par"
posiOuNeg = "O número do resultado é positivo"
intOuDec = "O número do resultado é inteiro"

if opcao not in "+-/*":
    print("Opção inválida")
else:
    if opcao == "+":
        resultado = num1 + num2
    elif opcao == "-":
        resultado = num1 - num2
    elif opcao == "/":
        resultado = num1 / num2
    elif opcao == "*":
        resultado = num1 * num2

    if resultado % 2 != 0:
        parOuImpar = "O número do resultado é ímpar"

    if resultado < 0:
        posiOuNeg = "O número do resultado é negativo"
    elif resultado == 0:
        posiOuNeg = "O número do resultado é neutro"

    if resultado != round(resultado):
        intOuDec = "O número do resultado é decimal"

    print(f'''
    O resultado da operação é {resultado:.2f}
    {parOuImpar}
    {posiOuNeg}
    {intOuDec}    
    ''')
