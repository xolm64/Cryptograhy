

class Table:

    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, other):
        len_sum = self.x+ other.x
        new_table= Table(self.x+ other.x, self.y , self.x )
        return new_table
    def __gt__(self, other):
        return self.x > other.x   # возвращает Тру или Фолс . мето сравнения обьектов класса


    def __str__(self):
        return f"Длина {self.x} ширина {self.y} высота {self.z}"


table1 = Table(15,10,30)
table2 = Table(15,10,30)

table = table1 + table2

print(table)