#esse programa recebe a nota dos alunos pares e ímpares, calcula a media e exibe a maior.
print("Vamos calcular a média dos números impares e depois dos números pares")

#criação de variáveis
alunoImpar = 1
alunoPar = 0
notaImpar = 0.0
notaPar = 0.0
totalImpar = 0.0
totalPar = 0.0
mediaImpar = 0.0
mediaPar = 0.0

#iniciando loop - alunos ímpares
for alunoImpar in range(1, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    notaImpar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(alunoImpar)))
    totalImpar = totalImpar + notaImpar
    alunoImpar = alunoImpar + 2

#calculo da média dos alunos ímpares
mediaImpar = totalImpar / 25

#exibição do resultado da média dos alunos ímpares
print("MÉDIA DOS ALUNOS ÍMPARES: {:.1f}".format(mediaImpar))

#iniciando loop - alunos pares
for alunopar in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    notaPar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(alunoPar)))
    totalPar = totalPar + notaPar
    alunoPar = alunoPar + 2

#calculo da média dos alunos pares
mediaPar = totalPar / 25

#exibição do resultado da média dos alunos pares
print("MÉDIA DOS ALUNOS PARES {:.1f}".format(mediaPar))

#exibindo resultado final
if mediaImpar > mediaPar:
    print("OS ALUNOS ÍMPARES OBTIVERAM O MELHOR DESEMPENHO, COM A MÉDIA DE {:.1f}".format(mediaImpar))
    print("A MÉDIA DOS ALUNOS PARES FOI DE {:.1f}".format(mediaPar))

elif mediaImpar == mediaPar:
    print("AMBOS OS ALUNOS PARES E ÍMPARES OBTIVERAM A MÉDIA DE {:.1f}".format(mediaImpar))

else:
    print("OS ALUNOS PARES OBTIVERAM O MELHOR DESEMPENHO, COM A MÉDIA DE {:.1f}".format(mediaPar))
    print("A MÉDIA DOS ALUNOS ÍMPARES FOI DE {:.1f}".format(mediaImpar))