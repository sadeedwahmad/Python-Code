from random import randint
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)



correct_counter = 0
wrong_counter = 0
#ADJUST THIS AND MAKE A PLAN 
#First Lvl: Make him do the easy ones for all 70 questions
#Second Lvl: Make him do the midLevel ones after question 20
#Third Lvl: Make him do the medium ones after question 40
#Fourth Lvl: Make him do the programme as designed
for m in range(70):
    a = 0
    b = 0
    c = randint(0, 1)
    if(m<=20):
        a = randint(0, 10)
        if(c==1):
            b=randint(-10,-1)
        else:
            b = randint(1, 10)
    
    elif(20<m<=40):
        a = randint(10, 50)
        if(c==1):
            b= randint(-15,-1) 
        else:
            b = randint(1, 15)
    elif(40<m<=60):
        a = randint(100, 700)
        if(c==1):
            b=randint(-20,-1)
        else:
            b = randint(1, 20)
        
    elif(60<m<=70):
        a = randint(150, 1000)
        if(c==1):
            b=randint(-50,-10)
        else:
            b = randint(10, 50)

    c = a*b
    print("Question number: " + str(m))
    print("What is: "+ str(c) + "/" + str(b))
    user_anwser = input("Enter Anwser: ")
    if(int(user_anwser) == c/b):
        print("Correct");
        correct_counter +=1 
    else:
        print("Wrong!")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(c) + "/" + str(b))
            user_anwser = input("Enter Anwser: ")
            if(int(user_anwser) == c/b):
                print("Correct");
                
                stuck = False
            else:
                print("Wrong!")
                wrong_counter +=1





    

print("You got " + str(correct_counter) +" Correct!")
print("You got " + str(wrong_counter) +" Wrong!")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("End Time =", current_time)
