import random
print("welcome to the number guessing game!")
number =random.randint(1,100)
attempts = 0
while True:
    try:
        guess = int(input("guess a number between 1 and 100: "))
        attempts +=1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")