# Set the minimum password length
minimum_length = 8


# Function to get the password from the user
def get_password():
    while True:
        password = input("Enter a password: ")
        if len(password) >= minimum_length:
            return password
        else:
            print(f"Password must be at least {minimum_length} characters long. Try again.")


# Function to print asterisks for a given password
def print_asterisks(password):
    print("Password is valid!")

    # Print asterisks for each character in the password
    for _ in password:
        print("*", end="")
    print()  # Print a newline to move to the next line


# Function to check password validity
def check_password():
    password = get_password()
    print_asterisks(password)


# Define the main function
def main():
    check_password()


# Call the main function
if __name__ == "__main__":
    main()
