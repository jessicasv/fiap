#Programa que recebe a quantidade de votos que cada dia da semana obteve e exibe o dia mais votado.

#Entrada de dados: quantidade de votos para cada dia da semana
print("Esse programa calculará o melhor dia para as lives de acordo com os votos da turma. Não devem haver empates!")
segundaf = int(input("Insira quantidade de votos para segunda-feira: "))
tercaf = int(input("Insira a quantidade de votos para terça-feira: "))
quartaf = int(input("insira a quantidade de votos para quarta-feira: "))
quintaf = int(input("insira a quantidade de votos para quinta-feira: "))
sextaf = int(input("insira a quantidade de votos para sexta-feira: "))

#Processamento dos dados e saída do algoritmo
if segundaf > tercaf and segundaf > quartaf and segundaf > quintaf and segundaf > sextaf:
    print("O dia mais votado foi segunda feira!")
elif tercaf > segundaf and tercaf > quartaf and tercaf > quintaf and tercaf > sextaf:
    print("O dia mais votado foi terca-feira!")
elif quartaf > segundaf and quartaf > tercaf and quartaf > quintaf and quartaf > sextaf:
    print("O dia mais votado foi quarta-feira!")
elif quintaf > segundaf and quintaf > tercaf and quintaf > quartaf and quintaf > sextaf:
    print("O dia mais votado foi quinta-feira!")
elif sextaf > segundaf and sextaf > tercaf and sextaf > quartaf and sextaf > quintaf:
    print("O dia mais votado foi sexta-feira!")
else:
    print("Parece que houve um empate... refaça a votação")

