from exercicios import Abstrata_Animal

class Cachorro_Gato(Abstrata_Animal):
    def __init__(self, nome, peso_em_quilos, animal_gato, animal_cachorro, porte_cachorro):
        super().__init__(nome, peso_em_quilos)
        self.animal_gato = animal_gato
        self.animal_cachorro = animal_cachorro
        self.porte_cachorro = porte_cachorro

    def emitir_som(self, animal_gato, animal_cachorro):
        self.animal_gato = animal_gato
        if self.animal_gato:
            print("Miau Miau")
        self.animal_cachorro
        print("Au Au")

    def Porte(self, animal_cachorro, porte_cachorro):
        self.animal_cachorro = animal_cachorro
        self.porte_cachorro = porte_cachorro
        if self.porte_cachorro == "P":
            
 
