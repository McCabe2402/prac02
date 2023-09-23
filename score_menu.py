def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_result(score):
    if score >= 70:
        print("Congratulations, you passed!")
    else:
        print("Sorry, you failed.")


def show_stars(score):
    print("*" * score)


def main():
    print("Welcome to Score Program!")

    choice = ''
    while choice != 'Q':
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Please select an option: ").strip().upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            if 'score' not in locals():
                print("You need to get a valid score first.")
            else:
                print_result(score)
        elif choice == 'S':
            if 'score' not in locals():
                print("You need to get a valid score first.")
            else:
                show_stars(score)
        elif choice == 'Q':
            print("Farewell! Thanks for using the Score Program.")
        else:
            print("Invalid choice. Please select a valid option (G/P/S/Q).")


if __name__ == "__main__":
    main()
