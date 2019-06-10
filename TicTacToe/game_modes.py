from TicTacToe import TicTacToe

def playerVplayer():
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

def playerVai():
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