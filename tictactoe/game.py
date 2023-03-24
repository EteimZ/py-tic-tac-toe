from enum import Enum, auto
from typing import Literal


class Player(Enum):
    X = auto()
    O = auto()


class TicTacToe:

    def __init__(self):
        self._player: Player = Player.X
        self._board: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    @property
    def player(self):
        return self._player.name

    @player.setter
    def player(self, player: Literal['X', 'O']):
        if player == 'X':
            self._player = Player.X
        elif player == 'O':
            self._player = Player.O

    @property
    def board(self):
        return self._board

    def displ(self):
        print(f"{self._board[0]}|{self._board[1]}|{self._board[2]}")
        print(f"{self._board[3]}|{self._board[4]}|{self._board[5]}")
        print(f"{self._board[6]}|{self._board[7]}|{self._board[8]}")

    def switch(self):
        if self._player == Player.X:
            self._player = Player.O
        else:
            self._player = Player.X

    def fullBoard(self):
        if len(set(self._board)) == 2:
            return True

    def checkWinner(self):
        
        board = self._board
        turn = "X" if self._player == Player.X else "O"

        # horizontal wins
        if board[0] == board[1] == board[2] == turn or board[3] == board[4] == board[5] == turn or board[6] == board[7] == board[8] == turn:
            return True

        # vertical wins
        if board[0] == board[3] == board[6] == turn or board[1] == board[4] == board[7] == turn or board[2] == board[5] == board[8] == turn:
            return True

        # diagonal wins
        if board[0] == board[4] == board[8] == turn or board[2] == board[4] == board[6] == turn:
            return True
    
    def update_pos(self, pos: int):
        if pos not in list(range(9)):
            return False
            
        if self._board[pos] != "X" and self._board[pos] != "O":
            self._board[pos] = self._player.name
            return True
        
        return False
