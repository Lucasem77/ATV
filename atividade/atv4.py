def calcular(a, b):
    if a == b:
        c = a + b
    else:
        c = a * b
    print(f"O resultado é {c}")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
calcular(a, b)
