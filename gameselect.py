from sentence_transformers import SentenceTransformer, util
import torch

#maybe take this out to a seperated file
game_list = {"Rock, Paper, Scissors":{"run code":"python.py",
                                      "text":"Rock, Paper, Scissors is a classic game almost everyone knows. The game is played by 1 player against the computer.\n Once opens, you will be asked to insert your name. Next, you will be asked to insert your selection- 1 for Rock/2 for Paper/3 for Scissors.\nOnce done thinking, you'll get the results: what you chose, what the computer chose and if you win/loose/tie (Teko-Teko).\nEnjoy!",
                                      "image":"./paper_rock_scissors/imgs/scr3.png",
                                      "ai_text":"fun, 1 player, logic, fast, classic"}, 
            "Tic-Tac-Toe":{"run code":"python.py",
                           "text":"Classic Tic-Tac-Tow (X-O) game for two players.\nOnce opens, you will be asked to insert names for both players. Clicking 'Start' will open the main game screen, where each one of you, at his turn, clicks the square he wants to put his X/O in. There are 3 options for ending the game: X player wins, O player wins or Tie.\nIf you choose to play again- the game will restart while the other player starts (once X player starts, in the next game- O player starts and so on). The winning or tie numbers will be accumulated and shown each time you end a game, untill you'll exit.\nEnjoy!",
                           "image":"./TicTacToe_tkinter/imgs/scrn2.png",
                           "ai_text":"fun, 2 players, logic, classic"}, 
            "Hangman":{"run code":"python.py",
                       "text":"Hangman is an english word game. Once ran, you will have the 4 elements that will guide you:\n1. Word to guess with number of letters in the parentheses followed by underline for each letter.\n2. Hangman is the ASCII art of the status you are at (each wrong guess will promote the hanging man art).\n3. Tries left is how many times you can error (initialy 6).\n4.Letters used is an array of letters you have guessed before to help you not guess the same again.\nNow, all you need to do is to guess a letter. The letter you guesed will now be in the Letters used array, and if it is in the word- it will replace the relevant underline or underlines.\nIf you guess before the man is hang (less than 6 tries)- you win and the man drops free from the hanging pole. If you do not guess the word in time- man stays hanged and you loose.\nEnjoy!",
                       "image":"./hangman/imgs/openning.png",
                       "ai_text":"fun, 1 player, word, words, text, english, not very short, long, vocabulary"},
            # "Point Color Detect":{"run code":"./ColorDetect/color_detect.py",
            #                         "text":"This is not a game per say, but a cute and fun app.\nLoad a piture, Double click any point on the image and you'll get the name and RGB codes with a solid bar of the color at that point. In relation to the color of the bar, the text will appear black (over lighter colors) or white (over darker colors).\nEnjoy!",
            #                         "image":"./ColorDetect/imgs/scr1.png",
            #                         "ai_text":"color, colors, RGB, app image, picture, point, show, cute, fun"}, 
            "Memmory Game":{"run code":"./memmory_game\memmoryGame.py",
                                    "text":"Memmory Game is a classic. pick your choice of numbers or colors and the size of the bord (the bigger- the harder) and start flipping the tiles.\nOnce you have a match- the tiles will stay open. Try to find all couples as fast as you can!\nEnjoy!",
                                    "image":"./memmory_game/imgs/scrn_colors.png",
                                    "ai_text":"color, colors, numbers, pictures, memory, cute, fun, long"},
            # "Chutes N Ladders":{"run code":"./memmory_game\memmoryGame.py",
            #                         "text":"Chutes N Ladders Game.\nEnjoy!",
            #                         "image":"logo.png",
            #                         "ai_text":"classic, board game, numbers, fun"},
            "Guess the Number":{"run code":"python.py",
                                    "text":"Guess the Number Game is a small cute numbers game.\nThe game has 2 modes. once you run it, you will be asked to select the mode:\n1. Computer guesses the number user thought of by hints (low/high/equal).\n2. Computer generates a random number. User guesses it by hints (low/high).\nIf you select option 1- you will be asked to guess the number the computer is thinking of. First you'll be asked to enter the top range of numbers. Then, the computer will randomly select a number between 1-top. Enter your guess. you will be answered if it is lower or higher than the computer's pick. Continue untill you guess the number. Try to bit your previous number of guesses!\nIf you select option 2- the computer will try to guess your number. First you'll be asked to enter the top range of numbers. Now- think of a number between 1-top. The computer will guess the number. Indicate if the guess higher (h) / lower (l) / equal (e) to your number. Continue untill computer guesses your number (equal)\nEnjoy!",
                                    "image":"./GuessingGame/imgs/2.png",
                                    "ai_text":"fun, 1 player, number, numbers, guessing game, math, not too long"}} 

class GameSelector:
    def __init__(self, game_list):
        # Load pre-trained sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Prepare embeddings for game descriptions
        self.game_names = list(game_list.keys())
        self.game_descriptions = [game_list[name]['text']+" "+game_list[name]['ai_text'] for name in self.game_names]
        self.description_embeddings = self.model.encode(self.game_descriptions)

    def find_best_match(self, user_input):
        # Encode user input
        input_embedding = self.model.encode(user_input)
        
        # Calculate cosine similarities
        similarities = util.cos_sim(input_embedding, self.description_embeddings)[0]
        
        # Find the index of the most similar description
        best_match_idx = torch.argmax(similarities).item()
        
        # Return the game name and similarity score
        return self.game_names[best_match_idx], similarities[best_match_idx].item()