import pygame
import math
pygame.init()

class colorSquare():
    #initialize object ---- have to import math
    def __init__(self, color, randomPath, velocity):
        self.color = color
        self.randomPath = randomPath
        self.x = float(self.randomPath[0])
        self.y = float(self.randomPath[1])
        #deriving component speeds
        self.velocity = velocity
        changeY = self.randomPath[3] - self.randomPath[1]
        changeX = self.randomPath[2] - self.randomPath[0]
        #edge case to prevent dividing by infinity
        if changeX == 0:
            self.theta = math.pi / 2
        else:
            self.theta = math.atan(changeY / changeX)
        self.speedX = abs(self.velocity * math.cos(self.theta))
        self.speedY = abs(self.velocity * math.sin(self.theta))
        if (changeY < 0 and changeX < 0):
            self.speedX *= -1
            self.speedY *= -1
        elif (changeY > 0 and changeX < 0):
            self.speedX *= -1
        elif (changeY < 0 and changeX > 0):
            self.speedY *= -1
        self.frames = round(abs(changeY / self.speedY))
        self.frameCount = 0
    #draws the object
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 50, 50))