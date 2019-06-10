# from minimaxTTT import *
from copy import deepcopy

class TicTacToe:
    def __init__(self):       
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
    def drawBoard(self, board):
    # This method prints out the board with current plays adjacent to a board with index.
        
        print()
        print("\t\tTic Tac Toe")
        print("\n\n")
        legend = 1
        for iRow in board:
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
        if move not in range(1,10):
            return False
        row = int((move-1)/3)
        col = (move-1)%3
        if board[row][col] != "X" and board[row][col] != "O":
            board[row][col] = turn
            return True
        else:
            return False
            
        
    def available_moves(self, board):
        moves = []
        for row in board:
            for col in row:
                if col != "X" and col != "O":
                    moves.append(int(col))
        return moves

  
    def has_won(self, board, player):
        for row in board:
            if row.count(player) == 3:
                return True
        for i in range(3):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False
    
    def game_is_over(self, board):
        return self.has_won(board, "X") or self.has_won(board, "O") or len(self.available_moves(board)) == 0

    def evaluate_board(self, board):
        if self.has_won(board, "X"):
            return 1
        elif self.has_won(board, "O"):
            return -1
        else:
            return 0
    
    def playerVplayer(self):
        prompt = "Y"
    
        while prompt == "y" or prompt == "Y":
            end = False
            symbol = "O"
            myGame = TicTacToe()
            myGame.drawBoard(myGame.board)
            
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
                        myGame.drawBoard(myGame.board)    
                
                if myGame.has_won(myGame.board, symbol) == True:
                    end = True
                    print(symbol, "wins. Congrats!")
                    
                elif len(myGame.available_moves(myGame.board)) == 0:
                    end = True
                    print("It's a tie.")

            input("Press Enter to continue")
            prompt = input("Do you want to play another game? (Y/N)? ")

    def minimax(self, input_board, is_maximizing):
        # Base case - the game is over, so we return the value of the board
        if self.game_is_over(input_board):
            return [self.evaluate_board(input_board), ""]
        # The maximizing player
        if is_maximizing:
        # The best value starts at the lowest possible value
            best_value = -float("Inf")
            best_move = ""
        # Loop through all the available moves
            for move in self.available_moves(input_board):
                # Make a copy of the board and apply the move to it
                new_board = deepcopy(input_board)
                self.select_space(new_board, move, "X")
                # Recursively find your opponent's best move
                hypothetical_value = self.minimax(new_board, False)[0]
            # Update best value if you found a better hypothetical value
                if hypothetical_value > best_value:
                    best_value = hypothetical_value
                    best_move = move
            return [best_value, best_move]
        # The minimizing player
        else:
            # The best value starts at the highest possible value
            best_value = float("Inf")
            best_move = ""
            # Testing all potential moves
            for move in self.available_moves(input_board):
                # Copying the board and making the move
                new_board = deepcopy(input_board)
                self.select_space(new_board, move, "O")
                # Passing the new board back to the maximizing player
                hypothetical_value = self.minimax(new_board, True)[0]
                # Keeping track of the best value seen so far
                if hypothetical_value < best_value:
                    best_value = hypothetical_value
                    best_move = move
            return [best_value, best_move]


    def playerVai(self):
        prompt = "Y"
            
        while prompt == "y" or prompt == "Y":
            end = False
            aiGame = TicTacToe()
            min_symb = "X"  # according to the ai, the player is the minimizing player
            max_symb = "O"
            isMaximizing = True
            aiGame.drawBoard(aiGame.board)
            while end == False:
                valid = False
                
                guess = int(input("It's your turn. Enter a valid integer:"))
                while valid == False:
                    if not aiGame.select_space(aiGame.board, guess, min_symb):
                        guess = int(input("Invalid move. Please enter an integer between 1 and 9 that is not occupied "))
                    else:
                        valid = True
                        aiGame.drawBoard(aiGame.board)

                print("Now the ai is deciding...")
                aiGame.select_space(aiGame.board, aiGame.minimax(aiGame.board, not isMaximizing)[1], max_symb)
                aiGame.drawBoard(aiGame.board)

                if aiGame.has_won(aiGame.board, min_symb) == True:
                    end = True
                    print(min_symb, "wins. Congrats!")
                elif aiGame.has_won(aiGame.board, max_symb) == True:
                    end = True
                    print(max_symb, "wins. Congrats!")
                elif len(aiGame.available_moves(aiGame.board)) == 0:
                    end = True
                    print("It's a tie.")

            input("Press Enter to continue")
            prompt = input("Do you want to play another game? (Y/N)? ")

def main():
    myGame = TicTacToe()
    # print(myGame.board)
    # myGame.playerVplayer()  # human vs human

    myGame.playerVai()  # human vs ai

main()