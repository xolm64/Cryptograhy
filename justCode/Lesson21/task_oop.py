class kniga:
    def __init__(self, name, tema, author):
        self.name = name
        self.tema = tema
        self.author = author


class  gazeta(kniga):
    def __init__(self, redactor):
        super().__init__
        self.redactor = redactor


gazeta1 = gazeta(kniga("Vasy",'sdf','sdf'))

gazeta1.redactor = "sdf"

print(gazeta1.redactor)
print(gazeta1.author)