class HogwartsHouse:
    def __init__(self, competidor1, competidor2, competidor3):
        self.competidor1 = competidor1
        self.competidor2 = competidor2
        self.competidor3 = competidor3
        

class Torneio:
    def __init__(self, primeira,segunda,terceira):
        self.primeira = primeira
        self.segunda = segunda
        self.terceira = terceira
        
    Nomes = HogwartsHouse ("Harry potter",
                           "cedrico diggory",
                            "vitor crum")
        
    Torneio = HogwartsHouse ('ovo de ouro',
                             'lago',
                             "labirinto")
    
    print (Nomes.__dict__)
        
                            
    
        
    # Griffinory = HogwartsHouse ("Grifinória",
                          # "vermelho e amarelo",
                          #  "Godric Grifindor",
                          #  "Dumbledore")

#torneio 1; ovo de ouro
# torneio 2; lago
# torneio 3, labirinto


