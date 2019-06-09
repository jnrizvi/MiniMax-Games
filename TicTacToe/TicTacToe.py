class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
       
        self.board = [" "]*10
        self.board[0]="#"
        
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        
        print(" | ".join(self.board[7:]), "7 | 8 | 9", sep="\t")
        print("---------", "---------", sep="\t")
        print(" | ".join(self.board[4:7]), "4 | 5 | 6", sep="\t")
        print("---------", "---------", sep="\t")
        print(" | ".join(self.board[1:4]), "1 | 2 | 3", sep="\t")

    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise
        
        return " " not in self.board
    
    def cellIsEmpty(self, cell):
        empty = True
        
        for i in self.board[1:]:
            if self.board[cell] != " ":
                empty = False
        
        return empty
    
    def assignMove(self, cell, symbol):
    # assigns the symbols to the cell in the board
        
        for i in self.board[1:]:
            self.board[cell] = symbol
            
        
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""
  
    def isWinner(self, ch):
    # Given a player's letter, this method returns True if that player has won.
        
        win = False
        row = [ch, ch, ch]
        
        if self.board[1:4] == row or self.board[4:7] == row or self.board[7:] == row:
            win = True
        
        for col_num in range(1,4):
            column = self.board[col_num::3]
            if column == row:
                win = True
        
        if self.board[1::4] == row or self.board[3:8:2] == row:
            win = True
        
        return win
    
def main():
    myBoard = TicTacToe()
    prompt = "Y"
    
    print("Welcome to Tic Tac Toe Series")
    
    while prompt == "y" or prompt == "Y":
        end = False
        symbol = "o"
        myBoard = TicTacToe()
        myBoard.drawBoard()
        
        while end == False:
            valid = False
            
            if symbol == "o":
                symbol = "x"
            elif symbol == "x":
                symbol = "o"
                
            guess = int(input("It is the turn for " + symbol + ". What is your move? "))
                
            while valid == False:
                if not 1 <= guess <= 9:
                    guess = int(input("Invalid move.Turn for " + symbol + " again. What is your move? "))
                    
                elif myBoard.cellIsEmpty(guess) == False:
                    guess = int(input(str(guess) + " is not available. Turn for " + symbol + " again. What is your move? "))
                    
                elif 1 <= guess <= 9 and myBoard.cellIsEmpty(guess) == True:
                    valid = True
                    myBoard.assignMove(int(guess), symbol)
                    myBoard.drawBoard()         
            
            if myBoard.isWinner(symbol) == True:
                end = True
                print(myBoard.whoWon(), "wins. Congrats!")
                
            elif myBoard.boardFull() == True:
                end = True
                print("It's a tie.")
            
        input("Press Enter to continue")
        prompt = input("Do you want to play another game? (Y/N)? ")
        
main()