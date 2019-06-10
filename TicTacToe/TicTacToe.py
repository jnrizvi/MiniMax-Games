from minimaxTTT import *

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
        if not ((move >= 1) and (move <= 9)):
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
        return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

    def evaluate_board(self, board):
        if has_won(self.board, "X"):
            return 1
        elif has_won(self.board, "O"):
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


    def playerVai(self, current_board, isMaximizing):
        prompt = "Y"
            
        while prompt == "y" or prompt == "Y":
            end = False
            aiGame = TicTacToe()
            min_symb = input("Choose X or O (X goes first):")  # according to the ai, the player is the minimizing player
            if min_symb == "O":
                max_symb = "X"
            elif min_symb == "X":
                max_symb = "O"

            aiGame.drawBoard(aiGame.board)
            while end == False:
                valid = False
                if min_symb == "X":
                    guess = int(input("It's your turn. Enter a valid integer:"))
                    while valid == False:
                        if not aiGame.select_space(aiGame.board, guess, min_symb):
                            guess = int(input("Invalid move. Please enter an integer between 1 and 9 that is not occupied "))
                        else:
                            valid = True
                            aiGame.drawBoard(aiGame.board)


                    print("Now the ai is deciding...")
                    select_space(aiGame.board, minimax(aiGame.board, True)[1], max_symb)
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

                elif min_symb == "O":
                    print("The ai is deciding...")
                    select_space(aiGame.board, minimax(aiGame.board, True)[1], max_symb)  # the ai will go first
                    aiGame.drawBoard(aiGame.board)                                        


                    guess = int(input("It's your turn. Enter a valid integer:"))          # then the player
                    while valid == False:
                        if not aiGame.select_space(aiGame.board, guess, min_symb):
                            guess = int(input("Invalid move. Please enter an integer between 1 and 9 that is not occupied "))
                        else:
                            valid = True
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

def main():
    myGame = TicTacToe()
    # print(myGame.board)
    # myGame.playerVplayer()  # human vs human

    # myGame.playerVai()  # human vs ai

main()