# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Prog 3 - My life

# write a text file named mylife.txt using append
with open("mylife.txt", "w") as file_life:
    
    #use while loop
    yes_no = "y"
        
    while yes_no == "y":
        # ask for user input
        user_input = input("Enter line: ")
        # write the user input into mylife.txt
        file_life.write(user_input + "\n")
        # ask user if they have more lines to add
        ask_user = input("Are there more lines? y/n: ").lower()

        if ask_user == "n":
            print("Done!")
            exit()
        
    
        