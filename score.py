import random


def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    user_result = determine_score_result(score)
    print(f"User Result: {user_result}")

    # Generate a random score between 0 and 100
    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random Score: {random_score}")
    print(f"Random Result: {random_result}")


if __name__ == "__main__":
    main()
