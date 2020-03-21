import random
from board import board
from tug import tug
from sub import sub
from battleship import battleship
from aircraft_carrier import aircraft_carrier

#function to add a point to the array
def addPoint(pointX, pointY, alrGuessed):
    alrGuessed[0].append(pointX)
    alrGuessed[1].append(pointY)

#function to check a given point
def checkPoint(pointX, pointY, gameBoard):
    hit = "X"
    miss = "O"
    if (gameBoard.display[pointY][pointX] == "T")  or (gameBoard.display[pointY][pointX] == "S") or (gameBoard.display[pointY][pointX] == "B") or (gameBoard.display[pointY][pointX] == "A"):
        gameBoard.display[pointY][pointX] = hit
        board.printBoard(gameBoard)
    elif (gameBoard.display[pointY][pointX] == ("-")):
        gameBoard.display[pointY][pointX] = miss
        board.printBoard(gameBoard)

#function to guess random points, returns point relative to the array (that starts counting at 0)
def randomGuess(num):
    #inclusive of 0 and exclusive of 1
    return int(random.random()*(num-1) + 0.5)

#function to check if a point has already been guessed
def checkGuess(randomX, randomY, alrGuessed):
    length = len(alrGuessed[0])
    for i in range(length):
        if (alrGuessed[0][i] == randomX) and (alrGuessed[1][i] == randomY):
            return 0
    return 1

#function to check points in a given direction
def checkInDirection(stratX, stratY, alrGuessed, columns, rows, direction):
    maxX = columns-1
    maxY = rows-1
    if (direction == 0) and (stratX-1 >= 0) and (checkGuess(stratX-1, stratY, alrGuessed) == 1):
        return [stratX-1, stratY, 0]
    elif (direction == 1) and (stratY-1 >= 0) and (checkGuess(stratX, stratY-1, alrGuessed) == 1):
        return [stratX, stratY-1, 1]
    elif (direction == 2) and (stratX+1 <= maxX) and (checkGuess(stratX+1, stratY, alrGuessed) == 1):
        return [stratX+1, stratY, 2]
    elif (direction == 3) and (stratY+1 <= maxY) and (checkGuess(stratX, stratY+1, alrGuessed) == 1):
        return [stratX, stratY+1, 3]
    return [-1,-1,-1]

#function to strategically check around a given point
def stratGuess(randomX, randomY, alrGuessed, columns, rows):
    maxX = columns-1
    maxY = rows-1
    direction = 0
    while (direction != 4):
        #uses direction and then verifies it is on the board and has not been guessed before
        if (direction == 0) and (randomX-1 >= 0) and (checkGuess(randomX-1, randomY, alrGuessed) == 1):
            return [randomX-1, randomY, 0]
        elif (direction == 1) and (randomY-1 >= 0) and (checkGuess(randomX, randomY-1, alrGuessed) == 1):
            return [randomX, randomY-1, 1]
        elif (direction == 2) and (randomX+1 <= maxX) and (checkGuess(randomX+1, randomY, alrGuessed) == 1):
            return [randomX+1, randomY, 2]
        elif (direction == 3) and (randomY+1 <= maxY) and (checkGuess(randomX, randomY+1, alrGuessed) == 1):
            return [randomX, randomY+1, 3]
        direction += 1
    return [-1,-1,-1]

#creating ships - possibility of user input but left at one of each for now
tug = tug()
sub = sub()
battleship = battleship()
aircraft_carrier = aircraft_carrier()
numShips = 4

#creating game board using user input
rows = int(input("How many rows would you like the board to have? (under 10) "))
columns = int(input("How many columns would you like the board to have? (under 10) "))
gameBoard = board(rows, columns)
print("This is the initial board: (x is horizontal, y is vertical)")
board.printBoard(gameBoard)

#generating locations of ships using user input (creates array as output)
locations = [[], []]

