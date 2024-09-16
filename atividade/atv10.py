def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        condicao = "Abaixo do peso"
    elif imc < 25:
        condicao = "Peso normal"
    elif imc < 30:
        condicao = "Acima do peso"
    else:
        condicao = "Obeso"
    print(f"O IMC é {imc:.2f}. Condição: {condicao}")

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))
calcular_imc(peso, altura)
