# Exemplo de lista

lista = [10, 20, 30, 40, 50]

lista.append(60) #ele inclui o numero para a ultima posiçao da lista
print(lista)
lista[3] = 90 # esta mudando a posiçao 3 (do numero 40), para o numero 90
print (lista)

# Exemplo de tupla
tupla = (10, 20, 30, 40, 50)
print(tupla)
#a tupla nasce com valores e os valores nao podem ser alterados. em quanto lista podem ser modificadas


#Exemplo de dicionario (estrutura de dados)
#(conjunto de duas informaçoes, chaves e valores)

dicionario = {
    "RA" : "2345678", 
    "Nome" : "Gabriel pensador",
    "Idade" : 20,
    "Curso" : "TDS"
}

print(dicionario["Nome"])   #Dicionario é um vetor onde imprime textos em vez de numeros.

for item in lista:
    print(item)
                    #Ambos imprimem os itens(numeros) da lista.
for item in tupla:
    print(item)

print("Imprime o dicionario versao 1")
for chave in dicionario:
     print(chave, ":", dicionario[chave])

print("Imprime o dicionario versao 2")
for chave, valor in dicionario.items():
        print(chave, ":", valor)