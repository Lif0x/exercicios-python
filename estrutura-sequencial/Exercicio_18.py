#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input("Digite o tamanho do arquivo (em Mb): "))
velocidadeInternet = float(input("Digite a velocidade da internet (em Mbps): "))
tempoAproximadoSegundos = int(tamanhoArquivo // velocidadeInternet)
Minutos = tempoAproximadoSegundos // 60
Segundos = tempoAproximadoSegundos % 60

print(f"\nO tempo aproximado de download é de {Minutos} minuto(s) e {Segundos} segundo(s)")