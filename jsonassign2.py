class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def jump(self):
        print(f"{self.name} is jumping!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def sleep(self):
        print(f"{self.name} is sleeping!")


# Create objects and implement the functionalities
dog1 = Dog("Max", 3, "Brown")
dog1.description()
dog1.get_info()
print()

dog2 = JackRussellTerrier("Buddy", 2, "White and Brown")
dog2.description()
dog2.get_info()
dog2.jump()
print()

dog3 = Bulldog("Rocky", 4, "Fawn")
dog3.description()
dog3.get_info()
dog3.sleep()
