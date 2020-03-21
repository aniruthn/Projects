class aircraft_carrier(object):
    #initializer
    def __init__ (self):
        self.letter = "A"
    #method that updates location of board with aircraft carrier
    def updateBoard(self, object, locations):
        #determines whether x or y is the same and increments the other
        if locations[1][6] == locations[1][7]:
            object.display[locations[1][6]][locations[0][6]] = self.letter
            object.display[locations[1][6]][locations[0][6]+1] = self.letter
            object.display[locations[1][6]][locations[0][6]+2] = self.letter
            object.display[locations[1][6]][locations[0][6]+3] = self.letter
            object.display[locations[1][6]][locations[0][7]] = self.letter
        elif locations[0][6] == locations[0][7]:    
            object.display[locations[1][6]][locations[0][6]] = self.letter
            object.display[locations[1][6]+1][locations[0][6]] = self.letter
            object.display[locations[1][6]+2][locations[0][6]] = self.letter
            object.display[locations[1][6]+3][locations[0][6]] = self.letter
            object.display[locations[1][7]][locations[0][6]] = self.letter
