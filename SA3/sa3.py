compra = float(input("\nValor Total da Compra: R$ "))
pagamento = float(input("\nValor recebido: R$ "))

while compra > pagamento: # caso o cliente pagar um valor menor da compra
    print("\033[1;31mValor errado!\033[m")
    pagamento = float(input("\nValor recebido: "))
else: # caso o cliente pagar um valor maior ou igual ao da compra
    troco = pagamento - compra
    print(f'\n\033[1;32mTroco: \033[mR$ {troco:.2f}\n')

for valor in [50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]:
    quantidade = troco // valor # divisão inteira que fornece a quantidade de notas e moedas
    troco = round((troco - (quantidade * valor)), 2) # valor que sobra a cada loop
    if quantidade > 0:
        if valor <= 1: # somente moedas como troco
            moeda = "moeda"
            valor = f'{valor:.2f}'.replace(".",",")
            if quantidade > 1:
                moeda = "moedas"
            print(f'{int(quantidade)} {moeda}: R$ {valor}')
        else: # somente notas como troco
            nota = "nota"
            valor = f'{valor:.2f}'.replace(".",",")
            if quantidade > 1:
                nota = "notas"
            print(f'{int(quantidade)} {nota}: R$ {valor}')


