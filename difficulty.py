import time

# Helps with Python 3.x compatibility
try:
    input = raw_input
except NameError:
    pass

# Choose the difficulty
def difficulty():
    print("  1.  EASY")
    print("  2.  HARD")

    # Makes sure the input is either 1 or 2 and then return 'E' for EASY and 'H' for Hard
    d_choice = input("What difficulty would like? ")
    while d_choice.isdigit() == False or int(d_choice) not in [1,2]:
        print("Invalid Input")
        d_choice = input("What difficulty would like? ")
    if int(d_choice) in [1,2]:
        if int(d_choice) == 1:
            print("You have chosen EASY")
            time.sleep(1.5)
            return "E"
        elif int(d_choice) == 2:
            print("You have chosen HARD")
            time.sleep(1.5)
            return "H"
    
