#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
terceiroNumero = float(input("Digite o terceiro número: "))
dobroPrimeiroMetadeSegundo = (primeiroNumero * 2) * (segundoNumero / 2)
somaTriploPrimeiroTerceiro = (primeiroNumero * 3) + terceiroNumero
terceiroCubo = terceiroNumero**3
print(f"O produto do dobro do primeiro com metade do segundo é {dobroPrimeiroMetadeSegundo}")
print(f"A soma do triplo do primeiro com o terceiro {somaTriploPrimeiroTerceiro}")
print(f"O terceiro número elevado ao cubo é {terceiroCubo}")