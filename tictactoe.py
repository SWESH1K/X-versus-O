import tkinter as tk
from tkinter import messagebox
import pygame
import os

# Import game functions
from game_mechanics import *

# Initialize pygame mixer
pygame.mixer.init()

# Set the path to the sounds folder
SOUNDS_FOLDER = "sounds"

# Load sound effects
def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(SOUNDS_FOLDER, filename))

gameover_sound = load_sound("gameover.wav")
youwon_sound = load_sound("youwon.wav")
click_sound = load_sound("click.wav")

# Create a Tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="red")  # Set background color to red

# Styling constants
BUTTON_FONT = ('Arial', 20, 'bold')  # Make the font bold
BUTTON_WIDTH = 6
BUTTON_HEIGHT = 3
BUTTON_COLOR = "yellow"  # Set button color to yellow

# Configure message box theme
root.option_add("*Dialog.msg.font", BUTTON_FONT)
root.option_add("*Dialog.msg.width", BUTTON_WIDTH)
root.option_add("*Dialog.msg.wrapLength", 200)
root.option_add("*Dialog.msg.foreground", "red")
root.option_add("*Dialog.msg.background", "yellow")

# Function to play button click sound
def play_click_sound():
    click_sound.play()

# Function to play game over sound
def play_gameover_sound():
    gameover_sound.play()

# Function to play winning sound
def play_youwon_sound():
    youwon_sound.play()

# Function to reset the game board
def resetBoard():
    for i in range(10):
        board[i] = ' '

# Function to restart the game
def restart_game():
    # Reset the game state
    resetBoard()
    for button in buttons:
        button.config(text=' ', state='normal')

# Function to handle player click
def player_click(position):
    play_click_sound()  # Play button click sound
    if spaceIsFree(position):
        insertLetter('X', position)
        buttons[position - 1].config(text='X', state='disabled', relief=tk.SUNKEN)
        if isWinner(board, 'X'):
            play_youwon_sound()  # Play winning sound
            messagebox.showinfo("Tic Tac Toe", "Congratulations! You win!")
            restart_game()
        elif isBoardfull(board):
            play_gameover_sound()  # Play game over sound
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            restart_game()
        else:
            bot_move()

# Function to handle bot move
def bot_move():
    move = botMove()
    if move != 0:
        insertLetter('O', move)
        buttons[move - 1].config(text='O', state='disabled', relief=tk.SUNKEN)
        if isWinner(board, 'O'):
            play_gameover_sound()  # Play game over sound
            messagebox.showinfo("Tic Tac Toe", "Sorry, you lost!")
            restart_game()
        elif isBoardfull(board):
            play_gameover_sound()  # Play game over sound
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            restart_game()

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(1, 10):
    button = tk.Button(root, text=' ', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       command=lambda i=i: player_click(i), bg=BUTTON_COLOR, fg='#333', bd=2)
    button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)
    buttons.append(button)

# Start the game
if __name__ == '__main__':
    root.mainloop()
