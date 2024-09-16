def somar_par_impar(numero):
    if numero % 2 == 0:
        resultado = numero + 5
    else:
        resultado = numero + 8
    print(f"O resultado é {resultado}")

numero = int(input("Digite um número: "))
somar_par_impar(numero)
