from Graphics import *
import numpy as np

beginGrfx(1300,700)

# layout of the game board
row = [0,0,0,0,0,0,0]
board = np.array([row,row,row,row,row,row,row])
print(board)

def background():
    setColor("black")
    fillRectangle(0,0,1300,700)
    
background()
# board pieces, rows and columns, score counters, number of games
global slots,rows,columnsredScore,yellowScore,tie,times
slots,rows,columns,redScore,yellowScore,tie,times = 42,6,7,0,0,0,int(numinput("Gametime","How many rounds do you want to play?")) 

# resets board after a game 
def erasePieces():
    setColor("Black")
    x=352
    y=155
    r=37.5
    for j in range(rows):
        for k in range(columns):
            fillCircle(x,y,r)
            x+=100
        x-=700
        y+=100

# draws game board
def Board():
    setColor('dark blue')
    fillRectangle(287.5,100,1012.5,700)
    erasePieces()
        
# draws supply pieces        
def supplyPieces():
    setColor('red')
    fillCircle(1102,155,37.5)
    setColor('yellow')
    fillCircle(1202,155,37.5)
    
# Erases the red supply piece
def eraseRedPiece():
    setColor("black")
    fillCircle(1102,155,37.5)
 
# Erases the yellow supply piece 
def eraseYellowPiece():
    setColor("black")
    fillCircle(1202,155,37.5)
    
# draws score counter    
def scoreCounter(redScore,yellowScore,b,d):
    a = 'Red: '+str(redScore)
    setColor(b)
    drawString(a,25,150,"Arial",48,'bold')
    c = 'Yellow: '+str(yellowScore)
    setColor(d)
    drawString(c,25,75,"Arial",48,'bold')
       
# updates score counter        
def tally(redScore,yellowScore):
    if checkRedWin(board) == True:
        scoreCounter(redScore,yellowScore,'black','yellow')
        scoreCounter(redScore+1,yellowScore,'red','yellow')
    elif checkYellowWin(board) == True:
        scoreCounter(redScore,yellowScore,'red','black')
        scoreCounter(redScore,yellowScore+1,'red','yellow')       

# Checks the board for all possible wins for the red pieces
def checkRedWin(board):
    tile = 1
    # Check horizontal space
    for y in range(rows):
        for x in range(columns):
            if all(board[y][x+k] == tile for k in range(4)):
                return True 
        
    # Check vertical spaces
    for x in range(columns):
        for y in range(rows):
            if all(board[y+k][x] == tile for k in range(4)):
                return True

    # check / diagonal spaces
    for x in range(3,columns):
        for y in range(rows-3):
            if all(board[y+k][x-k] == tile for k in range(4)):
                return True 

    # Check \ diagonal spaces
    for x in range(columns-3):
        for y in range(rows-3):
            if all(board[y+k][x+k] == tile for k in range(4)):
                return True
            
# Checks the board for all possible wins for the yellow pieces
def checkYellowWin(board):
    tile = 2
    # Horizontal
    for y in range(rows):
        for x in range(columns):
            if all(board[y][x+k] == tile for k in range(4)):
                return True

    # Vertical
    for x in range(columns):
        for y in range(rows):
            if all(board[y+k][x] == tile for k in range(4)):
                return True 
            
    # Positive Diagonal 
    for x in range(3,columns):
        for y in range(rows-3):
            if all(board[y+k][x-k] == tile for k in range(4)):
                return True
 
    # Negative Diagonal 
    for x in range(columns-3):
        for y in range(rows-3):
            if all(board[y+k][x+k] == tile for k in range(4)):
                return True
            
# Finds the corresponding row based on user input
def checkRow(x):
    if board[5][x] == 0:
        return 5
    elif board[4][x] == 0:
          return 4
    elif board[3][x] == 0:
          return 3
    elif board[2][x] == 0:
          return 2
    elif board[1][x] == 0:
          return 1
    elif board[0][x] == 0:
          return 0
        
# Sets all board pieces back to a value of 0
def reset():
    if (checkRedWin(board) or checkYellowWin(board)) == True:
        rowNum = 5
        colNum = 0
        for k in range(columns):
            for k in range(rows):
                if board[rowNum][colNum] == 1 or board[rowNum][colNum] == 2:
                    board[rowNum][colNum] = 0
                rowNum-=1
            rowNum+=6
            colNum+=1

# Simulates the game of Connect 4
def gameplay(redScore, yellowScore, tie):
    delay(200)
    starter = "red"  # red starts first game
    for game in range(times):
        game_over = False
        move = 0
        while move < slots and not game_over:
            # Turn order
            if starter == "red":
                Color = "red" if move % 2 == 0 else "yellow"
            else:
                Color = "yellow" if move % 2 == 0 else "red"

            supplyPieces()
            colNum = int(numinput(f"{Color.capitalize()}'s Turn","Type a column number 1-7")) - 1
            rowNum = checkRow(colNum)
            # Piece placement
            setColor(Color)
            x1 = 352 + (colNum * 100)
            y1 = 155 + (rowNum * 100)
            fillCircle(x1, y1, 37.5)
            if Color == "red":
                board[rowNum][colNum] = 1
                eraseRedPiece()
            else:
                board[rowNum][colNum] = 2
                eraseYellowPiece()
            delay(200)

            # Win check
            if checkRedWin(board):
                tally(redScore,yellowScore)
                redScore += 1
                starter = "red"
                game_over = True
            elif checkYellowWin(board):
                tally(redScore,yellowScore)
                yellowScore += 1
                starter = "yellow"
                game_over = True

            # Check draw 
            elif move == slots - 1:
                tie += 1
                game_over = True
            move += 1

        # Endgame
        if game < times - 1:
            erasePieces()
            reset()
        else:
            break

    # Final result
    if redScore > yellowScore:
        setColor("red")
        drawString("Grand Champion",410,90,"Arial",48,"bold")
    elif yellowScore > redScore:
        setColor("yellow")
        drawString("Grand Champion",410,90,"Arial",48,"bold")
    else:
        setColor("white")
        drawString("Draw",580,90,"Arial",48,"bold")

def execution():
    scoreCounter(redScore,yellowScore,'red','yellow')
    supplyPieces()
    Board()
    gameplay(redScore,yellowScore,tie)

execution()

endGrfx()