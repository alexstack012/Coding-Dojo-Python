class pet:
    def __init__(self, name, animal_type="unknown", tricks="unknown"):
        self.name = name
        self.animal_type = animal_type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        self.sound = {
            'dog': 'bark',
            'cat': 'hiss',
            'toad': 'ribbet',
            'parrot': "want a cracker"
        }

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.energy += 5
        return self

    def noise(self):
        print(self.sound[self.animal_type])
        return self


class serviceAnimals(pet):
    jobTypes = {
        'calm': 'calms',
        'guide': 'guides',
        'protect': 'protects',
        'warn': 'warns'
    }

    def job(self, job):
        print(self.name, self.jobTypes[job])
        return self
