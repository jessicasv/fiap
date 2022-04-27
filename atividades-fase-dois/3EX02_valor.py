#programa que recebe a quantidade e valor das transações realizadas no dia e mostra o total e média de gastos
print("Bem vind@! Vamos acompanhar seus gastos de hoje?")
#criação de variáveis
qtdeTransacoes = float(input("Quantas transações financeiras você realizou hoje? "))
i = 1 #variável contadora
gastoTotal = 0.0
gastoMedia = 0.0

#iniciando loop
while i <= qtdeTransacoes:
    gastoTotal = gastoTotal + float(input("Qual foi o valor da {}ª transação? R$".format(i)))
    i = i + 1

#cálculo da média de gastos do dia
gastoMedia = gastoTotal / qtdeTransacoes

#exibindo o resultado
print("O valor total de suas {:.0f} transações é de R${:.2f}.".format(qtdeTransacoes, gastoTotal))
print("A média de gastos do dia é de R${:.2f}".format(gastoMedia))