# 11.2 Классы
# Задача 2. Однотипные объекты

class Monitor():
    name = 'Samsung'
    matrix = 'VA'
    resolution = 'WQHD'
    frequency = 0


class Headphones():
    name = 'Sony'
    sensitivity = 108
    micro = True


monitors = [Monitor() for i in range(4)]
headphones = [Headphones() for k in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].micro = False
