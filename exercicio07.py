def media(matriz, indice):
    soma = 0
    quant = 0
    for i in matriz:
        soma += i[indice]
        quant += 1
    media = soma / quant
    return media


informacoes = []
while True:
    pessoa = []
    pessoa.append(str(input("Digite o nome: ")))
    pessoa.append(str(input("Digite o CPF: ")))
    pessoa.append(int(input("Digite a idade: ")))
    pessoa.append(float(input("Digite a renda mensal: R$")))
    print("=" * 30)
    informacoes.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input("Deseja cadastrar mais uma pessoa? (S/N)\n>>>"))
        if resp not in "SsNn":
            print("Resposta inválida tente novamente")
            continue
        else:
            if resp in "Ss":
                break    
            elif resp in "Nn":
                break
    if resp in "Nn":
        break

cont = 0
print("\n")
for i in informacoes:
    cont += 1
    print(f"{cont} {i}")

media_idade = media(informacoes, 2)
media_mensal = media(informacoes, 3)
print("\n")
print(f"A média de idade é {media_idade}.")
print(f"A média de renda mensal é R${media_mensal}")
print("\n")