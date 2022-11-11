# Задача 1. Машина

import random


class Toyota():
    name = 'car'
    color = 'red'
    cost = 1_000_000
    max_speed = 200
    current_speed = 0


names = ("Selica", "Rav 4", "LandCruiser")

car1 = Toyota()
car2 = Toyota()
car3 = Toyota()

cars = (car1, car2, car3)


for car in cars:
    car.name = random.choice(names)
    car.current_speed = random.randint(0, 201)

for car in cars:
    print(f'Машина {car.name} скорость сейчас = {car.current_speed} км/ч.')
