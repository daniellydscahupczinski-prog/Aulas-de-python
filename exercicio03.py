# Crie uma lista de produtos (ID, Nome, Valor_unitario, Estoque)
from colorama import Fore, init
init(autoreset=True)
produtos = [
    {
        "ID" : 1,
        "Nome" : "Cadeira",
        "Valor_unitario" : 50.50,
        "Estoque" : 100
    },
    {
        "ID" : 2,
        "Nome" : "Mesa",
        "Valor_unitario" : 100.00,
        "Estoque" : 51
    },
    {
        "ID" : 3,
        "Nome" : "Sofa",
        "Valor_unitario" : 300.00,
        "Estoque" : 49
    },
    {
        "ID" : 4,
        "Nome" : "Cama",
        "Valor_unitario" : 1500.99,
        "Estoque" : 11
    },
    {
        "ID" : 5,
        "Nome" : "Roupeiro",
        "Valor_unitario" : 800.00,
        "Estoque" : 9
    }
]
# Exiba a lista de produtos com: ID, Nome, Valor_unitario, Estoque, Valor em estoque (valor unitario * estoque), Status estoque <= 10 baixo, estoque <= 50 atencao, estoque > 50 ok

for produto in produtos:
    print(Fore.CYAN + "ID:", produto["ID"])
    print("Produto:", produto["Nome"])
    print("Valor: R$",produto["Valor_unitario"])
    print("Unidades em estoque:", produto["Estoque"])
    Valor_estoque = (produto["Valor_unitario"] * produto["Estoque"])
    print("Valor em estoque do produto: R$", Valor_estoque)
    if produto["Estoque"] <= 10:
        print(Fore.RED + "Quantidade em estoque: insuficiente")
    elif produto["Estoque"] <= 50:
        print(Fore.YELLOW + "Quantidade em estoque: atenção")
    else:
        print(Fore.GREEN + "Quantidade em estoque: OK")
    print("-" * 40)


    # OUTRO JEITO MAIS BONITO DE MOSTRAR O DICIONARIO
    
    from colorama import Fore, init, Style

def calcular_valor_estoque(produto):
    return produto["valor_unitario"] * produto["estoque"]

def analisar_estoque(produto):
    if produto["estoque"] <= 10 :
        return Fore.RED + Style.BRIGHT, "Estoque baixo"
    elif produto["estoque"] <= 50:
        return Fore.YELLOW + Style.BRIGHT, "Atenção"
    else:
        return Fore.GREEN + Style.BRIGHT, "Ok"

init(autoreset=True)

produtos = [
    {
        "id": 1,
        "nome": "Notebook Dell",
        "valor_unitario": 3500.00,
        "estoque": 10
    },
    {
        "id": 2,
        "nome": "Notebook Lenovo",
        "valor_unitario": 3200.00,
        "estoque": 15
    },    
    {
        "id": 3,
        "nome": "Notebook HP",
        "valor_unitario": 3000.00,
        "estoque": 80
    }
]

print(Fore.GREEN + Style.BRIGHT + "=" *100)
print(Fore.GREEN + Style.BRIGHT + f"{'LISTA DE PRODUTOS':^100}")
print(Fore.GREEN + Style.BRIGHT + "=" *100)
print(Fore.GREEN + Style.BRIGHT + f"{'ID':<5} {'NOME':<25} {'VALOR UNITÁRIO':<20} {'ESTOQUE':<10} {'VALOR ESTOQUE':<20} {'STATUS':<20}")
print(Fore.GREEN + Style.BRIGHT + "-" *100)
for produto in produtos:
    valor_estoque = calcular_valor_estoque(produto)
    cor, status = analisar_estoque(produto)

    print(Fore.BLUE + Style.BRIGHT + f"{produto['id']:<5} {produto['nome']:<25} R${produto['valor_unitario']:<20.2f} {produto['estoque']:<10} R${valor_estoque:<15.2f} {cor + status:<20}")
print(Fore.GREEN + Style.BRIGHT + "-" *100)