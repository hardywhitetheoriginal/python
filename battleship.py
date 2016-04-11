from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def printBoard(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
printBoard(board)

def randomRow(board):
    return randint(0, len(board) - 1)

def randomCol(board):
    return randint(0, len(board[0]) - 1)

shipRow = randomRow(board)
shipCol = randomCol(board)

for turn in range(24):
    
    print "Turn", turn + 1
    
    guessRow = int(raw_input("Guess Row:")) - 1
    guessCol = int(raw_input("Guess Col:")) - 1

    if guessRow == shipRow and guessCol == shipCol:
        print "Congratulations! You sunk my battleship!"
	break
    else:
        if (guessRow not in range(5)) or (guessCol not in range(5)):
            print "Oops, that's not even in the ocean."
        elif(board[guessRow][guessCol] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guessRow][guessCol] = "X"
            printBoard(board)
