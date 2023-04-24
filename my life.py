# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Prog 3 - My life

# write a text file named mylife.txt using append
with open("mylife.txt", "a") as file_life:
    # ask for user input
    user_input = input("Enter line: ")
    
    #use while loop
    i = 0
    yes_no = " "

    ask_user = input("Are there more lines? y/n")
    while yes_no == "y":
        file_life.write()