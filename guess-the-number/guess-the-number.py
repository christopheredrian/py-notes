import random

print("Select difficulty (easy, medium, hard): ", end='')
difficulty = input()
# difficulty = "easy"

difficulty_map = {
    'easy': 100,
    'medium': 500,
    'hard': 1000,
}

max_number_of_guesses = 10

print("Difficulty", difficulty)
max_number = difficulty_map[difficulty]

print("The number is between 1 and {}".format(max_number))

the_random_integer = random.randint(1, max_number)
number_of_guesses = 0

while True:
    print("Guess: ", end='')
    guess = int(input())

    if guess == the_random_integer:
        print("You got it!")
        break
    else:
        if number_of_guesses >= max_number_of_guesses:

            print("No more tips for you! I'm gonna change the number :P ")
            the_random_integer = random.randint(1, max_number)
            number_of_guesses = 0

        else:

            print("\nYou have {} chances left before I change the number".format(
                max_number_of_guesses - number_of_guesses))

            if guess > the_random_integer:
                print("It's lower than {0}".format(guess))
            else:
                print("Its Higher than {0}".format(guess))

    number_of_guesses += 1

print("Thanks!")
