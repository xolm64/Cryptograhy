

class Animal:
    def __init__(self, name):
        self.name = name
    def say_sm(self):
        print("gaf")
    def __str__(self):
        return self.name


dog = Animal("boss")
dog.say_sm()
print(dog)