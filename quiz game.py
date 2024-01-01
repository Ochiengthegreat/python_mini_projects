score_count = 0
print("Welcome to my football quiz!")

playing = input("Do you want to play the quiz? ")

if playing.upper() != "YES":
    quit()
else:
    print("Okay! Let's play")

print("Question 1")
answer = input("Who has the most goals in Champions League history? ")
if answer.upper() == "CRISTIANO":
    print("Correct!")
    score_count += 1
elif answer.upper() == "RONALDO":
    print("Correct!")
    score_count += 1
else:
    print("Incorrect!")

print("Question 2")
answer = input("Who is the premier league all time top scorer? ")
if answer.upper() == "ALAN SHEARER":
    print("Correct!")
    score_count += 1
elif answer.upper() == "SHEARER":
    print("Correct!")
    score_count += 1
else:
    print("Incorrect!")

print("Question 3")
answer = input("Who is the la liga all time top scorer? ")
if answer.upper() == "MESSI":
    print("Correct!")
    score_count += 1
elif answer.upper() == "LIONEL MESSI":
    print("Correct!")
    score_count += 1
else:
    print("Incorrect!")

print("You got " + str(score_count) + " questions correct!")
print("You got " + str((score_count / 4) * 100) + "%")