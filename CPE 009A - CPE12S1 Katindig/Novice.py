from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
    
#username = input("Your Username: ")
#character1 = Character(username)
#print("Your username is", character1.getUsername())
#print("Hp: ",character1.getHp())