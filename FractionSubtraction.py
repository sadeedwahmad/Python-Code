
from random import randint
from fractions import Fraction

#From 1-40  = Simple Fraciton Addition

from datetime import datetime
from ResultWriter import writeToResultsFile
from datetime import date

today = date.today()
# Textual month, day and year	
todayDate = "Date: " +  today.strftime("%B %d, %Y")
print(todayDate)
#ADJUST THIS AND MAKE A PLAN 

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
startTimeStr = "Start Time ="+ str(current_time)
print(startTimeStr)


correct_counter = 0
wrong_counter = 0


for m in range(40):
    ##answer = a/b + c/d
    a = randint(0, 10) #numerator
    c = randint(0, 10) #numerator
    b = randint(1, 10) #denomenator
    d = randint(1, 10) #denomenator

    print("Question number: " + str(m))
    ab_bigger=False
    real_answer = " "
    if(a*d> b*c):
        ab_bigger = True
    if(ab_bigger):
        print("What is: "+ str(a) + "/" + str(b) + " - " + str(c)  + "/" + str(d))
        real_answer = Fraction(a,b)-Fraction(c,d)
   
    else:
         print("What is: "+ str(c) + "/" + str(d) + " - " + str(a)  + "/" + str(b))
         real_answer = Fraction(c,d)-Fraction(a,b)
    user_answer = input("Enter answer: ")

    if(str(user_answer) == str(real_answer)):
        print("\033[1;32m Correct!  \n")
        correct_counter +=1 
    else:
        print("\033[1;31;40m Wrong!  \n")
        print(real_answer)
       # print("Correct answer is meant to be: " + str(real_answer))
        wrong_counter +=1
        stuck = True
        while(stuck):
            if(ab_bigger):
                print("What is: "+ str(a) + "/" + str(b) + " - " + str(c)  + "/" + str(d))
            else:
                print("What is: "+ str(c) + "/" + str(d) + " - " + str(a)  + "/" + str(b))
            user_answer = input("Enter answer: ")
            if(str(user_answer) == str(real_answer)):
                print("\033[1;32m Correct!  \n")
                stuck = False
            else:
                print("\033[1;31;40m Wrong!  \n")
               # print(str(real_answer))
                wrong_counter +=1

     
correctStr = "You got " + str(correct_counter) +" Correct!"
wrongStr = "You got " + str(wrong_counter) +" Wrong!"
print(correctStr)
print(wrongStr)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
EndTimeStr = "End Time: "+ str(current_time)
print(EndTimeStr)

writeToResultsFile("Test is: Fraction_Subtraction",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)