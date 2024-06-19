
board = [' '  for x in range(10)]  

def insertletter(letter, pos):
    board[pos] = letter

def spaceisFree(pos):
    return board[pos]== ' '



def printBoard(board):
    # print('  |  |')
    print(' '+board[1]+ '|' +  board[2]+ "|" + board[3])
    # print('  | |')
    print("-------")
    # print('  |  |')
    print(' '+board[4]+ '|' +  board[5]+ "|" + board[6])
    # print('  | |')
    print("-------")
    # print('  |  |')
    print(' '+board[7]+ '|' +  board[8]+ "|" + board[9])



def isWinner(board,le):
    hori = (board[7] == le and board[8] == le and board[9] == le ) or ( board[4] == le and board[5] == le and board[6]==le) or (board[1] == le and board[2] == le and board[3]==le) 
    verti = (board[1] == le and board[4] == le and board[7] == le ) or ( board[2] == le and board[5] == le and board[8]==le) or (board[3] == le and board[6] == le and board[9]==le)
    diag =  (board[1] == le and board[5] == le and board[9] == le ) or ( board[3] == le and board[5] == le and board[7]==le)
    return hori or verti or diag;



def playerMove():
    run = True
    while run :
        move = input('Please select a position which is avilabele on screen')

        try:    
            move = int(move)
            if move>0 and move<10:
                if spaceisFree(move):
                    run=False
                    insertletter('X', move)
                else:
                    print("Space is occupied")
            else:
                print("Pls type a number that exists")
        except:
            print("Type a number")




def compMove():
    possiblemove = [x for x, letter in enumerate (board) if letter == ' ' and x!=0]
    move = 0
    for let in ['O','X']:
        for i in possiblemove:
            boardCopy = board[:]
            boardCopy[i]= let
            if isWinner(boardCopy,let):
                move = i
                return move
    opencorners = []
    for i in possiblemove:
        if i in[1,3,7,9]:
            opencorners.append(i)
    if len(opencorners)>0:
        move = selectRandom(opencorners)
        return move
    if 5 in possiblemove:
        move = 5
        return move
    edges = []
    for i in possiblemove:
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges)>0:
        return selectRandom(edges)
    
    return move


def selectRandom(li):
    import random

    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isboardfull(board):
    if board.count(' ')<1:
        return True
    else:
        return False


def main():
    print('Starting game')
    printBoard(board)

    while not (isboardfull(board)):
        if not isWinner(board,'O'):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, o won this time')
            break
        if not(isWinner(board,"X")):
            move =  compMove()  
            if move == 0:
                print('Tie Game')
            else:
                insertletter("O", move)
                print("Computer placed an O in position", move,':')
                printBoard(board)
        else:
            print('DAMN, U BEATED THE COMPUTER, HOW DOES IT FEEL LIKE BEING A CHAMP')
            break
    
    if isboardfull(board):
        print('TIE : GAME OVER')


def tictactoeGame():
    main()
    print("Game over")
    char =  input("Type Y to play again and N to exit:  ")
    while(char not in ["Y","N"]):
        print("Invalid input")
        char =  input("Type Y to play again and N to exit:  ")
    
    if char == "Y":

        tictactoeGame()
    else:
        print("BYE BYE")

def Game():
    main()
    print("Game over")
    char =  input("Type Y to play again and N to exit:  ")
    while(char not in ["Y","N"]):
        print("Invalid input")
        char =  input("Type Y to play again and N to exit:  ")
    while char=='Y':
        main()
        char =  input("Type Y to play again and N to exit:  ")
    print("Thank you for playing")


tictactoeGame()


