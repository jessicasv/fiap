#Programa para calcular o bônus a ser pago pelos clientes do estúdio de acordo com seu tipo de assinatura.

#Entrada de dados do cliente: nome para identificação, tipo de assinatura e faturamento
print("Insira abaixo os dados do cliente para visualizar o valor do bônus a ser recebido.")
nome = input("Insira o nome do cliente: ")
assinatura = input("Insira o tipo de assinatura (basic, silver, gold ou platinum): ")
faturamento = float(input("Insira o faturamento anual do canal em R$: "))

#Variável para armazenar o valor do bônus a ser recebido
bonus = 0

#Realização do cálculo do percentual a ser recebido e saída do algoritmo
if assinatura == "basic":
    bonus = faturamento * 0.3
    print(f"O valor a ser pago pelo cliente {nome} do plano de assinatura 'basic' é R${bonus}")
elif assinatura == "silver":
    bonus = faturamento * 0.2
    print(f"O valor a ser pago pelo cliente {nome} do plano de assinatura 'silver' é R${bonus}")
elif assinatura == "gold":
    bonus = faturamento * 0.1
    print(f"O valor a ser pago pelo cliente {nome} do plano de assinatura 'gold' é R${bonus}")
elif assinatura == "platinum":
    bonus = faturamento * 0.05
    print(f"O valor a ser pago pelo cliente {nome} do plano de assinatura 'platinum' é R${bonus}")
else:
    print("Assinatura inválida. Preencha novamente.")
