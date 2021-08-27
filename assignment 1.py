import random
def main():
    #prompt the player for secret number
    secretnum = str(random.randint(1, 10000))
    print(secretnum)
    guess = 10
    score = 20

    print(f"The secret number is {len(secretnum)} numbers long")

    #loop through the code until number is guessed or you run out of guesses
    while guess > 0:
        wrong_pos = 0       #count number of wrong positions
        number_list = []
        guessnum = input("Guess the number: ")

        #check for invalid errors. user will not loose guesses for invalid inputs
        if len(guessnum) > len(secretnum) or \
            len(guessnum) < len(secretnum) or \
            guessnum.isnumeric() == False:
            print("invalid input")
            continue

        guess -= 1
        #create a list of correctly guessed numbers
        number_list = [num for num in guessnum if num in secretnum and num not in number_list]
        #break out of the loop once guessed num is equal to secretnumber
        if guessnum == secretnum:
            score += 5
            break
        else:
            score -= 2

        #count the number of  wrong positions.
        for number in number_list:
            if secretnum.index(number) != number_list.index(number):
                wrong_pos += 1

        #print formatted output as was given in the example program run
        printf(number_list, wrong_pos, guess)

    if guess > 0:
        print("\nCongrats! you guessed the right number")
        print("you got {} points".format(score))
    else:
        print("\nSorry you ran out of guesses")

    ans = input("Do you want to play again? (Yes/No)")
    if ans == "Yes" or ans == "yes" or ans == "y": main()
    else: return 0


def printf(numlist, position, guessnumber):
    print(f"{len(numlist)} digits: {numlist} guessed correctly.\n{position} numbers in wrong position")
    print(f"Turns remaining: {guessnumber}")
    print()

if __name__ == '__main__':
    main()
