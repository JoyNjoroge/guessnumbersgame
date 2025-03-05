import random
number = random.randint(1,51)
trials = 0
maxtrials = 10

while trials < maxtrials:
    x = int(input("Guess a number: "))
    if x == number:
        print("How did you get that! Spectacular!")
        break
    else:
        print("WRONG!!")
        trials +=1

if trials == maxtrials:
    print("Game over. Out of trials.")
    print(number)
