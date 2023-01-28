class Person():
    """human model"""

    def __init__(self, name, age):#self to go class
        """inicialisaition human atribut - name, age"""
        self.name = name
        self.age = age
        print("human created")

    def sing(self):
        """human sing"""
        print(self.name + " sing pip")
    
    def dence(self):
        """human sing"""
        print(self.name + " dance pip")

man = Person("Alex", 20)
woman = Person("Nasty", 22)

man.dence()
man.sing()