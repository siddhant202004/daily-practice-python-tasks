#Create a number guessing game using loops and functions.
import random
numbers = random.randint(1,21)
print("Note : for winning the price you only have 7 chance to win the game.")
for i in range(1,8):
    try:
        Guess = int(input("Guess a number between 1-20 : "))
        
    except ValueError: 
        print("Enter a number between 1-20: ")
        continue
    if Guess < 1 or Guess > 20:
        print("Please enter a number between 1 and 20.")
        continue

    elif Guess==numbers:
        print("Your guess is correct")
        break
    else:
        print("Your guess was wrong, try again")
else:
    print(f"The Correct Number is {numbers}")  
