class Bat:
    def __init__(self, brand):
        self.brand = brand


class Cricketer:
    def __init__(self, name, bat):
        self.name = name
        self.bat = bat

    def show_bat(self):
        print(f"{self.name} uses {self.bat.brand} bat")


bat1 = Bat("MRF")
sakib = Cricketer("Sakib", bat1)

sakib.show_bat()
