class sub(object):
    #initializer
    def __init__ (self):
        self.letter = "S"
    #method that updates board with location of sub
    def updateBoard(self, object, locations):
        #determines whether x or y is the same and increments the other
        if locations[1][2] == locations[1][3]:
            object.display[locations[1][2]][locations[0][2]] = self.letter
            object.display[locations[1][2]][locations[0][2]+1] = self.letter
            object.display[locations[1][2]][locations[0][3]] = self.letter
        elif locations[0][2] == locations[0][3]:    
            object.display[locations[1][2]][locations[0][2]] = self.letter
            object.display[locations[1][2]+1][locations[0][2]] = self.letter
            object.display[locations[1][3]][locations[0][2]] = self.letter
