
from random import randint


#From 1-40  = Simple Fraciton Addition

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)

#ADJUST THIS AND MAKE A PLAN 


correct_counter = 0
wrong_counter = 0

for m in range(40):
    ##Anwser = a/b + c/d
    a = randint(0, 10) #numerator
    c = randint(0, 10) #numerator
    b = randint(0, 10) #denomenator
    d = randint(0, 10) #denomenator

    print("Question number: " + str(m))
    print("What is: "+ str(a) + "/" + str(b) + " + " + str(c)  + "/" + str(d))
  
    user_anwser = input("Enter Anwser: ")
    if(b ==d):
        real_anwser = str(a+c) + "/" + str(d) 
    else: 
         real_anwser = str(a*d+c*b) + "/" + str(b*d) 
    if(user_anwser == real_anwser):
        print("Correct");
        correct_counter +=1 
    else:
        print("Wrong!")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(a) + "/" + str(b) + " + " + str(c)  + "/" + str(d))
            user_anwser = input("Enter Anwser: ")
            if(user_anwser == real_anwser):
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
