#esse programa calcula a quantidade de calorias ingeridas pelo usuário
#criação de variáveis
op = 0
nomeAlimento = ""
qtdeAlimento = 0.0
qtdeCalorias = 0.0
somaCalorias = 0.0
totalCalorias = 0.0

print("Bem vind@ ao contador de calorias diário Health Track!")

#iniciando loop - o programa continua solicitando as informações até que o usuário decida encerrá-lo
while op != 2:
    nomeAlimento = input("Insira o alimento ingerido: ")
    qtdeAlimento = float(input("Insira a quantidade/porção ingerida: "))
    qtdeCalorias = float(input("Insira a quantidade de calorias ingeridas: "))
    #calculo de calorias ingeridas e armazenamento na variavel
    somaCalorias = qtdeAlimento * qtdeCalorias
    totalCalorias = totalCalorias + somaCalorias
    #continuar ou não o loop
    op = int(input("Gostaria de registrar outro alimento?\n Digite 1 para SIM e 2 para NÃO: "))

#encerrando o programa
print("O total de calorias ingeridas hoje foi de {}".format(totalCalorias))