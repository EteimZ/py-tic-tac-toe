from tictactoe import TicTacToe
import sys
import os

# define os independent clear function
def clear():
 
    # for windows
    if os.name == 'nt':
        os.system('cls')
 
    # for posix os(linux and mac)
    else:
        os.system('clear')

def main():
    game = TicTacToe()
    
    clear()
    game.displ()

    while True:
        inp = int(input("Please select a number: "))

        clear()
        
        update = game.update_pos(inp - 1)
        game.displ()
        if game.checkWinner():
            sys.exit(f"Play {game.player} wins")
        if game.fullBoard():
            sys.exit("Game drawn")
        if update:
            game.switch()

if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit('Exiting game.')
