
while True:
    try: #comando de protecao 
        valor1 = int(input("Digite o primeiro valor: "))
        break
    except ValueError: #o execept procura se o erro que aconteceu esta mapeado na linha de baixo
        print("valor invalido, por favor, digite um numero inteiro.")
    except KeyboardInterrupt: #como se fosse o ctrl c do c++ (interrupçao)
        print("\n Operação cancelada pelo usuario. ")
        exit(1)


while True:
    try: #comando de protecao 
        valor2 = int(input("Digite o segundo valor: "))
        break
    except ValueError: #o execept procura se o erro que aconteceu esta mapeado na linha de baixo
        print("valor invalido, por favor, digite um numero inteiro.")
    except KeyboardInterrupt: #como se fosse o ctrl c do c++ (interrupçao)
        print("\n Operação cancelada pelo usuario. ")
        exit(1)


while True:
    print("Selecione um opcao: ")
    print("1 - Adiçao")
    print("2 - Subtraçao")
    print("3 - Multiplicaçao")
    print("4 - Divisao")
    try:
        opcao = int(input("Digite a opcao desejada: "))
        break
    except ValueError:
        print("Opcao invalida, por favor, digite um numero.")
    except KeyboardInterrupt:
        print("\n Operacao cancelada pelo usuario.")
        exit(1)

resultado = None # como se fosse nulo

match opcao:  #match significa switch no python
    case 1:
        resultado = valor1 + valor2     
    case 2:
        resultado = valor1 - valor2
    case 3:
        resultado = valor1 * valor2
    case 4:
        try:
            resultado = valor1 / valor2
        except ZeroDivisionError:
            print("Erro: divisao por zero nao é permitida.")
    case _:
        print("opçao invalida")
if resultado is not None:
    print("Resultado: ", resultado)

