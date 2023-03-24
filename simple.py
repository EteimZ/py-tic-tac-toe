from os import system

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# program entry point
def main():
    system('clear')
    displ(board)

    turn = "X"

    while True:
        player = input("Please play: ")

        if player not in board:
            system('clear')
            print("Wrong value")
            displ(board)
        
        elif board[int(player) - 1] != "X" and board[int(player) - 1] != "O":
            system('clear')
            board[int(player) - 1] = turn
            displ(board)
            checkWinner(board, turn)
            turn = switch_p(turn)
            fullBoard(board)
        

# display board
def displ(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"{board[6]}|{board[7]}|{board[8]}")

# switch player
def switch_p(turn):
    if turn == "X":
        return "O"
    else:
        return "X"

# define function to check if board is full
def fullBoard(board):
    if len(set(board)) == 2:
        print("Game Drawed")
        exit()

# define function to check winner
def checkWinner(board, turn):

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

if __name__ == '__main__':
    main()
