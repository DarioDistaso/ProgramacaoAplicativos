# Exercício 5. Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A # função deve imprimir todos os elementos da lista, enumerando-os. 

# Lista de produtos
L = ["café", "fruta", "guardanapos", "água", "cerveja", "bolo", "refrigerante", "carne", "farinha", "arroz", "feijão"]

def listar_compras(lista): # função que recebe a lista como parâmetro
    for i in range(0,len(lista)):
        print(f'\nItem {i}: ', lista[i]) # a cada iteração imprime os itens da lista, enumerando-os
    print("\n")

listar_compras(L) # chamada da função passando a lista L como parâmetro


