import random
def gerarmatriz(qntlinha, qntcolunas):
    matriz = []
    for i in range(qntlinha):
        linha = []
        for j in range(qntcolunas):
            linha.append(random.randint(1,20))
        matriz.append(linha)
    return matriz
def imprimirmatriz(matriz):
    for linha in matriz:
        print (linha)

linhas = int(input("Informe o número de linhas da matriz: \n"))
colunas = int(input("Informe o número de colunas da matriz: \n"))
matriz = gerarmatriz(linhas,colunas)
imprimirmatriz(matriz)