##python guesses the number
print( "Let's play a guessing game. I bet that if you choose a number between 1 and 100, I can guess it correctly within 7 tries.")

print("I will try to guess your number. To do so, I will need you to tell me if my guess is too high, too low, or If I guessed the number correctly.")

print("These are the responses that I can recognize: 'too high', 'too low', and 'correct'.")


print("My first guess is 50")

guesses = 1
guess = 50
difference = 25

while guesses <= 7:
    response = input()
    if response == "too high":
        guess = guess - difference
        print("My next guess is ", guess)
    
    elif response == "too low":
        guess = guess + difference
        print ("My next guess is ", guess)
    
    elif response == "correct":
        print("I win!")
        break
    difference = round((difference + .0001) /2)
    guesses += 1
