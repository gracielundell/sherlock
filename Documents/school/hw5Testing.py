



def shift():
    move = int(input("How many values would you like to shift the code? "))
    while move <= 0:
        print("Sorry that is not a valid number. Please try again.")
        move = int(input("What is the shift value that you would like to use?: "))    
    letter = "A"
    # encrypt
    letterNum = ord(letter) # ord give ASCII value, then can use this to +/-
    letterNum += move
    letterWrite = chr(letterNum)
    print(letterWrite)

def main():
    choice = input("Would you like to encrypt or decrypt a file? (e/d): ")
    while choice != "d" and choice != "e":
        print("Sorry that is not a valid option. Please try again.")
        choice = input("Would you like to encrypt or decrypt a file? (e/d): ")
        if choice == "d":
            print("poop")
        elif choice == "e":
           encrypt(shift())
    shift()
    

main()

