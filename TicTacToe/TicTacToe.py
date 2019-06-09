class TicTacToe:
    def __init__(self):       
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        
        print()
        print("\t\tTic Tac Toe")
        print("\n\n")
        legend = 1
        for iRow in self.board:
            print("\t", end="")
            for iCell in range(len(iRow)):
                # print(iCell)
                if iRow[iCell] != "X" and iRow[iCell] != "O":
                    print(" ", end="")
                else:
                    print(str(iRow[iCell]), end="")
                if iCell != 2:
                    print(" | ", sep="", end="")
            print("\t" + str(legend) + " | " + str(legend+1) + " | " + str(legend+2))
            if legend != 7:
                print("\t" + "---------" + "\t" + "---------")
            legend += 3

        print("\n\n\n")
    
    def select_space(self, board, move, turn):
        if not ((move >= 1) and (move <= 9)):
            return False
        row = int((move-1)/3)
        col = (move-1)%3
        if self.board[row][col] != "X" and self.board[row][col] != "O":
            self.board[row][col] = turn
            return True
        else:
            return False
            
        
    def available_moves(self, board):
        moves = []
        for row in self.board:
            for col in row:
                if col != "X" and col != "O":
                    moves.append(int(col))
        return moves

  
    def has_won(self, board, player):
        for row in self.board:
            if row.count(player) == 3:
                return True
        for i in range(3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False
    
    def game_is_over(self, board):
        return self.has_won(self.board, "X") or self.has_won(self.board, "O") or len(self.available_moves(self.board)) == 0

    def evaluate_board(self, board):
        if self.has_won(self.board, "X"):
            return 1
        elif self.has_won(self.board, "O"):
            return -1
        else:
            return 0
    
    def playerVplayer(self):
        end = False
        symbol = "O"
        myGame = TicTacToe()
        myGame.drawBoard()
        
        while end == False:
            valid = False
            
            if symbol == "O":
                symbol = "X"
            elif symbol == "X":
                symbol = "O"
                
            guess = int(input("It is the turn for " + symbol + ". What is your move? "))
                
            while valid == False:
                if not myGame.select_space(myGame.board, guess, symbol):
                    guess = int(input("Invalid move. Turn for " + symbol + " again. What is your move? "))
                else:
                    valid = True
                    myGame.drawBoard()    
            
            if myGame.has_won(myGame.board, symbol) == True:
                end = True
                print(symbol, "wins. Congrats!")
                
            elif len(myGame.available_moves(myGame.board)) == 0:
                end = True
                print("It's a tie.")

def main():
    myGame = TicTacToe()
    prompt = "Y"
    
    while prompt == "y" or prompt == "Y":
        myGame.playerVplayer()  
        input("Press Enter to continue")
        prompt = input("Do you want to play another game? (Y/N)? ")
        
main()