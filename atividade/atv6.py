def verificar_booleanos(valor1, valor2):
    if valor1 and valor2:
        print("Ambos são VERDADEIROS.")
    else:
        print("Ambos não são VERDADEIROS.")

valor1 = bool(int(input("Digite 1 para VERDADEIRO e 0 para FALSO para o primeiro valor: ")))
valor2 = bool(int(input("Digite 1 para VERDADEIRO e 0 para FALSO para o segundo valor: ")))
verificar_booleanos(valor1, valor2)
