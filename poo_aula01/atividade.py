#criar a classe quadrado

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado* self.lado
    
    def calcular_perimetro(self):
        return 4 *  (self.lado)       
    
#CRIAR A CLASSE FUNCIONÁRIO	FUNCIONÁRIO, NOME, VALOR_HORA ,HORAS_TRABALHADAS, 
# CALCULAR_SALARIO_BRUTO( ), 
# CALCULAR_INSS( ) --> SALÁRIO < 2500 --> 9% | SE NÃO 12.5%
# CALCULAR_SALARIO_LIQUIDO( )
# MOSTRAR_HOLERITE( )