# File: play.py
# This module launch a console Battleship game


from game import Game

print("Welcome to the Battleship Game!\n Let's start!")
game = Game()
while True:
    print("There is your field: ")
    print(game.field_with_ships())
    print("\n This is your rival's field: ")
    print(game.field_without_ships())
    game.read_position()
