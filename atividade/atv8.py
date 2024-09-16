def ordenar_decrescente(a, b, c):
    numeros = [a, b, c]
    numeros.sort(reverse=True)
    print(f"Números em ordem decrescente: {numeros}")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
ordenar_decrescente(a, b, c)
