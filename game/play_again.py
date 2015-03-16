try:
    input = raw_input
except NameError:
    pass

def play_again():
    p_a_choice = str(input("Play again? (y or n) "))
    while p_a_choice not in ["y", "n"]:
        print("Invalid Input")
        p_a_choice = str(input("Play again? (y or n) "))
    if p_a_choice == 'n':
        print("Goodbye")
        print("\n" * 55)
        return False
    elif p_a_choice == 'y':
        return True
