import os
from calculadora import Calculadora
from retangulo import Retangulo


def testa_retangulo():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    r1 = Retangulo(largura, altura)

    print(f"A área do retângulo é {r1.calcular_area()}")
    print(f"O perímetro do retângulo é {r1.calcular_perimetro()}")
    
def testa_calculadora():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    c1 = Calculadora(numero1, numero2)
    c2 = Calculadora(10, 8)

    print(f"A soma foi de {c1.somar()}")
    print(f"A subtração foi de {c1.subtrair()} e {c2.subtrair()}")
    print(f"A multiplicação foi de {c1.multiplicar()}")
    try:
        print(f"A divisão foi de {c1.dividir()}")
    except ValueError as e:
        print(e)

def main():

    os.system("cls" if os.name == "nt" else "clear")
    testa_calculadora()
    testa_retangulo()



if __name__ == "__main__":
    main()

