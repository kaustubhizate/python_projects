print("Welcome to Quiz Game")

playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# print("You got " + str('score') + " questions correct!")
print("You got " + (score / 4) * 100 + "%.")

if score == 4:
    print("You got a perfect score!")

elif score == 3:

    print("You got a good score!")

elif score == 2:


    print("You got a decent score!")

elif score == 1:

    print("You got a bad score!")

elif score == 0:

    print("You got a terrible score!")
    print("You should study more!")

