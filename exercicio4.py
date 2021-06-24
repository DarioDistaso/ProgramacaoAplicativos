# Exercício 4. Crie uma função para desenhar uma linha, usando o caractere '_' 
# (underline). O tamanho da linha deve ser definido na chamada da função.

def linha (t):
    print("_" * t, "\n")

tamanho = int(input("\nDefina o tamanho da linha: "))

linha(tamanho)
