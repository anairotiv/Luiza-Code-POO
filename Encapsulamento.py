class Hogwarts:
    def __init__(self, houses):
        self.houses = houses
    
    def get_houses(self):
        msg_houses = ', '.join(self.houses)
        return msg_houses
    
    def __get_secret_access(self):
        return "A camera secreta foi aberta!"

    def access_secret_camera(self, witch):
        if witch == "Harry":
            return self.__get_secret_access()
        
        return "Voce não tem acesso a esse local"
    
school = Hogwarts(['Grifinória', 'Lufa-Lufa', 'Sonserina', 'Corvinal'])

acess = school.access_secret_camera("Hermione")
print(acess)

#acess = school.access_secret_camera("Harry")
#print(acess)