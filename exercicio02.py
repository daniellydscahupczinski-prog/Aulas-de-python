from colorama import Fore, init, Back, Style  # DA BIBLIOTECA COLORAMA IMPORTE AS CLASSES QUE VOCE QUER IMPORTAR

init(autoreset = True)

def ler_dados(): #def é pra criar uma funçao
    while True:
        try:
            valor = int(input("Digite um número inteiro (0 para encerrar): "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

total_pares = 0
total_impares = 0

valor = ler_dados()

while valor != 0:
    if valor % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
    valor = ler_dados()
print(Fore.GREEN + f"Total de números pares: {Fore.BLUE}{total_pares}")
print(Fore.GREEN + f"Total de números ímpares: {Fore.RED}{total_impares}")