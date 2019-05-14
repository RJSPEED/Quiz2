
class Animal:
    def __init__(self, name):
        self.name = name
        self.species = None
    
    def make_noise(self):
        print("")
        
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "tiger"

    def make_noise(self):
        print("Roar!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "dog"

    def make_noise(self):
        print("Bark!")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "cow"

    def make_noise(self):
        print("Moo!")

class Zoo:
    def __init__(self):
        self.animals =[]
    
    def add(self, animal):
        #self.animals.append(animal)
        if isinstance(animal, Animal) == False:
            return "Animal not in Animal Class" 
        else:
            self.animals.append(animal)
            return self.animals
    
    def show_animals(self):
        for animals in self.animals:
            #print animal name / species
            print()
            #call make noise method






my_zoo = Zoo()
print(my_zoo.add("Monkey"))

"""
#mike = Animal("Mike")
#print(mike.species)
#print(mike.name)
#mike.make_noise()

tony = Tiger("Tony")
print(tony.species)
tony.make_noise()

brutus = Dog("Brutus")
print(brutus.species)
brutus.make_noise()

colin = Cow("Colin")
print(colin.species)
colin.make_noise()

"""
