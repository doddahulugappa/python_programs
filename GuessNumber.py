import random
counter = 1
flag = False
number_generated = random.randint(1,7)
print("Please  guess a number between 1 to 7; maximum attempts are 3")
while(True):
    if counter == 1:
        guessed_number = int(input("Guess:"))
        if guessed_number == number_generated:
            flag = True
            break
    else:
        guessed_number = int(input("\nYour guessed number is wrong, guess again:"))
        if guessed_number == number_generated:
            flag = True
            break


    if counter == 3:
        break

    counter += 1 # counter = counter + 1

if not flag:
    print("maximum guessing attempt reached! You have lost the game!\n actual number was ",number_generated)
else:
    print("You won the game in", counter, " Attempt !\n Actual number was", number_generated)






