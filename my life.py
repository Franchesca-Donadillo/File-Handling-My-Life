# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Prog 3 - My life

# write a text file named mylife.txt using append
with open("mylife.txt", "a") as file_life:
    
    #use while loop
    i = 0
    yes_no = "y"
    
    user_input = input("Enter line: ")
    ask_user = input("Are there more lines? y/n: ").lower()
    
    while True:
        user_input = input("Enter line: ")
        file_life.write(user_input)
        ask_user = input("Are there more lines? y/n: ").lower()
        i+=1

        if ask_user == "n":
            print("Done!")
            exit()
        
    
        