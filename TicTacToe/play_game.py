import game_modes

def main():
    mode = int(input("Enter 1 for player vs player, or 2 for player vs ai: "))
    if mode == 1:
        game_modes.playerVplayer()  # human vs human
    elif mode == 2:
        game_modes.playerVai()  # human vs ai

main()