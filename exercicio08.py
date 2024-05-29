
jogovelha = [["1","2","3"],["4","5","6"],["7","8","9"]]

while True:
    contador = 0
    while True:
        contador += 1
        if contador % 2 == 0:
            saida = "X"
        else:
            saida = "O"
        for i in jogovelha:
            print(i)
        print("_" * 30)
        jogada = str(input(f"Vez do ({saida})\n Escolha a jogada: "))
        if jogada == "1":
            if jogovelha[0][0] != "1":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[0][0] = saida
        elif jogada == "2":
            if jogovelha[0][1] != "2":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[0][1] = saida
        elif jogada == "3":
            if jogovelha[0][2] != "3":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[0][2] = saida
        elif jogada == "4":
            if jogovelha[1][0] != "4":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[1][0] = saida
        elif jogada == "5":
            if jogovelha[1][1] != "5":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[1][1] = saida
        elif jogada == "6":
            if jogovelha[1][2] != "6":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[1][2] = saida
        elif jogada == "7":
            if jogovelha[2][0] != "7":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[2][0] = saida
        elif jogada == "8":
            if jogovelha[2][1] != "8":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[2][1] = saida
        elif jogada == "9":
            if jogovelha[2][2] != "9":
                print("Esta posição já foi escolhida!")
                contador -= 1
                continue
            else:
                jogovelha[2][2] = saida

        if jogovelha[0][0] == jogovelha[0][1] == jogovelha[0][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[1][0] == jogovelha[1][1] == jogovelha[1][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[2][0] == jogovelha[2][1] == jogovelha[2][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][0] == jogovelha[1][0] == jogovelha[2][0]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            print("=" * 30)
            break
        elif jogovelha[0][1] == jogovelha[1][1] == jogovelha[2][1]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][2] == jogovelha[1][2] == jogovelha[2][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][0] == jogovelha[1][1] == jogovelha[2][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][2] == jogovelha[1][1] == jogovelha[2][0]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        else:
            if contador == 9:
                print("=" * 30)
                print("EMPATE!!!")
                print("=" * 30)
                break
    while True:
        resposta = str(input("Deseja jogar denovo? (S/N)"))
        print("=" * 30)
        if resposta not in "SsNn":
            print("Digito inválido! Tente novamente.")
            continue
        elif resposta in "Ss":
            jogovelha.clear()
            jogovelha = [["1","2","3"],["4","5","6"],["7","8","9"]]
            break
        elif resposta in "Nn":
            break
    if resposta in "Nn":
        break
print("FIM DE JOGO!!!")