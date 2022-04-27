#Programa para cálculo do IMC

#Entrada de dados: peso em quilos e altura em metros
print("Olá! Vamos calcular seu IMC?")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

#Cálculo do IMC
imc = peso / (altura * altura)

#Saída do algoritmo
print(f"Seu IMC é {imc:.2f}") #Formatação para exibir apenas duas casas decimais

if imc < 16.00:
    print("Categoria: baixo peso III")
elif imc >= 16.00 and imc <= 16.99:
    print("Categoria: baixo peso II")
elif imc >= 17.00 and imc <= 18.49:
    print("Categoria: baixo peso grau I")
elif imc >= 18.50 and imc <= 24.99:
    print("Categoria: peso ideal")
elif imc >= 25.00 and imc <= 29.99:
    print("Categoria: sobrepeso")
elif imc >= 30.00 and imc <= 34.99:
    print("Categoria: obesidade grau I")
elif imc >= 35.00 and imc <= 39.99:
    print("Categoria: obesidade grau II")
elif imc >= 40.00:
    print("Categoria: obesidade grau III")
else:
    print("Dados inválidos, insira novamente.")
