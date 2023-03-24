from enum import Enum, auto
from os import system

class Player(str, Enum):
    X = 'X'
    O = 'O'


class TicTacToe:

    def __init__(self):
        self.player: Player = Player.X
        self.board: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def displ(self):
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")

    def switch(self):
        if self.player == Player.X:
            self.player = Player.O
        else:
            self.player = Player.X

    def fullBoard(self):
        if len(set(self.board)) == 2:
            print("Game Drawed")
            exit()

    def checkWinner(self):
        
        board = self.board
        turn = "X" if self.player == Player.X else "O"

        # horizontal wins
        if board[0] == board[1] == board[2] == turn or board[3] == board[4] == board[5] == turn or board[6] == board[7] == board[8] == turn:
            print(f'{turn} is the winner')
            exit()

        # vertical wins
        if board[0] == board[3] == board[6] == turn or board[1] == board[4] == board[7] == turn or board[2] == board[5] == board[8] == turn:
            print(f'{turn} is the winner')
            exit()

        # diagonal wins
        if board[0] == board[4] == board[8] == turn or board[2] == board[4] == board[6] == turn:
            print(f'{turn} is the winner')
            exit()

    def play(self):
        system('clear')
        self.displ()


        while True:
            player = input("Please play: ")

            if player not in self.board:
                system('clear')
                print("Wrong value")
                self.displ()
        
            elif self.board[int(player) - 1] != "X" and self.board[int(player) - 1] != "O":
                system('clear')
                self.board[int(player) - 1] = self.player.name
                self.displ()
                self.checkWinner()
                self.switch()
                self.fullBoard()

game = TicTacToe()
game.play()
