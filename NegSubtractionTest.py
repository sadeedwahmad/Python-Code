from random import randint


#From 1-20  = Simple Addition
#From 20-50 = Two Digit Addition
#From 50-60 = Three Digit Addition
#From 60-70 = Four Digit Addition
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)

#ADJUST THIS AND MAKE A PLAN 
#Make Him do this 3 times
#First Time do not raise difficulty after question 50
#Second Time do not raise the difficulty after question 60
#Thrid Time run the programme as designed

correct_counter = 0
wrong_counter = 0

for m in range(50,90):
    a = 0
    b = 0
    if(m<=20):
        a = randint(10, 20)
        b = randint(0, 10)
    elif(20<m<=50):
        a = randint(0, 99)
        b = randint(0, 99)
    elif(50<m<=60):
        a = randint(500, 999)
        b = randint(500, 999)
    elif(60<m<=75):
        a = randint(20, 999)
        b = randint(20, 999)
    elif(75<m<=90):
        a = randint(1000, 3000)
        b = randint(1000, 3000)
    print("Question number: " + str(m))
    print("What is: "+ str(a) + " - " + str(b))
    user_anwser = input("Enter Anwser: ")
    if(int(user_anwser) == a-b):
        print("Correct");
        correct_counter +=1 
    else:
        print("Wrong!")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(a) + " - " + str(b))
            user_anwser = input("Enter Anwser: ")
            if(int(user_anwser) == a-b):
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
