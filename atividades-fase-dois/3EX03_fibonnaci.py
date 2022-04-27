#programa que verifica se um número inteiro faz parte da sequência de Fibonnaci
print("Bem vind@! Vamos verificar se um número está ou não na sequência de Fibonnaci?")
#criação de variáveis
numero = int(input("Digite um número inteiro: "))
anterior = 0
proximo = 1
fibonnaci = 0

#iniciando loop
while proximo < numero:
    fibonnaci = proximo + anterior
    anterior = proximo
    proximo = fibonnaci

#exibindo resultado
if numero == proximo:
    print("Ação bem sucedida! {} faz parte da sequência de Fibonnaci.".format(numero))
else:
    print("A ação falhou... {} não faz parte da sequência de Fibonnaci.".format(numero))