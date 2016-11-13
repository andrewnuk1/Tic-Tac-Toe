# set up a list of the 1 to 9 points
points = [0,0,0,0,0,0,0,0,0] # takes value 0 for empty, 1 for "X" or 4 for "O"
marker = [1,2,3,4,5,6,7,8,9] # for the board, takes numbers for empty, or "X" or "O"
checkforwin = [0,0,0,0,0,0,0,0,0] # [row1, row2, row3, col1, col2, col3, diag1, diag2, diag3] 012 345 678 036 147 258 048 246
computerAITurn = 0 # setting computer player

# function to move
def move(x):
    if computerAITurn == x:
        computerAI()
    else:
        movedone= input("move!")

    # check move is valid
        if movedone > 0 and movedone < 10:
            if points[movedone-1]==0:
                points[movedone-1]=x
                print("Move completed, next player's turn")
                if points[movedone-1]==1:
                    marker[movedone-1]="X"
                elif points[movedone-1]==4:
                    marker[movedone-1]="O" 
            else:
                print("false move, try again")
                move(x)
        else:
            print("false move, try again")
            move(x)        

# function to add computer player
def computerAI():
    movemade = 0 # becomes 1 when move is made
    opponentTurn = 0 # will be either 1 or 4
    whoseTurn = computerAITurn # will be either 1 or 4 initially


    for checking in range(2): # check to see if can win and then check to prevent loss
        if movemade==0 and checking == 1:
            if computerAITurn==1:
                whoseTurn=4
            else:
                whoseTurn=1
        elif movemade==1: # break out of the loop if a move was mage in first loop
            break
        
        for check in range(3):
            checkforwin[check] = points[(3*check)] + points[(3*check)+1] + points[(3*check)+2]
            if checkforwin[check] == whoseTurn*2:
                if points[(3*check)]==0:
                    points[(3*check)] = computerAITurn
                    movedone = (3*check) +1
                elif points[(3*check)+1]==0:
                    points[(3*check)+1]= computerAITurn
                    movedone =(3*check)+1+1
                elif points[(3*check)+2]==0:
                    points[(3*check)+2] = computerAITurn
                    movedone =(3*check)+2+1
                movemade = 1
                break

            checkforwin[check+3] = points[check] + points[check+3] + points[check+6]
            if checkforwin[check+3]==whoseTurn*2:
                if points[check]==0:
                    points[check] = computerAITurn
                    movedone = check +1
                elif points[check+3]==0:
                    points[check+3]= computerAITurn
                    movedone =check+3+1
                elif points[check+6]==0:
                    points[check+6] = computerAITurn
                    movedone =check+6+1
                movemade = 1
                break

            checkforwin[check+6] = points[check] + points[4] + points[8-check]
            if checkforwin[check+6]==whoseTurn*2:
                if points[check]==0:
                    points[check] = computerAITurn
                    movedone = check +1
                elif points[4]==0:
                    points[4]= computerAITurn
                    movedone =4+1
                elif points[8-check]==0:
                    points[8-check] = computerAITurn
                    movedone =8-check + 1
                movemade = 1
                break
   

    # no win, no block => take the centre then corners then mid points
    # [4,0,2,6,8,1,3,5,7] = Centre / corners / mid points list
    if movemade == 0:
        orderOfTest=[4,0,2,6,8,1,3,5,7]
        for test in orderOfTest:
            if points[test]==0:
                points[test]=computerAITurn
                movedone=test+1
                break

    print("Move completed, next player's turn")
    if points[movedone-1]==1:
        marker[movedone-1]="X"
    elif points[movedone-1]==4:
        marker[movedone-1]="O"


# function to set up board
def setupboard():
    print("")
    print(" " + str(marker[0]) + " " + str(marker[1]) + " " + str(marker[2]))
    print(" " + str(marker[3]) + " " + str(marker[4]) + " " + str(marker[5]))
    print(" " + str(marker[6]) + " " + str(marker[7]) + " " + str(marker[8]))


# funtion to check for winning move
def checkwin():
    for check in range(3): #check row1, col1, diag1 etc
        checkforwin[check] = points[(3*check)] + points[(3*check)+1] + points[(3*check)+2]
        checkforwin[check+3] = points[check] + points[check+3] + points[check+6]
        checkforwin[check+6] = points[check] + points[4] + points[8-check]
    if 3 in checkforwin or 12 in checkforwin:
        print("the game is won!")
        exit()
    

# Play the game
setupboard()

whoGoFirst=input("Do you want to go number 1 or number 2")
if whoGoFirst==1:
    computerAITurn = 4
else:
    computerAITurn = 1

for totalmoves in range(9):
    move((points.count(0)%2)+4 - ((points.count(0)%2)*4))
    setupboard()
    checkwin()
print("draw")
exit()
