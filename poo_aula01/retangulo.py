class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
      
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def main():
        calcular_area()
        calcular_perimetro()

    if __name__ == "__main__":
    main()
