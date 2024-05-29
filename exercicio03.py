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

linhas = int(input("Informe o número de linhas da matriz: \n"))
colunas = int(input("Informe o número de colunas da matriz: \n"))
matriz = gerar_matriz(linhas,colunas)
imprimir_matriz(matriz)
somapares = soma_matriz(matriz)
print(f"A soma dos números pares da matriz é: {somapares}")



            
