def gerar_matriz(qntlinhas,qntcolunas):
    matriz = []
    for i in range(qntlinhas):
        linha = []
        for j in range(qntcolunas):
            elemento = int(input(f"Informe M{i}{j}\n"))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)        

def soma_matriz (matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            if elemento % 2 == 0:
                soma += elemento
    return soma
def soma_coluna(matriz):
    while True:
        contador = 0
        coluna_escolhida = int(input("Informe a coluna a ser somada: "))
        for i in range( len(matriz[0])):
            contador += 1
        if  coluna_escolhida > 0 and coluna_escolhida <= contador:
            soma = 0
            for i in matriz:
                soma += i[coluna_escolhida - 1]
            return soma
        else:
            print("Esta coluna não existe! Tente novamente.")
            continue

linhas = int(input("Informe o número de linhas da matriz: \n"))
colunas = int(input("Informe o número de colunas da matriz: \n"))
matriz = gerar_matriz(linhas,colunas)
imprimir_matriz(matriz)
somcoluna = soma_coluna(matriz)
print(somcoluna)