# Set the minimum password length
minimum_length = 8

# Initialize a variable to keep track of whether the password is valid
is_valid = False

while not is_valid:
    # Ask the user for a password
    password = input("Enter a password: ")

    # Check if the password meets the minimum length requirement
    if len(password) >= minimum_length:
        is_valid = True
        print("Password is valid!")

        # Print asterisks for each character in the password
        i = 0
        while i < len(password):
            print("*", end="")
            i += 1
        print()  # Print a newline to move to the next line
    else:
        print(f"Password must be at least {minimum_length} characters long. Try again.")
