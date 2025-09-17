# 5 rounds
# display guesses, round num, winner
# find even or odd by integar division
from random import randint
cscore = 0
hscore = 0

print("Winner & Losers Game - Human is even, Computer is odd")

for rnd in range(1,6):
    print("Round:", rnd)
    hguess = int(input("Enter your guess (1-5): "))
    cguess = randint(1,5)
    print(f"Human Guess: {hguess} - Computer Guess: {cguess}")
    sum = hguess + cguess
    if sum % 2 != 0:
        print("Sum is Odd")
        cscore += 1
    else:
        print("Sum is Even")
        hscore += 1
    print(f"Human Score: {hscore} - Computer Score: {cscore}")
if hscore > cscore:
    print("Human Wins!")
else:
    print("Computer Wins!")