def calcular_pagamento(preco, condicao):
    if condicao == 1:
        total = preco * 0.9
    elif condicao == 2:
        total = preco * 0.85
    elif condicao == 3:
        total = preco
    elif condicao == 4:
        total = preco * 1.1
    print(f"O valor a ser pago é R$ {total:.2f}")

preco = float(input("Digite o preço do produto: "))
condicao = int(input("Digite a condição de pagamento (1-4): "))
calcular_pagamento(preco, condicao)
