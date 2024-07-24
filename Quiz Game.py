print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play")
score = 0
questions_answered = 0

answer = input("""What does CPU stand for? 
""")
questions_answered += 1
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("That's incorrect.")

answer = input("""What does GPU stand for? 
""")
questions_answered += 1
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("That's incorrect.")

answer = input("""What does RAM stand for? 
""")
questions_answered += 1
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("That's incorrect.")

print("That's all! Thank you for playing!")
print(f"You received {score} out of {questions_answered} points")