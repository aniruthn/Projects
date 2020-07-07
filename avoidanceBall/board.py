import pygame
pygame.init()

class board():
    #initialize object
    def __init__(self, rows, columns, thickness, color):
        self.rows = rows
        self.columns = columns
        self.thickness = thickness
        self.color = color
        self.grid = [[0 for i in range(self.columns)] for j in range(self.rows)]
    #gets location of ball
    def getBallLocation(self):
        for row in range (self.rows):
            for col in range (self.columns):
                if self.grid[row][col] == 1:
                    return [250 + row * 100, 250 + col * 100, 25]
    #redraws the board
    def draw(self, win, ballColor):
        #creates grid
        for row in range (self.rows):
            for col in range (self.columns):
                pygame.draw.rect(win, self.color, (200 + row * 100, 200 + col * 100, 100, 100), self.thickness)
                #draws ball
                if self.grid[row][col] == 1:
                    pygame.draw.circle(win, ballColor, (250 + row * 100, 250 + col * 100), 25, self.thickness)