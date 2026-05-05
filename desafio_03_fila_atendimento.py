# desafio_03_fila_atendimento.py

fila = []

while True:
    print("\n1 - Chegar aluno")
    print("2 - Atender aluno")
    print("3 - Mostrar fila")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        fila.append(nome)

    elif opcao == "2":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Aluno atendido: {atendido}")
        else:
            print("Fila vazia.")

    elif opcao == "3":
        print("Fila atual:", fila)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")