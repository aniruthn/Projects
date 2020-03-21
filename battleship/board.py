class board(object):
    #intializer
    def __init__ (self, rows, columns):
        self.display = [["-" for i in range(columns)] for j in range(rows)]
    #method to print the board in a readable manner
    def printBoard (self):
        print()
        length = len(self.display[0])
        print(" ", end=" ")
        for i in range(length):
            print (i+1, end=" ")
        print()
        #uses counters since the r and c refer to characters
        counterR = -1
        for r in self.display:
            print(counterR+2, end=" ")
            counterR += 1
            counterC = -1
            for c in r:
                counterC += 1
                #uses end statement to prevent the creation of a new line after each column
                print(self.display[counterR][counterC], end=" ")
            print()
        print()
    #method to check the board to determine if there are any ships left
    def checkBoard (self):
        #uses counters since the r and c refer to characters
        counterR = -1
        for r in self.display:
            counterR += 1
            counterC = -1
            for c in r:
                counterC += 1
                token = self.display[counterR][counterC]
                if (token == "T") or (token == "S") or (token == "B") or (token == "A"):
                    return 0
        return 1
