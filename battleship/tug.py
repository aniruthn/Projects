class tug(object):
    #initializer
    def __init__ (self):
        self.letter = "T"
    #method that updates board with location of tug
    def updateBoard(self, object, locations):
        object.display[locations[1][0]][locations[0][0]] = self.letter
        object.display[locations[1][1]][locations[0][1]] = self.letter
