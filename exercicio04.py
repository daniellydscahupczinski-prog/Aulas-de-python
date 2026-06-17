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