# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Prog 3 - My life

# write a text file named mylife.txt using append
with open("mylife.txt", "w") as file_life:
    # add title
    print("MY LIFE".center(55) + "\n" + "_"*60)
    file_life.write("My Life\n\n")

    #use while loop
    yes_no = "y"
    input_num = 1    
    while yes_no == "y":
        # ask for user input
        user_input = input(f"\nEnter line {input_num}: ")
        # write the user input into mylife.txt
        file_life.write(f"Line #{input_num}: "+ user_input + "\n")
        # ask user if they have more lines to add
        ask_user = input("Are there more lines? y/n: ").lower()
        input_num += 1

        # if there is no line to be input
        if ask_user == "n":
            print("_"* 60)
            print("\nLoading loading loading........")
            print("Done! Your input is already in the text file.\n")
            exit()
        
    
        