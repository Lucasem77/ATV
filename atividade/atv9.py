def calcular_peso_ideal(sexo, altura):
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    else:
        peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal é {peso_ideal:.2f} kg.")

sexo = input("Digite o sexo (M/F): ").upper()
altura = float(input("Digite a altura (em metros): "))
calcular_peso_ideal(sexo, altura)
