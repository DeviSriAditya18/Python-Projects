print('Welcome to my computer quiz')

playing=input("Do u want to play?")

if playing.lower()!="yes" :
    quit()

print("OK! Let's play:")

score=0

answer=input("What does CPU stand for? ")
if(answer.lower()=="central processing unit"):
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer=input("What does GPU stand for? ")
if(answer.lower()=="graphics processing unit"):
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer=input("What does RAM stand for? ")
if(answer.lower()=="random access memory"):
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got {} marks.".format(score))
print("You got {} percentage.".format((score/3)*100))
