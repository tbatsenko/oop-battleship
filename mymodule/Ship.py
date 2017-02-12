"""
Клас Ship Атрибути:
● bow ​— ​tuple з координатами типу int, що означають розміщення лівого верхнього кута кораблю (корми);
● horizontal — змінна типу bool, що означає напрямок розміщення напрямку; 
● length — розмір корабля, наприклад лінкор має розмір (1, 4); атрибут повинен бути приватним; 
● hit ​—​ список bool, що відповідає тому чи суперник влучив у відповідну частину корабля; атрибут має бути приватним

 Методи:
● __init__(length) — у ініціалізаторі атрибуту length повинно присвоюватися передане значення, а також повинні
створюватися атрибути із значеннями за замовчування; 
● shoot_at(tuple) — виконує операцію, яка відображає те,
 що у класі Ship суперник влучив у частину відповідну частину корабля.
"""
class Ship(object):
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length  # just int value
        self.__hit = [False for i in range(length)]

    def shoot_at(self, coord):
        if self.horizontal:
            ship_cells = [(self.bow[0], self.bow[1] + i) for i in range(self.__length)]
            try:
                ship_part_coord = ship_cells.index(coord)
                
                return True, self
            except ValueError:
                return False, coord
                