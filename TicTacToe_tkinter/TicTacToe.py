from tkinter import messagebox
import tkinter as tk
import numpy as np

#constant defaults of game visualizations (size, colors)
size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


class TicTacToe():
    
    def __init__(self):
        """
        init class
        """
        #window
        self.window = tk.Tk()
        self.window.geometry = ("300x600")
        self.window.title('Tic Tac Toe')
        #title
        self.label_title = tk.Label(self.window, text="TicTacToe Game", font=("Courier 22 bold underline"), foreground="Green")
        self.label_title.pack()
        #insert players' names
        self.label_p1 = tk.Label(self.window, text="Please enter player X name: ", font=("Courier 16"))
        self.label_p1.pack()
        self.p1_input= tk.Entry(self.window, width= 40)
        self.p1_input.focus_set()
        self.p1_input.pack()
        self.label_p2 = tk.Label(self.window, text="Please enter player O name: ", font=("Courier 16"))
        self.label_p2.pack()
        self.p2_input= tk.Entry(self.window, width= 40)
        self.p2_input.pack()
        #start game button
        self.start_button = tk.Button(self.window, text= "Start",width= 20, command= self.start_game).pack(pady=20)
        self.window.mainloop()

        
    def start_game(self):
        """
        after clicking start game- 
        1. verify players names.
        2. create window with titles and grids
        """
        self.x_name = self.p1_input.get()
        self.o_name = self.p2_input.get()
        #player name is error handling
        if not (self.x_name.strip() and self.o_name.strip()):
            messagebox.showerror("Error", "Please enter valid player names")
            return
        self.window.withdraw()
        #main window
        self.game_window = tk.Toplevel(self.window)
        self.game_window.title('Tic Tac Toe')
        #title
        self.label_title = tk.Label(self.game_window, text=f"TicTacToe Game\n{self.x_name} (X) vs. {self.o_name} (O)", font=("Courier 22 bold underline"), foreground="Green")
        self.label_title.pack()
        #grid
        self.canvas = tk.Canvas(self.game_window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        # clicks from user
        self.game_window.bind('<Button-1>', self.click)
        #initializing the game
        self.initialize_board()        
        self.player_X_turns = True  #In the first game- player X is clicking
        self.board_status = np.zeros(shape=(3, 3))  #

        self.player_X_starts = True #In the first game- player X is starting
        self.reset_board = False
        self.gameover = False
        self.tie = False  
        self.X_wins = False 
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0
        
    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        """
        between each game- board needs to be initialized (draw grid)
        """
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    def play_again(self):
        """
        clicking play again button.
        Restart window.
        """
        self.play_again_button.destroy()
        self.exit_button.destroy()
        self.canvas.delete("all")                 
        self.initialize_board()  
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))
        self.reset_board = False

    def quit(self):
        """
        clicking 'Exit'- destroy all
        """
        self.game_window.quit()
        self.game_window.destroy()
        self.window.quit() 
        self.window.destroy()


    def draw_O(self, logical_position):
        """
        draw 'O' in the clicked square of grid (canvas.create_oval)
        """
        logical_position = np.array(logical_position) #grid value on the board
        grid_position = self.convert_logical_to_grid_position(logical_position) #actual pixel values of the center of the grid
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                outline=symbol_O_color)

    def draw_X(self, logical_position):
        """
        draw 'X' in the clicked square of grid (2 lines)
        """
        grid_position = self.convert_logical_to_grid_position(logical_position) #actual pixel values of the center of the grid
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)

    def display_gameover(self):
        """
        In case player X wins / player O wins / tie - jump to the screen that shows who won and the accumulation of wins
        """
        if self.X_wins:
            self.X_score += 1
            text = f'Winner: \t{self.x_name} (X)'
            color = symbol_X_color
        elif self.O_wins:
            self.O_score += 1
            text = f'Winner: \t{self.o_name} (O)'
            color = symbol_O_color
        else:
            self.tie_score += 1
            text = 'Its a tie'
            color = 'gray'

        #clear grid and show the winning and winning table text
        self.canvas.delete("all")
        self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 26 bold", fill=color, text=text)

        score_text = 'Scores: \n'
        self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 20 bold", fill=Green_color, text=score_text)

        score_text = f'\t{self.x_name} (X) : ' + str(self.X_score) + '\n'
        score_text += f'\t{self.o_name} (O): ' + str(self.O_score) + '\n'
        score_text += '\tTie: ' + str(self.tie_score) + '\n\n'
        self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 18 bold", fill=Green_color, text=score_text)
        self.reset_board = True

        # Create "Play Again" button
        self.play_again_button = tk.Button(self.game_window, text="Play Again", font=("cmr 18 bold"), bg=Green_color, fg="white", command=self.play_again)
        self.play_again_button.place(x=size_of_board / 3, y=16 * size_of_board / 16, anchor="center")

        # Create "Exit" button
        self.exit_button = tk.Button(self.game_window, text="Exit", font=("cmr 18 bold"), bg="red", fg="white", command=self.quit)
        self.exit_button.place(x=1.5 * size_of_board / 2, y=16 * size_of_board / 16, anchor="center")

   
    def convert_logical_to_grid_position(self, logical_position):
        """
        convert the click grid value on the board to the actual pixel value.
        return pixel value (the square center)
        """
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        """
        convert the pixel position to the square grid
        """
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        """
        check in the board status array if the position of this grid square already has a value in it
        """
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def is_winner(self, player):
        """
        After every step, check if there is a strike of X or O
        by comparing the values in each row/column/diagonal
        """
        player = -1 if player == 'X' else 1

        # Three in a row
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        # Diagonals
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    def is_tie(self):
        """
        if no one wins, but all board grid are occupied- its a tie
        """
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    def is_gameover(self):
        """
        In case of win or tie- the game is over
        """
        # Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        # if self.X_wins:
        #     print(f'{self.x_name} (X) wins')
        # if self.O_wins:
        #     print(f'{self.o_name} (O) wins')
        # if self.tie:
        #     print('Its a tie')

        return gameover


    def click(self, event):
        """
        a click event. can result in drawing X and passing turn to O (or the opposite) or result as a game over
        """
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns

            # Check if game is over
            if self.is_gameover():
                self.display_gameover()