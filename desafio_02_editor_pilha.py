# desafio_02_editor_pilha.py

texto = []

while True:
    print("\n1 - Digitar palavra")
    print("2 - Desfazer última palavra")
    print("3 - Mostrar texto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        palavra = input("Digite uma palavra: ")
        texto.append(palavra)

    elif opcao == "2":
        if len(texto) > 0:
            removida = texto.pop()
            print(f"Palavra removida: {removida}")
        else:
            print("Nada para desfazer (pilha vazia).")

    elif opcao == "3":
        print("Texto atual:", " ".join(texto))

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")