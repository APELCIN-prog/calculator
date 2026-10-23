import random


class SpaceShip:
    def __init__(self, fuel=100, hull=100):
        self.fuel = fuel
        self.hull = hull


class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = 100


class Mission:
    def __init__(self, target):
        self.target = target
        self.distance = 0

    def play(self, ship, crew):
        print(f"Старт миссии: {self.target}\n")

        while self.distance < 100 and ship.fuel > 0 and ship.hull > 0:
            self.distance += 25
            ship.fuel -= random.randint(15, 25)

            event = random.choice(["asteroid", "breakdown", "safe"])
            if event == "asteroid":
                ship.hull -= 30
                crew.health -= 20
                print(
                    f"Ход: прошли {self.distance}%. Попали в астероиды! Корпус: {ship.hull}%, Жизнь пилота: {crew.health}%")
            elif event == "breakdown":
                ship.hull -= 15
                print(f"Ход: прошли {self.distance}%. Поломка! Корпус: {ship.hull}%")
            else:
                print(f"Ход: прошли {self.distance}%. Полет нормальный. Топливо: {ship.fuel}%")

        print("\n=== ИТОГ ===")
        if self.distance >= 100 and ship.hull > 0:
            print(f"Ура! Мы успешно долетели до: {self.target}!")
        else:
            print("Миссия провалена! Корабль уничтожен или закончилось топливо.")


ship = SpaceShip()
pilot = CrewMember("Джон", "Пилот")
mission = Mission("Марс")

mission.play(ship, pilot)
