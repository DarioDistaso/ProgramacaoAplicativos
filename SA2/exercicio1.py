# Exercício 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações: a) tamanho da lista; b) maior valor da lista; c) menor valor da lista; d) soma de todos os elementos da lista; e) lista em ordem crescente; f) lista em ordem decrescente.

# Inicialização das variáveis
L = [5, 7, 2, 9, 4, 1, 3]
tamanhoLista = 0
maior_valor = -999999999
menor_valor = 999999999
soma = 0

for numero in L:
    if numero > maior_valor:
        maior_valor = numero

    if numero < menor_valor:
        menor_valor = numero

    soma += numero # variável que retorna a soma dos números da lista
    tamanhoLista += 1 # variável que retorna o tamanho da lista


print(f'\nTamanho da lista: {tamanhoLista}')
print(f'\nMaior valor da lista: {maior_valor}')
print(f'\nMenor valor da lista: {menor_valor}')
print(f'\nSoma de todos os elementos da lista: {soma}')


for i in range(len(L) - 1): # repete a comparação pelo número de elementos na lista
    for j in range(len(L) - 1): # em cada iteração vai comparando os valores do primeiro índice da lista até o penúltimo 
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

print(f'\nLista em ordem crescente: {L}')


for i in range(len(L) - 1): 
    for j in range(len(L) - 1): # ordenação decrescente
        if L[j] < L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

print(f'\nLista em ordem decrescente: {L}')


