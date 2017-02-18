"""
Клас Game Атрибути:
● field — список ігрових полів (об’єкти класу Field); атрибут повинен бути приватним; 
● players — список гравців (об’єкти класу Player); атрибут повинен бути приватним; 
● current_player — індекс поточного гравця; атрибут повинен бути приватним. 

Методи: 
● __init__() — ініціалізує нову гру, список гравців, список полів та індекс початкового гравця; 

● read_position() — зчитує координати пострілу гравця і конвертує їх у потрібний тип. 

● field_without_ships(index) — повертає стрічку, що зображає лише ті клітинки
ігрового поля Field з індексом index, у які стріляв суперник; 

● field_with_ships() — повертає стрічку, що зображає ігрове поле Field
 з індексом index з кораблями, а також усі клітинки у які стріляв суперник. 
"""
# File: field.py


from field import Field
from player import Player


class Game(object):
    def __init__(self):
        """
        This method initializes a new instance of Game class.
        field: (list[Field, Field]) - list of Fields for the game
        players: (list[Player, Player]) - list of Players for the game
        """
        field1, field2 = Field(), Field()
        self.__fields = [field1, field2]
        print("Player 1, please enter your name:")
        name1 = input()
        print("Player 2, please enter your name:")
        name2 = input()
        self.__players = [Player(name1), Player(name2)]
        self.__current_player = 1

    def read_position(self):
        """
        This method asks current player for the coord to shoot at and
        modifies a field properly.
        :return: None
        """
        if self.__current_player == 1:
            coord = self.__players[0].read_position()
            self.__fields[1].shoot_at(coord)
            self.__current_player = 2
        else:
            coord = self.__players[1].read_position()
            self.__fields[0].shoot_at(coord)
            self.__current_player = 1

    def field_without_ships(self):
        """
        This method calls rival's field method to display a field in str
        """
        if self.__current_player == 1:
            return self.__fields[1].field_without_ships()
        return self.__fields[0].field_without_ships()

    def field_with_ships(self):
        """
        This method calls current player field method to display a field in str
        """
        if self.__current_player == 1:
            return self.__fields[0].field_with_ships()
        return self.__fields[1].field_with_ships()
