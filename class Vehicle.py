class Vehicle:
    def __init__(self, brand, year, display_info):
        self.brand = brand
        self.year = year
        self.display_info = display_info


class Car(Vehicle):
    def __init__(self, brand, year, display_info):
        super().__init__(brand, year, display_info)




class Motorcycle(Vehicle):
    def __init__(self, brand, year, display_info):
        super().__init__(brand, year, display_info)