def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

numero = int(input("Digite um número: "))
verificar_par_impar(numero)
