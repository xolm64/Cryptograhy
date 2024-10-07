

class Car:
    def __init__(self, model,year,color):
        self.model=model
        self.year=year
        self.color=color
    def renew(self):
        self.year = 2024

    def recolor_black(self):
        self.color = " black"

    def __str__(self):
        return f" класс по описанию машин  {self.model}"

class Bike(Car):
    def __init__(self, model, year, color):
        super().__init__(model, year, color)
    def __str__(self):
        return f" класс по описанию велосипедов  {self.model}"


car1 = Car('bmw', 2015, 'white')
car2 = Car ('opel', 1990, 'orange')
bike1 = Bike('trek', 2020, 'blue')
print(f' машина {car1.model}, год {car1.year}, цвет {car1.color}')
print(car1)
car1.renew()
print(f' новый год выпуска машины {car1.model} : {car1.year}')
car1.recolor_black()
print(f' новый цвет машины {car1.model} : {car1.color}')
print(bike1)
bike1.recolor_black()
print((f' новый цвет велосипеда {bike1.model} : {bike1.color}'))