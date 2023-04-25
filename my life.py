# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Prog 3 - My life

# import pyfiglet
import pyfiglet
# import rich
from rich.theme import Theme
from rich.console import Console

theme_life = Theme ({"title": "bold green", "load": "yellow", "lines" : "magenta", "done" : "bold blue"})
console_life = Console(theme = theme_life)

# choose design/ format
title = pyfiglet.figlet_format("My Life".center(55), font = "digital")
# print title
console_life.print(title, style = "title")

# write a text file named mylife.txt using append
with open("mylife.txt", "w") as file_life:
    # add title
    console_life.print("_" * 60, style = "lines")
    file_life.write("My Life".center(41) + "\n\n")

    #use while loop
    yes_no = "y"
    input_num = 1    
    while yes_no == "y":
        # ask for user input
        user_input = input(f"\nEnter line {input_num}: ")
        # write the user input into mylife.txt
        file_life.write(f"Line #{input_num}: " + user_input + "\n")
        # ask user if they have more lines to add
        ask_user = input("Are there more lines? y/n: ").lower()
        input_num += 1

        # if there is no line to be input
        if ask_user == "n":
            console_life.print("_"* 60, style = "lines")
            console_life.print("\nLoading loading loading........", style = "load")
            console_life.print("\nDone! Your input is already in the text file.\n", style = "done")
            exit()
        
    
        