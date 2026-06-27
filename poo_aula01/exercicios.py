from abc import ABC, abstractmethod

class Abstrata_Animal(ABC):

    def __init__(self, nome, peso_em_quilos):
        self.nome = nome
        self.peso_em_quilos = peso_em_quilos 


    @abstractmethod
    def emitir_som(self):
        print("Som")

    def comer(self, quantidade_em_gramas):
        self.quantidade_em_gramas = quantidade_em_gramas
        print(f"O peso do animal agora é de {self.peso_em_quilos} + {self.quantidade_em_gramas}")

    def andar(self, distancia_em_metros):
        self.distancia_em_metros = distancia_em_metros
        self.distancia_em_metros - self.peso_em_quilos
    
       

        