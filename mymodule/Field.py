"""
Клас Field Атрибути:
● ships — двохвимірний список кораблів, елементи якого посиланнями на об’єкти класу Ship;
 атрибут повинен бути приватним.
Методи:
● __init__() —  генерує двохвимірний список, елементами якого є посилання на об’єкти класу Ship.
 Порожні клітинки можна представити об’єкт класу Ship з особливими параметрами або як None.

Для генерації поля ви можете використати раніше реалізовані функції.

● shoot_at(tuple) — виконує операцію, яка означає, що суперник влучив у клітинку ігрового поля Field;.

● field_without_ships() — повертає стрічку, що зображає лише ті клітинки ігрового поля, у які стріляв суперник;
● field_with_ships() — повертає стрічку, що зображає поле з кораблями, а також усі клітинки у які стріляв суперник


"""
from ship import Ship
from game_funcs import convert_ltr_coord, is_valid, ship_size

class Field(object):
    def __init__(self):
        def generate_field():
            """
            (None) -> (data)
            This function randomly generates a field with the ships for Battleship game.
            """
            import random

            ships = []

            def gen_angle():
                """
                (None) -> (str)
                This function randomly generates a ship angle situation - vertical - in this case function returns "v"
                or horizontal - in this case function returns "h"
                """
                if random.choice((0, 1)) == 0:
                    return "h"  # horizontal
                return "v"  # vertical

            def situate_ship(ship_size, free_cells, field):
                """
                (int), (list), (list) -> (list), (list)
                This function takes a ship size, list of cells available for situation, a field itself and randomly generates
                a ship position and writes it to the field.
                Function returns modified list of available cells and a modified field.
                """
                angle = gen_angle()
                if angle == "v":
                    free_cells = list(filter(lambda item: item[0] < 11 - ship_size, free_cells))
                else:
                    free_cells = list(filter(lambda item: item[1] < 11 - ship_size, free_cells))
                if not free_cells:
                    return free_cells, field
                random_coord = random.choice(free_cells)
                if angle == "v":
                    for c1 in [-1, 0, 1]:
                        for c2 in range(-1, ship_size + 1):
                            try:
                                free_cells.remove((random_coord[0] + c2, random_coord[1] + c1))
                            except:
                                pass
                    for i in range(ship_size):
                        field[random_coord[0] + i][random_coord[1]] = "*"

                if angle == "h":
                    for c1 in [-1, 0, 1]:
                        for c2 in range(-1, ship_size + 1):
                            try:
                                free_cells.remove((random_coord[0] + c1, random_coord[1] + c2))
                            except:
                                pass
                    for i in range(ship_size):
                        field[random_coord[0]][random_coord[1] + i] = "*"
                return [free_cells, field, random_coord, angle]

            while True:
                availible_cells = [(i, j) for j in range(10) for i in range(10)]
                field = [[" " for j in range(10)] for i in range(10)]
                oo_field = [[Ship((r, c), True, 0) for c in range(10)] for r in range(10)]
                for num in range(1, 5):
                    if num == 1:
                        after_ship = situate_ship(1, availible_cells, field)
                        oo_field[after_ship[2][0]][after_ship[2][1]] = Ship(after_ship[2],
                                                                            True if after_ship[3][0] == "h" else False,
                                                                            num)

                    for times in range(5 - num):
                        after_ship = situate_ship(num, availible_cells, field)
                        availible_cells, field = after_ship[0], after_ship[1]
                        oo_field[after_ship[2][0]][after_ship[2][1]] = Ship(after_ship[2],
                                                                            True if after_ship[3] == "h" else False,
                                                                            5-num)

                if is_valid(field):
                    return field, oo_field

        self.ships = generate_field()[1]

    def shoot_at(self, coord):
        self.ships[coord].shoot_at()
        pass

    def field_without_ships(self):
        pass

    def field_with_ships(self):
        pass

"""
● shoot_at(tuple) — виконує операцію, яка означає, що суперник влучив у клітинку ігрового поля Field;.

● field_without_ships() — повертає стрічку, що зображає лише ті клітинки ігрового поля, у які стріляв суперник;
● field_with_ships() — повертає стрічку, що зображає поле з кораблями, а також усі клітинки у які стріляв суперник
"""

my_fld = Field()
print(my_fld.ships)
