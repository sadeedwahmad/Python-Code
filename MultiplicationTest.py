from random import randint


#From 1-30  = Simple Mutliplication
#From 30-60 = Two Digit Mutliplication
#From 60-80 = Three Digit Mutliplication
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)


#ADJUST THIS AND MAKE A PLAN 

correct_counter = 0
wrong_counter = 0

for m in range(75):
    a = 0
    b = 0
    if(m<=30):
        a = randint(0, 10)
        b = randint(1, 10)

    elif(30<m<=60):
        a = randint(0, 99)
        b = randint(20, 99)
        
    elif(60<m<=75):
        a = randint(100, 999)
        b = randint(100, 999)

    print("Question number: " + str(m))
    print("What is: "+ str(a) + " X " + str(b))
    user_anwser = input("Enter Anwser: ")
    if(int(user_anwser) == a*b):
        print("Correct");
        correct_counter +=1 
    else:
        print("Wrong!")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(a) + " X " + str(b))
            user_anwser = input("Enter Anwser: ")
            if(int(user_anwser) == a*b):
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
