import pygame
import sys
import random
import math
from board import board
from colorSquare import colorSquare
pygame.init()

#function to generate the path across the screen
def randomPath(screenWidth, screenHeight):
    #determine what edge the starting point will be on
    ran1 = random.random()
    ran2 = random.random()
    if ran1 < 0.5: #horizontal motion
        startY = random.randint(50, screenHeight+50)
        endY = random.randint(50, screenHeight+50)
        if ran2 < 0.5: #L to R
            startX = -50
            endX = screenWidth
        else: #R to L
            startX = screenWidth
            endX = -50
    else: #vertical motion
        startX = random.randint(-50, screenWidth)
        endX = random.randint(-50, screenWidth)
        if random.random() < 0.5: #U to D
            startY = -50
            endY = screenHeight
        else: # D to U
            startY = screenHeight
            endY = -50
    return [startX, startY, endX, endY]

#function to randomly generate one square object, assigning path
def generateSquare(screenWidth, screenHeight, color):
    velocity = 4
    path = randomPath(screenWidth, screenHeight)
    return colorSquare(color, path, velocity)       

#function to check if a circle and a square overlap
def overlap(board, square):
    ballLocation = board.getBallLocation()
    a = ballLocation[0]
    b = ballLocation[1]
    r = ballLocation[2] + 5
    #check top edge
    if square.x > a:
        if math.sqrt((square.x - a) ** 2 + (square.y - b) ** 2) <= r:
            return True
        else:
            return False
    elif square.x <= a <= square.x + 50:
        if abs(square.y - b) <= r:
            return True
        else:
            return False
    elif square.x + 50 < a:
        if math.sqrt((square.x + 50 - a) ** 2 + (square.y - b) ** 2) <= r:
            return True
        else:
            return False
    #check bottom edge
    if square.x > a:
        if math.sqrt((square.x - a) ** 2 + (square.y + 50 - b) ** 2) <= r:
            return True
        else:
            return False
    elif square.x <= a <= square.x + 50:
        if abs(square.y + 50 - b) <= r:
            return True
        else:
            return False
    elif square.x + 50 < a:
        if math.sqrt((square.x + 50 - a) ** 2 + (square.y + 50 - b) ** 2) <= r:
            return True
        else:
            return False
    #check left edge
    if square.y > b:
        if math.sqrt((square.x - a) ** 2 + (square.y - b) ** 2) <= r:
            return True
        else:
            return False
    elif square.y <= b <= square.y + 50:
        if abs(square.x - a) <= r:
            return True
        else:
            return False
    elif square.y + 50 < b:
        if math.sqrt((square.x - a) ** 2 + (square.y + 50 - b) ** 2) <= r:
            return True
        else:
            return False
    #check right edge
    if square.y > b:
        if math.sqrt((square.x + 50 - a) ** 2 + (square.y - b) ** 2) <= r:
            return True
        else:
            return False
    elif square.y <= b <= square.y + 50:
        if abs(square.x + 50 - a) <= r:
            return True
        else:
            return False
    elif square.y + 50 < b:
        if math.sqrt((square.x + 50 - a) ** 2 + (square.y + 50 - b) ** 2) <= r:
            return True
        else:
            return False
    
#colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

columns = int(input("How many rows for the grid? "))
rows = int(input("How many columns for the grid? "))

difficulty = input("What level of difficulty would you like? (easy, medium, hard, insane) ")
while not ((difficulty == "easy") or (difficulty == "medium") or (difficulty == "hard") or (difficulty == "insane")):
    print("Try Again with a real difficulty this time.")
    difficulty = input("What level of difficulty would you like? (easy, medium, hard, insane) ")

pygame.display.set_caption("Avoidance Ball")

screenWidth = 400 + 100 * rows
screenHeight = 400 + 100 * columns
win = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

gameBoard = board(rows, columns, 5, white)
gameBoard.grid[0][0] = 1

locationBall = [0, 0]

colorSquares = []

score = 0
obstacleCount = 0
moveLoop = 0
font = pygame.font.SysFont("calibri", 30, True)

#menu loop - select difficulty
if difficulty == "easy":
    number = round((2 + rows + columns) / 2)
    gSquares = number
    rSquares = number
