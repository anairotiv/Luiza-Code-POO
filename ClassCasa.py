class HogwartsHouse:
    def __init__(self, name, color, founder, participants):
        self.name = name
        self.color = color
        self.founder = founder
        self.partipants = participants

    def get_points_house(self):
        return f"A casa {self.name} possui a pontuação total \
        de 50 pontos"

    def play_quidditch(self):
        return f"A pontuação do quadribol foi de 10 pontos"
    
    def nome_participante(self):
        return f"um dos partipcipantes da casa Lufa-Lufa é {self.partipants}"


hufflepuff = HogwartsHouse('Lufa-Lufa',
                           'Amarelo e Preto',
                           'Helga Lufa-Lufa',
                           'Cedrico Diggory')

points_house = hufflepuff.get_points_house()
print('Pontuação =>', points_house)
print(f"a cor da casa é", hufflepuff.color)


#metodo privado não acessa pela classe.

#Griffinory = HogwartsHouse ("Grifinória",
                          # "vermelho e amarelo",
                          #  "Godric Grifindor",
                          # "Dumbledore")
