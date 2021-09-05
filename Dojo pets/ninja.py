class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(self.first_name, "has taken", self.pet.name, "for a walk")
        return self

    def feed(self):
        self.pet.eat()
        print(self.first_name, "has fed", self.pet.name, "with", self.pet_food)
        return self

    def bath(self):
        print(self.first_name, "gave", self.pet.name, "a much needed bath")
        self.pet.noise()
        return self
