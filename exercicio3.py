# Exercicio 3. Escreva um programa que leia 20 valores inteiros e informe a média deles, o maior e o menor valor.

# Inicialização das variáveis
soma = 0
maior_valor = -999999999
menor_valor = 999999999


for i in range(0,20):
    numero = int(input("\nDigite un valor: "))
    soma += numero # variável soma executa a soma dos 20 números digitados pelo usuário

    if numero > maior_valor: # condição para um numero se tornar o maior valor
        maior_valor = numero

    if numero < menor_valor: # condição para um numero se tornar o menor valor
        menor_valor = numero

media = soma / (i + 1)

print(f'\nA média dos valores digitados é: {media}') # impressão da média
print(f'\nO maior valor é: {maior_valor}') # impressão do maior valor
print(f'\nO menor valor é: {menor_valor}\n') # impressão do menor valor