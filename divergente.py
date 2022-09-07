#o filme tem 5 divisões feitas por faccoes e cada uma representa um valor diferente,
#ai quando eu criar um personagem eu posso fazer com que ele digite o valor que ele se identifica
#a partir disso o codigo retorna na tela para qual faccão ele vai.

#Abnegção = altruistas
#erudicao = inteligente
#audacia = coragem
#amizade = bondosos
#franqueza = honestos

#Tris -> abnegacao
#quatro -> coragem
#caleb -> amizade
#christina -> franqueza
# Ana -> erudição

#opcao2
#cria o personagem e as faccoes, e coloca cada um nas suas respectivas faccoes.

class Faccoes: 
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
class Abnegacao(Faccoes):
    def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)
        
    carct_abnega = Faccoes('Tris', 'Altruismo')
    print ('o nome é', carct_abnega.nome) 
    print("o valor é ", carct_abnega.valor)
 
class Audacia(Faccoes):
    def __init__(self, nome, valor, participante):
        self.participante = participante
        super().__init__(nome, valor)
        
    caract_audacia = Faccoes('quatro', 'coragem')
    print("o valor é ",caract_audacia.valor)
    print("o nome do personagem é ", caract_audacia.nome)
            
#class Amizade(Faccoes):
   # def __init__(self, nome, valor, participante):
       # self.participante = participante
       # super().__init__(nome, valor)

#class Franqueza(Faccoes):
    # def __init__(self, nome, valor, participante):
       # self.participante = participante
       # super().__init__(nome, valor)

#class Erudicao(Faccoes):
  # def __init__(self, nome, valor, participante):
      #  self.participante = participante
       # super().__init__(nome, valor)

#Audacia1 = Audacia('audacia', 'coragem','ana vitoria')
#print(Audacia1.nome)
#rint(Audacia1.participante)
#print(Audacia1.valor)