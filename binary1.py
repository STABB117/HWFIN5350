print("Think of a whole number between 1 and 100. I will attempt to guess it in 7 tries or less. I will guess, and then I will need you to tell me if my guess is 'too high', 'too low', or 'correct'.")
higher = 101 
lower = 0
tries = 1
while higher > lower:
    if tries < 8:
        guess = ((higher + lower)//2)
        print("My guess is ", guess)
        response = input()
        if response == "too high":
            higher = guess
        if response == "too low":
            lower = guess
        if response == "correct":
            print("I win!")
            break
        tries +=1
    else:
        print("I lose.")
        break