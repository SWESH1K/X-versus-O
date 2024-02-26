# Main Game

from game_mechanics import *
import random
import time

def playerTurn():
    if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
    else:
        print("You Lost the game!")
        quit()

def botTurn():
    # Checking for the bot move:
    if not(isWinner(board, 'X')):
        move = botMove()
        if move == 0:
            print("Tie Game!!")
        else:
            insertLetter('O',move) # Chances for the error
            print('Bot places "O" in postion -> ',move)
            printBoard()
    else:
        print("Yeah! you won the game!!")
        quit()

def main():
    print("Welcome to the X versus O game!!")
    turn = random.randint(0,1)

    if turn: printBoard()
    while not(isBoardfull(board)):
        if turn:
            playerTurn()
            print("The Bot is analysing...")
            time.sleep(2)
            if isBoardfull(board): break
            botTurn()
        else:
            botTurn()
            playerTurn()
            print("The Bot is analysing...")
            time.sleep(2)
            if isBoardfull(board): break

    if isBoardfull(board):
        print("Tie Game!!")

if __name__ == '__main__':
    main()