#uses for loop for efficiency
for num in range(numShips):
    if num == 0:
        typeShip = "tug"
    if num == 1:
        typeShip = "sub"
    if num == 2:
        typeShip = "battleship"
    if num == 3:
        typeShip = "aircraft carrier"
    print("For", typeShip, ": (which requires", str(num+2), "units horizontally or vertically between start and end coordinates)")
    start = input("What start coordinates would you like this to be placed at? (in (x,y) format, no negatives) ")
    #adds start coordinates to the locations array
    locations[0].append(int(start[1])-1)
    locations[1].append(int(start[3])-1)
    end = input("What end coordinates would you like this to be placed at? (in (x,y) format, no negatives) ")
    #adds end coordinates to the locations array
    locations[0].append(int(end[1])-1)
    locations[1].append(int(end[3])-1)

    #updates and prints board after each ship's coordinates have been entered
    if num == 0:
        tug.updateBoard(gameBoard, locations)
        board.printBoard(gameBoard)
    if num == 1:
        sub.updateBoard(gameBoard, locations)
        board.printBoard(gameBoard)
    if num == 2:
        battleship.updateBoard(gameBoard, locations)
        board.printBoard(gameBoard)
    if num == 3:
        aircraft_carrier.updateBoard(gameBoard, locations)
        board.printBoard(gameBoard)

#initailized variables for algorithm
miss = "O"
hit = "X"
winCondition = 0
isGuessed = 0
alrGuessed = [[-2], [-2]]
randomX = randomGuess(columns)
randomY = randomGuess(rows)

