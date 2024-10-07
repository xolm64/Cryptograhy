class Shkaf:

    def __init__(self):
        self.is_open = False

    def open_door(self):
        print("Открываем дверь...")
        self.is_open = True

    def close_door(self):
        print("Закрываем дверь...")
        self.is_open = False

    def get_candies(self):
        if self.is_open:
            print("ням-ням-ням")
        else:
            print("Дверь шкафчика закрыт :(")

    def __enter__(self):
        print("Зашли в контекстный менеджер...")
        self.open_door()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_door()
        print("Вышли из контекстного менеджера...")


with Shkaf() as s1:
    s1.get_candies()


