def calcular_dobro_triplo(numero):
    if numero > 0:
        print(f"O dobro de {numero} é {numero * 2}.")
    else:
        print(f"O triplo de {numero} é {numero * 3}.")

numero = int(input("Digite um número: "))
calcular_dobro_triplo(numero)
