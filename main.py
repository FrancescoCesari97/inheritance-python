
#* Inheritance = Allows a class to inherit attributes and methods from another class
#* ###########   Helps with code reusability and extensibility
#* ###########   class Child(Parent)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

    
#     def eat(self):
#         print(f"{self.name} is eating")

    
#     def slepp(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("Woof")

# class Cat(Animal):
#     def speak(self):
#         print("Meow")

# class Mouse(Animal):
#     def speak(self):
#         print("Squik")

# dog = Dog("Scooby")
# cat = Cat("Garfild")
# mouse = Mouse("Mickey")

# print(dog.name)
# print(cat.name)

# dog.eat()


#* multiple inherance = inherit from more than one parent class C(A, B)


# class Prey:
#     def flee(self):
#         print("This animal is fleeing")

# class Predator:
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass


# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()


# fish.flee()
# fish.hunt()



#* multilevel inheritance = inherit from a parent which inherits from another parent C(B) <- B(A) <- A



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"this {self.name} is eating")



class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")



class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


fish.eat()
fish.hunt()