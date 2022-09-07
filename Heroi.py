class Heroi:
    def __init__(self, nome, idade, fraqueza):
        self.nome = nome
        self.idade = idade
        self.fraqueza = fraqueza
    
    def get_name(self):
        return self.nome
    
class HomemAranha(Heroi):
    def __init__(self, nome, idade, fraqueza, cidade):
        self.cidade = cidade
        super().__init__(nome, idade, fraqueza)
    
    def skill(self):
        return f'O poder do homem aranha é ser forte\n'

class Flash(Heroi):
    def __init__(self, nome, idade, fraqueza):
        super().__init__(nome, idade, fraqueza)
    
    def skill(self):
        return "O poder dele é a velocidade\n"

class Batman(Heroi):
    def __init__(self, nome, idade, fraqueza):
        super().__init__(nome, idade, fraqueza)
    
    def skill(self):
        return "poder de dormir\n"
        
heroi1 = HomemAranha('Peter Parker', '18 anos', 'a mulher', 'NY')
heroi1.get_name()
print ('o poder do homem aranha', heroi1.skill())

heroi2 = Flash('Barry Allen', '30 anos', 'a muie')
print('poder do flash', heroi2.skill())

heroi3 = Batman('Bruce', '30 anos', 'o coringa')
print ("Poder do batman é", heroi3.skill())