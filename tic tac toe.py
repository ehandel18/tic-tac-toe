import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if board[inp - 1] == "-" and inp >=1 and inp <= 9:
        board[inp - 1] = currentPlayer
    else:
        print("not a valid move")    

def horizontalcheck(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[7]
        return True
    return False
    
def verticalcheck(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True   
    return False

def diaganolcheck(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def tieCheck(board):
    global gameRunning
    if "-" not in board[:8]:
        print(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if horizontalcheck(board) or verticalcheck(board) or diaganolcheck(board):
        print(f"The winner is {winner}")
        gameRunning = False 
        

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gameRunning == True:
    printBoard(board)
    playerInput(board)
    checkWin()
    tieCheck(board)
    switchPlayer()
    computer(board)
    checkWin()
    tieCheck(board)
