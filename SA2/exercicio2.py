# Exercício 2. Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo (para ser positivo a média deve ser acima de 1).

#Inicialização da variável soma
soma = 0

for i in range(0,4): # loop para digitar 4 números
    numero = int(input("\nDigite um numero: "))
    soma += numero # a cada loop a variável soma recebe a soma dos valores digitados

media = soma / (i + 1) # cálculo da média: soma dividido pelo numero de valores digitados

print(f'\nA média dos numeros digitados é: {media}\n')

if media > 1:
    print("Positivo\n")

else:
    print("Negativo\n")