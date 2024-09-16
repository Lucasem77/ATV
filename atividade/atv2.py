def solicitar_tempo_casada():
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo (M/F): ").upper()
    estado_civil = input("Digite seu estado civil: ").upper()

    if sexo == 'F' and estado_civil == 'CASADA':
        anos_casada = int(input("Quanto tempo você está casada (anos)? "))
        print(f"{nome}, você está casada há {anos_casada} anos.")
    else:
        print(f"{nome}, não é necessário informar o tempo de casada.")

solicitar_tempo_casada()
