class battleship(object):
    #initializer
    def __init__ (self):
        self.letter = "B"
    #method that updates board with location of battleship
    def updateBoard(self, object, locations):
        #determines whether x or y is the same and increments the other
        if locations[1][4] == locations[1][5]:
            object.display[locations[1][4]][locations[0][4]] = self.letter
            object.display[locations[1][4]][locations[0][4]+1] = self.letter
            object.display[locations[1][4]][locations[0][4]+2] = self.letter
            object.display[locations[1][4]][locations[0][5]] = self.letter
        elif locations[0][4] == locations[0][5]:    
            object.display[locations[1][4]][locations[0][4]] = self.letter
            object.display[locations[1][4]+1][locations[0][4]] = self.letter
            object.display[locations[1][4]+2][locations[0][4]] = self.letter
            object.display[locations[1][5]][locations[0][4]] = self.letter
