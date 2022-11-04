def soma_imposto (taxa_imposto, custo):
    global globalCusto
    globalCusto = custo + (custo/100*taxa_imposto)
    return globalCusto

globalCusto = float(input('Qual é o preço do produto? '))
taxa_imposto = float(input('Quantia de imposto em porcentagem: '))
print(f"O novo valor do produto é: {soma_imposto(taxa_imposto, globalCusto)}")
