class Person():
    """create human"""

    def  __init__(self, name, age, height):
        """inizialisetion atribute human"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """do human"""
        description = self.name + " " + str(self.age) + " " + str(self.height) + " " + str(self.weight)
        print(description)

    def get_weight(self):
        """get weight"""
        print("weight human: " + str(self.weight))

    def update_weight(self, kg):
        """update weight"""
        self.weight = kg

class Warrior(Person):
    """create warrior"""

    def __init__(self, name, age, height):
        """iniz atribute"""
        super().__init__(name, age, height) #from person -> super class
        self.rage = 100
    
    def get_rage(self):
        """get rage"""
        print("rage warrior: " + str(self.rage))
    
    def description_person(self):
        """do warrior"""
        description = self.name + " age: " + str(self.age) + " range: " + str(self.rage)
        # print(description)
        return description




# warrior = Warrior("Wuldfrig", 43, 20)
# warrior.get_rage()
# warrior.update_weight(140)
# warrior.description_person()
# warrior.description_person()
# print("new person: " + warrior.description_person())


# man = Person("alex", 30, 180)
# man.description_person()
# man.update_weight(120)
# man.get_weight()