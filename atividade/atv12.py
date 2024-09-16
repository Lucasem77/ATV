def calcular_media(nota1, nota2, nota3, me):
    ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7
    if ma >= 90:
        conceito = 'A'
    elif ma >= 75:
        conceito = 'B'
    elif ma >= 60:
        conceito = 'C'
    elif ma >= 40:
        conceito = 'D'
    else:
        conceito = 'E'
    
    status = "Aprovado" if conceito in ['A', 'B', 'C'] else "Reprovado"
    print(f"Média de Aproveitamento: {ma:.2f}. Conceito: {conceito}. Status: {status}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
me = float(input("Digite a média dos exercícios: "))
calcular_media(nota1, nota2, nota3, me)
