import random
import time

rock = "🗿"
paper = "📜"
scissors = "✂"
dic_rps = {1:rock, 2:paper, 3:scissors}

def validate_input(players_selection):
    """
    validate the player input is 1/2/3 only
    """
    if players_selection not in [1,2,3]:
        print("Input not valid")
        return False
    return True


def show_processing_icons():
    """
    simulate a "thinking" or "processing" wait for processing who wins. shows the Paper, Rock, Scissors icons flashing
    """
    i=0
    while i<6:
        print(rock, end="\r")
        time.sleep(0.5)
        print(paper, end="\r")
        time.sleep(0.5)
        print(scissors, end="\r")
        time.sleep(0.5)
        i = i+2
    print("", end="\r")

def player_selection_print(players_selection, player):
    """
    show the icon of the player's pick (1:rock, 2:paper, 3:scissors). Player can be the human or the
    """
    return player + ": " + dic_rps[players_selection]    

def winner_print(players_selection, computers_selection, player):
    """
    according to player-computer picks, return if its a tie or who's the winner
    """
    win = f"{player}- You win!"
    loose = f"{player}- I win, you loose!"
    if players_selection == computers_selection:
        return "Teko-Teko!"
    elif [players_selection, computers_selection] == [1,2]:
        return loose
    elif [players_selection, computers_selection] == [1,3]:
        return win
    elif [players_selection, computers_selection] == [2,1]:
        return win
    elif [players_selection, computers_selection] == [2,3]:
        return loose
    elif [players_selection, computers_selection] == [3,1]:
        return loose
    elif [players_selection, computers_selection] == [3,2]:
        return win  
    
def main():
    #run game in cmd
    print(f"        Rock {rock} Paper {paper} Scissors {scissors} Game")
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    player = input("\n\nInsert your name: ")
    players_selection = int(input(f"\nHi {player},\nPlease select: 1 (Rock) / 2 (Paper) / 3 (Scissors): "))
    if validate_input(players_selection):
        computers_selection = random.choice([1,2,3])
        show_processing_icons()
        print("\n\n", player_selection_print(players_selection, player), "     |     ", player_selection_print(computers_selection, "Computer"), "\n\n", winner_print(players_selection, computers_selection, player))

if __name__ == "__main__":
    main()
