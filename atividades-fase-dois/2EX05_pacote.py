#programa que calcula desconto e média de acordo com a categoria do passageiro
print("Bem vind@! Para verificar o desconto da sua viagem, preencha os dados abaixo.")
#criação de variáveis
valorBruto = float(input("Insira o VALOR BRUTO do pacote: R$"))
categoria = str(input("Insira o número correspondente à categoria dos assentos: 1 para PRIMEIRA CLASSE, 2 para EXECUTIVA e 3 para ECONÔMICA: "))
viajantes = float(input("Insira a quantidade de passageiros: "))
valorLiquido = 0.0
valorDesconto = 0.0
valorMedio = 0.0

#execução do algoritmo
if categoria == "1" and viajantes >= 4:
    valorDesconto = valorBruto * 0.20
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "1" and viajantes == 3:
    valorDesconto = valorBruto * 0.15
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "1" and viajantes == 2:
    valorDesconto = valorBruto * 0.1
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "2" and viajantes >= 4:
    valorDesconto = valorBruto * 0.08
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "2" and viajantes == 3:
    valorDesconto = valorBruto * 0.07
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "2" and viajantes == 2:
    valorDesconto = valorBruto * 0.05
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "3" and viajantes >= 4:
    valorDesconto = valorBruto * 0.05
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "3" and viajantes == 3:
    valorDesconto = valorBruto * 0.04
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
elif categoria == "3" and viajantes == 2:
    valorDesconto = valorBruto * 0.03
    valorLiquido = valorBruto - valorDesconto
    valorMedio = valorLiquido / viajantes
else:
    print("Informações inválidas. Por favor, verifique e insira novamente.")
    print("A oferta de desconto é válida somente para grupos de 2 ou mais pessoas.")

#saída do algoritmo
print("O VALOR BRUTO da sua viagem é de R${:.2f}. O VALOR DO DESCONTO concedido é de R${:.2f}.".format( valorBruto, valorDesconto))
print("O VALOR LÍQUIDO da viagem é de R${:.2f}, sendo a MÉDIA de R${:.2f} por passageiro.".format(valorLiquido, valorMedio))
print("Boa viagem!")