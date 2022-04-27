#programa que verifica se o bpm se encontra na faixa adequada de acordo com a idade
print("Bem vind@ ao verificador de BPM Health Track! Seu uso não substitui a avaliação de um especialista. ")
#criação de variáveis
idade = int(input("Insira sua idade: "))
bpm = int(input("Insira seus batimentos cardíacos por minuto (BPM): "))

#processamento de dados e saída do algoritmo
if idade >= 65 and bpm <= 60 and bpm >= 50:
    print("Seus batimentos estão DENTRO da faixa adequada para a sua idade!")
elif idade >= 65 and bpm > 60:
    print("Seus batimentos estão ACIMA da faixa adequada para a sua idade!")
elif idade >= 65 and bpm < 50:
    print("Seus batimentos estão ABAIXO da faixa adequada para a sua idade!")
elif idade <= 65 and idade >= 18 and bpm <= 80 and bpm >= 70:
    print("Seus batimentos estão DENTRO da faixa adequada para a sua idade!")
elif idade <= 65 and idade >= 18 and bpm > 80:
    print("Seus batimentos estão ACIMA da faixa adequada para a sua idade!")
elif idade <= 65 and idade >= 18 and bpm < 70:
    print("Seus batimentos estão ABAIXO da faixa adequada para a sua idade!")
elif idade <= 17 and idade >= 8 and bpm <= 100 and bpm >= 80:
    print("Seus batimentos estão DENTRO da faixa adequada para a sua idade!")
elif idade <= 17 and idade >= 8 and bpm > 100:
    print("Seus batimentos estão ACIMA da faixa adequada para a sua idade!")
elif idade <= 17 and idade >= 8 and bpm < 80:
    print("Seus batimentos estão ABAIXO da faixa adequada para a sua idade!")
elif idade <= 2 and bpm <= 140 and bpm >= 120:
    print("Seus batimentos estão DENTRO da faixa adequada para a sua idade!")
elif idade <=2 and bpm > 140:
    print("Seus batimentos estão ACIMA da faixa adequada para a sua idade!")
elif idade <= 2 and bpm < 120:
    print("Seus batimentos estão ABAIXO da faixa adequada para a sua idade!")
else:
    print("Idade não suportada pelo programa. Procure um especialista.")