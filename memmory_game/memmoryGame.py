import tkinter as tk
import random
from tkinter import messagebox
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        # Initialize game variables
        self.name = ""
        self.board_size = (4, 3)
        self.tile_type = 'Numbers'
        self.game_mode = 'Clock'
        self.cards = []
        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.matched_cards = 0
        self.match_count_player = 0
        self.match_count_computer = 0
        self.timer_started = False
        self.start_time = None
        self.elapsed_time = 0
        self.game_running = False

        self.create_settings()

    def create_settings(self):
        # Create the settings UI in Tkinter
        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.pack()

        # Player's Name
        self.name_label = tk.Label(self.settings_frame, text="Enter your name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.settings_frame)
        self.name_entry.grid(row=0, column=1)

        # Board Size
        self.board_size_label = tk.Label(self.settings_frame, text="Select Board Size:")
        self.board_size_label.grid(row=1, column=0)
        self.board_size_var = tk.StringVar(value="4x3")
        self.board_size_menu = tk.OptionMenu(self.settings_frame, self.board_size_var, "4x3", "4x6", "6x7")
        self.board_size_menu.grid(row=1, column=1)

        # Tile Type
        self.tile_type_label = tk.Label(self.settings_frame, text="Select Tile Type:")
        self.tile_type_label.grid(row=2, column=0)
        self.tile_type_var = tk.StringVar(value="Numbers")
        self.tile_type_menu = tk.OptionMenu(self.settings_frame, self.tile_type_var, "Numbers", "Colors")#, "Flowers")
        self.tile_type_menu.grid(row=2, column=1)

        # Game Mode
        self.game_mode_label = tk.Label(self.settings_frame, text="Select Game Mode:")
        self.game_mode_label.grid(row=3, column=0)
        self.game_mode_var = tk.StringVar(value="Clock")
        self.game_mode_menu = tk.OptionMenu(self.settings_frame, self.game_mode_var, "Clock")#, "Against Computer")
        self.game_mode_menu.grid(row=3, column=1)

        # Start Button
        self.start_button = tk.Button(self.settings_frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=4, column=0, columnspan=2)

    def start_game(self):
        # Gather settings and start the game
        self.name = self.name_entry.get()
        board_size = self.board_size_var.get()
        self.board_size = tuple(map(int, board_size.split('x')))
        self.tile_type = self.tile_type_var.get()
        self.game_mode = self.game_mode_var.get()

        # Validate name input
        if not self.name:
            messagebox.showerror("Input Error", "Please enter your name!")
            return

        # Hide settings and start the game board
        self.settings_frame.pack_forget()
        self.create_board()

    def create_board(self):
        self.cards = self.generate_cards()
        random.shuffle(self.cards)

        # Create a frame for the game board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = []
        for row in range(self.board_size[0]):
            row_buttons = []
            for col in range(self.board_size[1]):
                button = tk.Button(self.board_frame, text=" ", width=10, height=3, 
                                   command=lambda r=row, c=col: self.card_clicked(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Add Name and Timer Label
        self.name_label = tk.Label(self.root, text=f"Player: {self.name}")
        self.name_label.pack()

        self.timer_label = tk.Label(self.root, text="Time: 0 seconds")
        self.timer_label.pack()

        if self.game_mode == "Clock":
            self.start_timer()

    def generate_cards(self):
        # Generate cards based on the tile_type chosen (numbers, colors, or images)
        total_cards = self.board_size[0] * self.board_size[1]
        card_values = self.get_tile_values(total_cards)
        return card_values * 2  # 2 identical cards for each tile

    def get_tile_values(self, total_cards):
        if self.tile_type == 'Numbers':
            return list(range(1, total_cards // 2 + 1))
        elif self.tile_type == 'Colors':
            if total_cards == 12:
                return ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange']
            elif total_cards == 24:
                return ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Cyan', 'Magenta', 'Brown', 'Gray', 'Black']
            elif total_cards == 42:
                return ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Cyan', 'Magenta', 'Brown', 'Gray', 'Black',
                        'White', 'Teal', 'Maroon', 'Olive', 'Lime', 'Navy', 'Gold', 'Silver', 'Turquoise', 'Lavender', 'Peach', 'Coral']
        
        # elif self.tile_type == 'Flowers':
        #     return ['Flower'] * (total_cards // 2)  # placeholder for image tiles

    def start_timer(self):
        self.start_time = time.time()
        self.timer_started = True
        self.update_timer()

    def update_timer(self):
        if self.timer_started:
            self.elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {self.elapsed_time} seconds")
            self.root.after(1000, self.update_timer)

    def card_clicked(self, row, col):
        if self.first_card and self.second_card:
            return  # Prevent clicking while previous cards are still open

        card_value = self.cards[row * self.board_size[1] + col]
        if card_value == 'matched':
            return  # Ignore if card is already matched

        # Show the card's value
        if self.tile_type == 'Colors':
          self.buttons[row][col].config(bg=card_value,text=str(card_value), state="disabled")  # Set background color
        else:
            self.buttons[row][col].config(text=str(card_value), state="disabled")

        if not self.first_card:
            self.first_card = (row, col)
        elif not self.second_card:
            self.second_card = (row, col)
            self.check_match()

    def check_match(self):
        row1, col1 = self.first_card
        row2, col2 = self.second_card

        card1_value = self.cards[row1 * self.board_size[1] + col1]
        card2_value = self.cards[row2 * self.board_size[1] + col2]

        if card1_value == card2_value:
            # Cards match
            self.cards[row1 * self.board_size[1] + col1] = 'matched'
            self.cards[row2 * self.board_size[1] + col2] = 'matched'
            self.matched_cards += 2
            self.first_card = None
            self.second_card = None
            if self.matched_cards == len(self.cards):
                # Stop the timer
                self.timer_started = False
                messagebox.showinfo("Game Over", f"Congratulations {self.name}, you completed the game in {self.elapsed_time} seconds!")
                self.root.quit()
                self.root.destroy()  # Destroy the Tk instance
        else:
            # Cards don't match, hide them after a short delay
            self.root.after(1000, self.hide_cards, row1, col1, row2, col2)

    def hide_cards(self, row1, col1, row2, col2):
        if self.tile_type == 'Colors':
            default_bg = self.board_frame.cget('bg')  # Get default background color
            self.buttons[row1][col1].config(bg=default_bg, text=" ", state="normal")
            self.buttons[row2][col2].config(bg=default_bg, text=" ", state="normal")
        else:
            self.buttons[row1][col1].config(text=" ", state="normal")
            self.buttons[row2][col2].config(text=" ", state="normal")
        self.first_card = None
        self.second_card = None

def rungame():
    # Create the main Tkinter window
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
