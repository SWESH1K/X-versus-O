# Main Game

from game_mechanics import *

def main():
    print("Welcome to the X versus O game!!")
    printBoard()

    while not(isBoardfull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("You Lost the game!")
            break

        # Checking for the bot move:
        if not(isWinner(board, 'X')):
            move = botMove()
            if move == 0:
                print("Tie Game!!")
            else:
                insertLetter('O',move) # Chances for the error
                print('Computer places "O" in postion -> ',move)
                printBoard()
        else:
            print("Yeah! you won the game!!")
            break

    if isBoardfull(board):
        print("Tie Game!!")

if __name__ == '__main__':
    main()