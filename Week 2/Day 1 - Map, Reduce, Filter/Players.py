import random


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        
        
class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        #self.health = health
        #self.strength = strength
        
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage."
        elif self.health <= 0:
            return f"{self.name} has died in act of combat."
        
    def battle_cries(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)
        self.health = health
        self.strength = strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage."
        elif self.health <= 0:
            return "A Saxon has died in combat."
        

class War:
    
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    
    def add_viking(self, Viking):
        self.viking_army.append(Viking)
            
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)
       
    def viking_attack(self):
        rand_sax = random.choice(self.saxon_army)
        rand_vik = random.choice(self.viking_army).strength
        daño_recibido = rand_sax.receive_damage(rand_vik) 
        if rand_sax.health <= 0:
            self.saxon_army.remove(rand_sax)
        return (daño_recibido)
            
    def saxon_attack(self):
        rand_sax = random.choice(self.saxon_army).strength
        rand_vik = random.choice(self.viking_army)
        daño_recibido = rand_vik.receive_damage(rand_sax) 
        if rand_vik.health <= 0:
            self.viking_army.remove(rand_vik)
        return (daño_recibido) 
    
    def show_status(self):
        if (len(self.saxon_army) == 1) and (len(self.viking_army) == 1):
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."