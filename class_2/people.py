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
man = Person("alex", 30, 180)
# man.description_person()
man.update_weight(120)
man.get_weight()