# File: field.py
from ship import Ship
from game_funcs import convert_ltr_coord, is_valid, ship_size, field_to_str


class Field(object):
    def __init__(self):
        """
        This method initialize a new Field class instance.
        """
        def generate_field():
            """
            (None) -> (data)
            This function randomly generates a field with the ships for
            Battleship game.
            """
            import random

            def gen_angle():
                """
                (None) -> (str)
                This function randomly generates a ship angle situation:
                vertical - in this case function returns "v"
                or horizontal - in this case function returns "h"
                """
                if random.choice((0, 1)) == 0:
                    return "h"  # horizontal
                return "v"  # vertical

            def situate_ship(ship_size, free_cells, func_field, func_oo_field):
                """
                (int), (list), (list) -> (list), (list)
                This function takes a ship size, list of cells available
                for situation, a field itself and randomly generates
                a ship position and writes it to the field.
                Function returns modified list of available cells and
                a modified field.
                """
                angle = gen_angle()
                if angle == "v":
                    free_cells = list(filter(
                        lambda item: item[0] < 11 - ship_size, free_cells))
                else:
                    free_cells = list(filter(
                        lambda item: item[1] < 11 - ship_size, free_cells))
                if not free_cells:
                    return free_cells, func_field, func_oo_field
                random_coord = random.choice(free_cells)
                if angle == "v":
                    for c1 in [-1, 0, 1]:
                        for c2 in range(-1, ship_size + 1):
                            try:
                                free_cells.remove((random_coord[0] + c2,
                                                   random_coord[1] + c1))
                            except:
                                pass
                    for i in range(ship_size):
                        func_field[random_coord[0] + i][random_coord[1]] = "*"
                        new_ship = Ship(random_coord, False, ship_size)
                        func_oo_field[random_coord[0]+i][random_coord[1]] = \
                            new_ship

                if angle == "h":
                    for c1 in [-1, 0, 1]:
                        for c2 in range(-1, ship_size + 1):
                            try:
                                free_cells.remove((random_coord[0] + c1,
                                                   random_coord[1] + c2))
                            except:
                                pass
                    for i in range(ship_size):
                        func_field[random_coord[0]][random_coord[1] + i] = "*"
                        n_ship = Ship(random_coord, True, ship_size)
                        func_oo_field[random_coord[0]][random_coord[1] + i] = \
                            n_ship
                return [free_cells, func_field, func_oo_field]

            while True:
                availible_cells = [(i, j) for j in range(10) for i in range(10)]
                field = [[" " for j in range(10)] for i in range(10)]
                oo_field = [[Ship((r, c), True, 0) for c in range(10)]
                            for r in range(10)]
                for num in range(1, 5):
                    if num == 1:
                        after_ship = situate_ship(1, availible_cells,
                                                  field, oo_field)
                        availible_cells, field, oo_field = after_ship[0],\
                                                           after_ship[1],\
                                                           after_ship[2]
                    for times in range(5 - num):
                        after_ship = situate_ship(num, availible_cells,
                                                  field, oo_field)
                        availible_cells, field, oo_field = \
                            after_ship[0], after_ship[1], after_ship[2]

                if is_valid(field):
                    return field, oo_field
        fields = generate_field()
        self.ships = fields[1]
        self.player_field = fields[0]
        self.damaged_cells = [[" " for j in range(10)] for i in range(10)]

    def shoot_at(self, coord):
        """
        (tuple) -> (None)
        This method reloads the field of rival after shooting.
        """
        valid_crd = (convert_ltr_coord(coord[0]), coord[1]-1)
        self.ships[valid_crd[0]][valid_crd[1]].shoot_at(valid_crd)
        self.damaged_cells[valid_crd[0]][valid_crd[1]] = "X"

    def field_without_ships(self):
        """
        (None) -> (str)
        This method returns a field of a rival of curr player with cells,
        which were shooten.
        """
        return field_to_str(self.damaged_cells)

    def field_with_ships(self):
        """
        (None) -> (str)
        This method returns a field of current player with ships in str
        """
        player_field = [["X" if self.damaged_cells[i][j] == "X"
                         else self.player_field[i][j]
                         for j in range(10)] for i in range(10)]
        return field_to_str(player_field)