#algorithm - loops until all ships have been sunk, determined by win condition
while (winCondition == 0):    
    #generates random points until a new one is created
    isGuessed = checkGuess(randomX, randomY, alrGuessed)
    while (isGuessed == 0):
        randomX = randomGuess(columns)
        randomY = randomGuess(rows)
        isGuessed = checkGuess(randomX, randomY, alrGuessed)
    
    #adds point to those already guessed
    addPoint(randomX, randomY, alrGuessed)
    
    #determines if there is a hit or a miss
    checkPoint(randomX, randomY, gameBoard)

    #launches algorithm if the random point was a hit (one hit down) - doesn't end until the entire ship is sunk
    if (gameBoard.display[randomY][randomX] == hit):
        #checks to see if all ships have been sunk
        winCondition = board.checkBoard(gameBoard)
        if (winCondition == 1):
            break
        
        #resets stratHit condition after it has been changed to True
        stratHit = False

        #guesses around the point until a hit is found
        while (stratHit == False):
            #stratGuess function accounts for the already guessed point list
            stratPoint = stratGuess(randomX, randomY, alrGuessed, columns, rows)
            stratX = stratPoint[0]
            stratY = stratPoint[1]
            checkPoint(stratX, stratY, gameBoard)
            addPoint(stratX, stratY, alrGuessed)
            if (gameBoard.display[stratY][stratX] == hit):
                stratHit = True
                #attempts to create a line for hitting ships (two hits already)
                directionPoint = checkInDirection(stratX, stratY, alrGuessed, columns, rows, stratPoint[2])
                directionX = directionPoint[0]
                directionY = directionPoint[1]
                #checks to see if all ships have been sunk
                winCondition = board.checkBoard(gameBoard)
                if (winCondition == 1):
                    break
                checkPoint(directionX, directionY, gameBoard)
                addPoint(directionX, directionY, alrGuessed)
                if (gameBoard.display[directionY][directionX] == hit):
                    #continues in the same direction (three hits already)
                    secondDirectionPoint = checkInDirection(directionX, directionY, alrGuessed, columns, rows, directionPoint[2])
                    secondDX = secondDirectionPoint[0]
                    secondDY = secondDirectionPoint[1]
                    if (secondDX >= 0) and (secondDY >= 0):
                        checkPoint(secondDX, secondDY, gameBoard)
                        addPoint(secondDX, secondDY, alrGuessed)
                        if (gameBoard.display[secondDY][secondDX] == hit):
                            #continues in the same direction (four hits already)
                            thirdDirectionPoint = checkInDirection(secondDX, secondDY, alrGuessed, columns, rows, secondDirectionPoint[2])
                            thirdDX = thirdDirectionPoint[0]
                            thirdDY = thirdDirectionPoint[1]
                            if (thirdDX >= 0) and (thirdDY >= 0):
                                #continues in same direction - could be five hits or four hits (if a miss)
                                checkPoint(thirdDX, thirdDY, gameBoard)
                                addPoint(thirdDX, thirdDY, alrGuessed)
                                #accounts for both a miss or being out of bounds to check the other direction
                                if (gameBoard.display[thirdDY][thirdDX] == miss or (thirdDX[1] == -1)):
                                    #checks in the other direction (four hits already)
                                    fourthDirectionPoint = checkInDirection(randomX, randomY, alrGuessed, columns, rows, (secondDirectionPoint[2]+2)%4)
                                    fourthDX = fourthDirectionPoint[0]
                                    fourthDY = fourthDirectionPoint[1]
                                    if (fourthDX >= 0) and (fourthDY >= 0):
                                        #put in final guess (five hits which is the max)
                                        checkPoint(fourthDX, fourthDY, gameBoard)
                                        addPoint(fourthDX, fourthDY, alrGuessed)
                        #accounts for both a miss or being out of bounds to check the other direction
                        elif (gameBoard.display[secondDY][secondDX] == miss or (secondDX[1] == -1)):
                            #checks in the other direction (three hits already)
                            thirdDirectionPoint = checkInDirection(randomX, randomY, alrGuessed, columns, rows, (directionPoint[2]+2)%4)
                            thirdDX = thirdDirectionPoint[0]
                            thirdDY = thirdDirectionPoint[1]
                            if (thirdDX >= 0) and (thirdDY >= 0):
                                checkPoint(thirdDX, thirdDY, gameBoard)
                                addPoint(thirdDX, thirdDY, alrGuessed)
                                if (gameBoard.display[thirdDY][thirdDX] == hit):
                                    #continues in the same direction (four hits already)
                                    fourthDirectionPoint = checkInDirection(thirdDX, thirdDY, alrGuessed, columns, rows, thirdDirectionPoint[2])
                                    fourthDX = fourthDirectionPoint[0]
                                    fourthDY = fourthDirectionPoint[1]
                                    if (fourthDX >= 0) and (fourthDY >= 0):
                                        #put in final guess (five hits which is the max)
                                        checkPoint(fourthDX, fourthDY, gameBoard)
                                        addPoint(fourthDX, fourthDY, alrGuessed)
                #accounts for both a miss or being out of bounds to check the other direction
                elif ((gameBoard.display[directionY][directionX] == miss) or (directionPoint[1] == -1)):
                    #checks in the other direction (two hits already)
                    secondDirectionPoint = checkInDirection(randomX, randomY, alrGuessed, columns, rows, (stratPoint[2]+2)%4)
                    secondDX = secondDirectionPoint[0]
                    secondDY = secondDirectionPoint[1]
                    if (secondDX >= 0) and (secondDY >= 0):
                        #checks to see if all ships have been sunk
                        checkPoint(secondDX, secondDY, gameBoard)
                        addPoint(secondDX, secondDY, alrGuessed)
                        #doesn't need to check in the other direction as if it is a miss then the point would be on its own
                        if (gameBoard.display[secondDY][secondDX] == hit):
                            #continues in the same direction (three hits already)
                            thirdDirectionPoint = checkInDirection(secondDX, secondDY, alrGuessed, columns, rows, secondDirectionPoint[2])
                            thirdDX = thirdDirectionPoint[0]
                            thirdDY = thirdDirectionPoint[1]
                            if (thirdDX >= 0) and (thirdDY >= 0):
                                #checks to see if all ships have been sunk
                                checkPoint(thirdDX, thirdDY, gameBoard)
                                addPoint(thirdDX, thirdDY, alrGuessed)
                                if (gameBoard.display[thirdDY][thirdDX] == hit):
                                    #continues in the same direction (four hits already)
                                    fourthDirectionPoint = checkInDirection(thirdDX, thirdDY, alrGuessed, columns, rows, secondDirectionPoint[2])
                                    fourthDX = fourthDirectionPoint[0]
                                    fourthDY = fourthDirectionPoint[1]
                                    if (fourthDX >= 0) and (fourthDY >= 0):
                                        #checks to see if all ships have been sunk
                                        #put in final guess (five hits which is the max)
                                        checkPoint(fourthDX, fourthDY, gameBoard)
                                        addPoint(fourthDX, fourthDY, alrGuessed)
        
        #checks to see if all ships have been sunk
        winCondition = board.checkBoard(gameBoard)

#informs user that win condition has been met
board.printBoard(gameBoard)
print("The computer has now beaten the game and sunk all of the ships you placed.")
