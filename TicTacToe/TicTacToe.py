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