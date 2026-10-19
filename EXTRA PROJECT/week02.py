"""Week 2: Decisions and Loops programming problems.

Run this file and choose a task from the menu. Each task is kept in its own
function so it can also be run independently.
"""

import random


def password_strength():
    password = input("Enter a password: ")
    if len(password) >= 12:
        print("Strong")
    elif len(password) >= 8:
        print("Moderate")
    else:
        print("Weak")

#%%
def multiplication_quiz():
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    answer = int(input(f"What is {number1} * {number2}? "))
    if answer == number1 * number2:
        print("Correct!")
    else:
        print(f"Incorrect. The answer is {number1 * number2}.")


def even_or_odd():
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def bmi():
    pounds = float(input("Enter weight in pounds: "))
    inches = float(input("Enter height in inches: "))
    if pounds <= 0 or inches <= 0:
        print("Weight and height must be greater than zero.")
        return

    kilograms = pounds * 0.45359237
    metres = inches * 0.0254
    bmi = kilograms / (metres ** 2)

    if bmi < 18.5:
        interpretation = "Underweight"
    elif bmi < 25.0:
        interpretation = "Normal"
    elif bmi < 30.0:
        interpretation = "Overweight"
    else:
        interpretation = "Obese"
    print(f"BMI: {bmi:.2f} ({interpretation})")


def negative_numbers():
    for number in range(-10, 0):
        print(number)


def number_pattern():
    for end in range(1, 6):
        for number in range(1, end + 1):
            print(number, end=" ")
        print()


def sum_to_n():
    n = int(input("Enter the value n: "))
    if n < 1:
        print("Please enter a positive integer.")
        return
    total = 0
    for number in range(1, n + 1):
        total += number
    print(f"The sum of all numbers until {n} is {total}")


def multiplication_table():
    number = int(input("Enter a number: "))
    for multiplier in range(10):
        print(f"{multiplier} x {number} = {multiplier * number}")


def multiplication_grid():
    for row in range(10):
        print(" ".join(f"{row * column:>2}" for column in range(10)))


def dog_years():
    human_years = float(input("Enter human years: "))
    if human_years < 0:
        print("Human years cannot be negative.")
    elif human_years <= 2:
        print(f"{human_years:g} human years is {human_years * 10.5:g} dog years.")
    else:
        dog_years = 2 * 10.5 + (human_years - 2) * 4
        print(f"{human_years:g} human years is {dog_years:g} dog years.")


def vowel_or_consonant():
    letter = input("Enter a letter: ").strip().lower()
    if len(letter) != 1 or not letter.isalpha() or not letter.isascii():
        print("Please enter one letter of the alphabet.")
    elif letter in "aeiou":
        print(f"{letter} is a vowel.")
    elif letter == "y":
        print("Sometimes y is a vowel, and sometimes y is a consonant.")
    else:
        print(f"{letter} is a consonant.")


def reverse_pattern():
    for start in range(5, 0, -1):
        for number in range(start, 0, -1):
            print(number, end=" ")
        print()


def highest_score():
    count = int(input("Enter the number of students: "))
    if count < 1:
        print("There must be at least one student.")
        return
    highest_name = ""
    highest_score = float("-inf")
    for student in range(count):
        name = input(f"Enter student {student + 1}'s name: ")
        score = float(input(f"Enter {name}'s score: "))
        if score > highest_score:
            highest_name = name
            highest_score = score
    print(f"Highest score: {highest_name} with {highest_score:g}")


def guessing_game():
    secret = random.randint(1, 100)
    tries = 0
    print("Guess the secret number (between 1 and 100).")
    while True:
        guess = int(input("Your guess: "))
        tries += 1
        if guess < secret:
            print("Too small.")
        elif guess > secret:
            print("Too large.")
        else:
            print(f"Correct! You guessed it in {tries} {('try' if tries == 1 else 'tries')}.")
            break


def two_digit_lottery():
    lottery = f"{random.randint(10, 99)}"
    guess = input("Enter a two-digit number: ").strip()
    if len(guess) != 2 or not guess.isdigit():
        print("Please enter exactly two digits.")
        return

    if guess == lottery:
        prize = 10000
        message = "Exact match"
    elif sorted(guess) == sorted(lottery):
        prize = 3000
        message = "Both digits match"
    elif any(digit in lottery for digit in guess):
        prize = 1000
        message = "One digit matches"
    else:
        prize = 0
        message = "No match"
    print(f"Lottery number: {lottery}")
    print(f"{message}. You win £{prize:,}.")


def three_digit_lottery():
    lottery = f"{random.randint(100, 999)}"
    guess = input("Enter a three-digit number: ").strip()
    if len(guess) != 3 or not guess.isdigit():
        print("Enter three digits.")
        return

    if guess == lottery:
        prize = 10000
        message = "Exact match"
    elif sorted(guess) == sorted(lottery):
        prize = 3000
        message = "All three digits match"
    elif any(digit in lottery for digit in guess):
        prize = 1000
        message = "At least one digit matches"
    else:
        prize = 0
        message = "No match"
    print(f"Lottery number: {lottery}")
    print(f"{message}. You win £{prize:,}.")


def two_highest_scores():
    count = int(input("Enter the number of students: "))
    if count < 2:
        print("Enter at least two students to find the top two scores.")
        return
    highest = float("-inf")
    second_highest = float("-inf")
    for student in range(count):
        score = float(input(f"Enter student {student + 1}'s score: "))
        if score > highest:
            second_highest = highest
            highest = score
        elif score > second_highest:
            second_highest = score
    print(f"Highest score: {highest:g}")
    print(f"Second highest score: {second_highest:g}")


def password_cracker():
    actual = input("Enter the actual password: ")
    guess = input("Enter the password guess: ")
    if not actual:
        print("The actual password cannot be empty.")
        return
    matching_positions = sum(
        actual[index] == guess[index]
        for index in range(min(len(actual), len(guess)))
    )
    accuracy = matching_positions / len(actual) * 100
    if guess == actual:
        print("Password cracked!")
    else:
        print(f"Accuracy: {accuracy:.0f}%")


TASKS = {
    1: ("Password strength checker", password_strength),
    2: ("Multiplication quiz", multiplication_quiz),
    3: ("Even or odd", even_or_odd),
    4: ("BMI", bmi),
    5: ("Negative numbers", negative_numbers),
    6: ("Number pattern", number_pattern),
    7: ("Sum of numbers from 1 to n", sum_to_n),
    8: ("Multiplication table", multiplication_table),
    9: ("Multiplication table grid", multiplication_grid),
    10: ("Dog years", dog_years),
    11: ("Vowel or consonant", vowel_or_consonant),
    12: ("Reverse number pattern", reverse_pattern),
    13: ("Find the highest score", highest_score),
    14: ("Guessing game", guessing_game),
    15: ("Two-digit lottery", two_digit_lottery),
    16: ("Three-digit lottery", three_digit_lottery),
    17: ("Find the two highest scores", two_highest_scores),
    18: ("Password cracker", password_cracker),
}


def main():
    while True:
        print("\nWeek 2 - Decisions and Loops")
        for number, (name, _) in TASKS.items():
            print(f"{number:2}. {name}")
        print(" 0. Exit")
        choice = input("Choose a task (0-18): ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        if not choice.isdigit() or int(choice) not in TASKS:
            print("Please choose a number from 0 to 18.")
            continue

        print()
        TASKS[int(choice)][1]()


if __name__ == "__main__":
    main()
