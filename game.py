# Mechanics of the Game

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def isWinner(board, letter):
    for i in [1,4,7]:
        if board[i] == letter and board[i+1] == letter and board[i+2] == letter:
            return True
    for i in [1,2,3]:
        if board[i] == letter and board[i+3] == letter and board[i+6] == letter:
            return True
    if board[1] == letter and board[5] == letter and board[9] == letter:
            return True
    elif board[7] == letter and board[5] == letter and board[3] == letter:
            return True
    return False
def playerMove():
    run = True
    while run:
        move = input("Please enter the position the place the X: ")
        try:
            move = int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertLetter('X',move)
                else:
                    print("Sorry the entered place is already filled!")
            else:
                print("Please enter the number within the range!")
        except:
            print("Please only enter the number!")


def botMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0

    for letter in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:] # Creates a copy
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move
            
    cornersOpen = [i for i in possibleMoves if i in [1,3,7,9]]

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = [i for i in possibleMoves if i in [12,4,6,8]]

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move

def selectRandom(list):
    import random

    length = len(list)
    r = random.randint(0,length)
    return list[r]


def isBoardfull(board):
    if board.count(' ') > 1: return False
    else: return True

if __name__ == '__main__':
     print(board)