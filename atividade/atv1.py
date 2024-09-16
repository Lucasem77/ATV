def verificar_soma(a, b, c):
    if a + b < c:
        print("A soma de A + B é menor que C")
    else:
        print("A soma de A + B não é menor que C")


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
verificar_soma(a, b, c)
