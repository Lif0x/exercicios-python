#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de 
#cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valorSaque = int(input("Digite o valor de saque: "))

notas100 = valorSaque // 100
notasApos100 = valorSaque % 100
notas50 = notasApos100 // 50
notasApos50 = notasApos100 % 50
notas10 = notasApos50 // 10
notasApos10 = notasApos50 % 10
notas5 = notasApos10 // 5
notas1 = notasApos10 % 5

if notas100 == 0 and notas50 == 0 and notas10 == 0 and notas5 == 0:
    print(f"Seram necessárias {notas1} nota(s) de R$ 1.00.")
elif notas100 == 0 and notas50 == 0 and notas10 == 0:
    print(f"Seram necessárias {notas5} nota(s) de R$ 5.00 e {notas1} nota(s) de R$1.00")
elif notas100 == 0 and notas50 == 0:
    print(f"Seram necessárias {notas10} nota(s) de R$ 10.00, {notas5} nota(s) de R$5.00 e {notas1} nota(s) de R$ 1.00")
elif notas100 == 0:
    print(f"Seram necessárias {notas50} nota(s) de R$ 50.00, {notas10} nota(s) de R$10.00, {notas5} nota(s) de R$ 5.00 e {notas1} nota(s) de R$ 1.00")
else:
    print(f"Seram necessárias {notas100} nota(s) de R$ 100.00, {notas50} nota(s) de R$50.00, {notas10} nota(s) de R$ 10.00, {notas5} nota(s) de R$ 5.00 e {notas1} nota(s) de R$ 1.00")
