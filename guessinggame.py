import random

print("Number Guessing Game :)")

Answer = random.randint(1, 9)
guesses = 0
print("which number is it? what answer is fine? all i know is its in between 1-9")
while guesses < 5:
    guess= int(input("put your answer here:"))
    if guess==Answer:
        print("you did it! you won!")
        break
    elif guess < Answer:
        print(guess ," is too smol")
    else:
        print(guess ,"? dats to beeg")
    guesses+=1

if not guesses < 5:
    print("well gosh diddly darn.", Answer, "was the right Answer")