elif difficulty == "medium":
    number = round((3 + rows + columns) / 2)
    if number - 1 > 0:
        gSquares = number - 1
    else:
        gSquares = 1
    rSquares = number + 1
elif difficulty == "hard":
    number = round((4 + rows + columns) / 2)
    if number - 2 > 0:
        gSquares = number - 2
    else:
        gSquares = 1
    rSquares = number + 2
elif difficulty == "insane":
    number = round((4 + rows + columns) / 2)
    if number - 3 > 0:
        gSquares = number - 3
    else:
        gSquares = 1
    rSquares = number + 3
for thing in range(rSquares):
    colorSquares.append(generateSquare(screenWidth, screenHeight, red))
for thing in range(gSquares):
    colorSquares.append(generateSquare(screenWidth, screenHeight, green))

#loading screen
win.fill(black)
loadingText = font.render("Avoidance Ball", 1, white)
win.blit(loadingText, (round(screenWidth/2 - loadingText.get_width()/2), round(screenHeight/2 - loadingText.get_height()/2)))
pygame.display.update()
pygame.time.delay(2000)

#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    #limits speed of ball movement
    if moveLoop > 0:
        moveLoop += 1
    if moveLoop > 5:
        moveLoop = 0

    #sets placeholder values of current location of ball
    yValue = locationBall[0]
    xValue = locationBall[1]

    #adjusts placeholder values with key input; resets original location to be empty
    if keys[pygame.K_a] and moveLoop == 0:
        yValue = (yValue + rows - 1) % rows
        moveLoop = 1
        gameBoard.grid[locationBall[0]][locationBall[1]] = 0
    if keys[pygame.K_d] and moveLoop == 0:
        yValue = (yValue + 1) % rows
        moveLoop = 1
        gameBoard.grid[locationBall[0]][locationBall[1]] = 0
    if keys[pygame.K_w] and moveLoop == 0:
        xValue = (xValue + columns - 1) % columns
        moveLoop = 1
        gameBoard.grid[locationBall[0]][locationBall[1]] = 0
    if keys[pygame.K_s] and moveLoop == 0:
        xValue = (xValue + 1) % columns
        moveLoop = 1
        gameBoard.grid[locationBall[0]][locationBall[1]] = 0
    
    #switches placeholder values back to location of ball to be updated on grid
    locationBall[0] = yValue
    locationBall[1] = xValue
    gameBoard.grid[locationBall[0]][locationBall[1]] = 1

    #draws grid and prints text
    win.fill(black)
    gameBoard.draw(win, blue)

    #checks if squares are done
    i = 0
    while i < len(colorSquares):
        colorSquares[i].frameCount += 1
        #tried using positions but failed, frames works better
        if (colorSquares[i].frameCount - colorSquares[i].frames) == 0:
            #square = square.color
            colorSquares[i] = generateSquare(screenWidth, screenHeight, colorSquares[i].color)
        #checks collision between ball and squares
        if overlap(gameBoard, colorSquares[i]):
            if colorSquares[i].color == green:
                score += 1
                colorSquares[i] = generateSquare(screenWidth, screenHeight, colorSquares[i].color)
            elif colorSquares[i].color == red:
                score -= 1
                obstacleCount += 1
                colorSquares[i] = generateSquare(screenWidth, screenHeight, colorSquares[i].color)
        colorSquares[i].draw(win)
        colorSquares[i].x += colorSquares[i].speedX
        colorSquares[i].y += colorSquares[i].speedY
        i += 1

    #adds text
    scoreText = font.render("Score: " + str(score), 1, white)
    obstacleText = font.render("Obstacles Hit: " + str(obstacleCount), 1, white)
    win.blit(scoreText, (100, 50))
    win.blit(obstacleText, (100, 100))

    #updates window
    pygame.display.update()

    #ends game
    if obstacleCount >= 3:
        win.fill(black)
        endText = font.render("It's Over!", 1, white)
        win.blit(endText, (round(screenWidth/2 - endText.get_width()/2), round(screenHeight/2 - endText.get_height()/2)))
        pygame.display.update()
        pygame.time.delay(2500)
        run = False

    #limits fps to 60
    clock.tick(60)

sys.exit()
pygame.quit()