# File: player.py


from field import Field

class Player(object):
    def __init__(self, name):
        """
        This method initializes a new Player instance.
        """
        self.__name = name

    def read_position(self):
        """
        This method asks Player for the coord to shoot at, reads it from input
        and returns it as a tuple
        """
        print(self.__name + " it's your turn to shoot!")
        print("Type the coord i - from A to J, j - from 1 to 10:")
        i, j = input().split()
        return i, int(j)
