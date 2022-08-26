#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

comprimento = float(input("Digite o comprimento do quadrado (em cm): "))
largura = float(input("Digite a largura do quadrado (em cm): "))
areaQuadrado = comprimento * largura
print(f"O dobro da área do quadrado em cm é {areaQuadrado * 2}")