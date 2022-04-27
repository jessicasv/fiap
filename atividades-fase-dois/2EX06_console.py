#programa que recebe os votos dos 5 membros da equipe e exibe a opção mais votada
print("Parabéns pelo ótimo desempenho! Insira a sua opção preferida entre os consoles: PLAYSTATION, XBOX e NINTENDO.")
#criação de variáveis e entrada de dados
pessoa1 = str(input("1. Insira o voto do primeiro membro da equipe: "))
pessoa2 = str(input("2. Insira o voto do segundo membro da equipe: "))
pessoa3 = str(input("3. Insira o voto do terceiro membro da equipe: "))
pessoa4 = str(input("4. Insira o voto do quarto membro da equipe: "))
pessoa5 = str(input("5. Insira o voto do quinto membro da equipe: "))

#execução do algoritmo e exibição do resultado
if pessoa1.upper() == "PLAYSTATION" and pessoa2.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION" and pessoa5.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 5 votos!")
elif pessoa1.upper() == "PLAYSTATION" and pessoa2.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 4 votos!")
elif pessoa1.upper() == "PLAYSTATION" and pessoa2.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa1.upper() == "PLAYSTATION" and pessoa2.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa1.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa1.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION" and pessoa5.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa1.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION" and pessoa5.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa2.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa2.upper() == "PLAYSTATION" and pessoa3.upper() == "PLAYSTATION" and pessoa5.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa3.upper() == "PLAYSTATION" and pessoa4.upper() == "PLAYSTATION" and pessoa5.upper() == "PLAYSTATION":
    print("PLAYSTATION foi o console escolhido com 3 votos!")
elif pessoa1.upper() == "XBOX" and pessoa2.upper() == "XBOX" and pessoa3.upper() == "XBOX" and pessoa4.upper() == "XBOX" and pessoa5.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 5 votos!")
elif pessoa1.upper() == "XBOX" and pessoa2.upper() == "XBOX" and pessoa3.upper() == "XBOX" and pessoa4.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 4 votos!")
elif pessoa1.upper() == "XBOX" and pessoa2.upper() == "XBOX" and pessoa3.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa1.upper() == "XBOX" and pessoa2.upper() == "XBOX" and pessoa4.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa1.upper() == "XBOX" and pessoa3.upper() == "XBOX" and pessoa4.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa1.upper() == "XBOX" and pessoa3.upper() == "XBOX" and pessoa5.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa1.upper() == "XBOX" and pessoa4.upper() == "XBOX" and pessoa5.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa2.upper() == "XBOX" and pessoa3.upper() == "XBOX" and pessoa4.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa2.upper() == "XBOX" and pessoa3.upper() == "XBOX" and pessoa5.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa3.upper() == "XBOX" and pessoa4.upper() == "XBOX" and pessoa5.upper() == "XBOX":
    print("O console XBOX ganhou com o total de 3 votos!")
elif pessoa1.upper() == "NINTENDO" and pessoa2.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO" and pessoa5.upper() == "NINTENDO":
    print("Com 5 votos... o escolhido foi o console NINTENDO!")
elif pessoa1.upper() == "NINTENDO" and pessoa2.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO":
    print("Com 4 votos... o escolhido foi o console NINTENDO!")
elif pessoa1.upper() == "NINTENDO" and pessoa2.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa1.upper() == "NINTENDO" and pessoa2.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa1.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa1.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO" and pessoa5.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa1.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO" and pessoa5.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa2.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa2.upper() == "NINTENDO" and pessoa3.upper() == "NINTENDO" and pessoa5.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
elif pessoa3.upper() == "NINTENDO" and pessoa4.upper() == "NINTENDO" and pessoa5.upper() == "NINTENDO":
    print("Com 3 votos... o escolhido foi o console NINTENDO!")
else:
    print("Ops! Parece que houve um empate... Refaça a votação.")