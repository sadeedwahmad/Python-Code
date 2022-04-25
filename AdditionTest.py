from random import randint

from ResultWriter import writeToResultsFile
#From 1-20  = Simple Addition
#From 20-50 = Two Digit Addition
#From 50-60 = Three Digit Addition
#From 60-70 = Four Digit Addition
from datetime import datetime
from datetime import date

today = date.today()
# Textual month, day and year	
todayDate = "Date: " +  today.strftime("%B %d, %Y")
print(todayDate)


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
startTimeStr = "Start Time ="+ str(current_time)
print(startTimeStr)

#ADJUST THIS AND MAKE A PLAN 
#Make Him do this 3 times
#First Time do not raise difficulty after question 50
#Second Time do not raise the difficulty after question 60
#Thrid Time run the programme as designed

correct_counter = 0
wrong_counter = 0

for m in range(80):
    a = 0
    b = 0
    if(m<=20):
        a = randint(0, 10)
        b = randint(0, 10)
    elif(20<m<=50):
        a = randint(0, 99)
        b = randint(20, 99)
    elif(50<m<=60):
        a = randint(100, 999)
        b = randint(100, 999)
    elif(60<m<=80):
        a = randint(1000, 3000)
        b = randint(1000, 3000)
    print("Question number: " + str(m))
    print("What is: "+ str(a) + " + " + str(b))
    user_answer = input("Enter answer: ")
    if(str(user_answer) == str(a+b)):
        print("\033[1;32m Correct!  \n")
        correct_counter +=1 
    else:
        print("\033[1;31;40m Wrong!  \n")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(a) + " + " + str(b))
            user_answer = input("Enter answer: ")
            if(str(user_answer) == str(a+b)):
                print("\033[1;32m Correct!  \n")
                
                stuck = False
            else:
                print("\033[1;31;40m Wrong!  \n")
                wrong_counter +=1
        
correctStr = "You got " + str(correct_counter) +" Correct!"
wrongStr = "You got " + str(wrong_counter) +" Wrong!"
print(correctStr)
print(wrongStr)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
EndTimeStr = "End Time: "+ str(current_time)
print(EndTimeStr)





writeToResultsFile("Test is: Addition",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)
