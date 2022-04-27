#programa que decifra senha com uso do cálculo de fatorial
print("Para que o cálculo seja realizado corretamente, insira apenas os números correspondentes aos MINUTOS atuais, como exibidos em seu relógio!")
#criação de variáveis
minutos = int(input("Insira os minutos como exibidos no relógio nesse momento: "))
i = minutos #variavel contadora
fatorial = 1

#iniciando loop - fatorial
while i > 0:
    fatorial = fatorial * i
    i = i - 1

#atribuindo o valor de fatorial a variável senha
senha = fatorial

#exibindo senha
print("A senha para liberação da máquina é LIBERDADE{}".format(senha))
