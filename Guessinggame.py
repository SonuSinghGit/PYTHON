import random
number = random.randint(1, 100)
counut = 0
while True:
    try:       
        num = int(input("Guess a number between 1 and 100: "))
        counut += 1  
        if num == number:
            print("Congratulations You guessed the number in", counut, "guesses.")
            break
        elif num > number:
            print("Too high Try again.")
        else:
            print("Too low Try again.")
    except ValueError:  
        print("Invalid input. Please enter a valid integer.")
