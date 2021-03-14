from exp_tracker_func import add, choices, clear, view_expenses



def main():
    print("\tE X P E N S E  T R A C K E R")
    print("\t============================")

    while True:
        choices()
        choice = input("> ")

        if choice == "1":
            add()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("DETAILED VIEW, EDIT DATA, UPDATE & DELETE")
        elif choice == "4":
            clear()
        elif choice == "5":
            print("G O O D  B Y E")
            break
        else:
            print("Invalid!!!! Read the prompt and enter a valid input")


    
if __name__ == "__main__":
    main()
