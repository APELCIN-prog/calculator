class Vehicle:
    def __init__(self):
        super().__init__()

    def info(self):
        return "Это транспортное средство для перемещения людей или грузов."


class Car(Vehicle):
    def __init__(self, mark, car_type):
        super().__init__()
        self.mark = mark
        self.car_type = car_type

    def info(self):
        return f"Марка: {self.mark}\nТип кузова: {self.car_type}\nНа машине передвигаемся по дорогам!"


class Ship(Vehicle):
    def __init__(self, name, ship_type):
        super().__init__()
        self.name = name
        self.ship_type = ship_type

    def info(self):
        return f"Название: {self.name}\nТип корабля: {self.ship_type}\nНа корабле передвигаемся по воде!"


class Airplane(Vehicle):
    def __init__(self, model, airplane_type, company):
        super().__init__()
        self.model = model
        self.airplane_type = airplane_type
        self.company = company

    def info(self):
        return (f"Модель: {self.model}\nТип самолёта: {self.airplane_type}\n"
                f"Компания: {self.company}\nНа самолёте летают!")


car = Car(mark="Toyota", car_type="Седан")
ship = Ship(name="Победа", ship_type="Круизный лайнер")
airplane = Airplane(model="Boeing 737", airplane_type="Пассажирский", company="Аэрофлот")


print(car.info())
print("-" * 30)
print(ship.info())
print("-" * 30)
print(airplane.info())

