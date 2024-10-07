class Person:
    def __init__(self, my_name, my_age): #конструктор
        self.name = my_name
        self.age = my_age
    def __str__(self):
        return self.name

person1 = Person(my_name = "kairat", my_age = 24)
person2 = Person(my_name = "vova", my_age = 6)


print(person1.name)
print(person1.age)
print(person1)