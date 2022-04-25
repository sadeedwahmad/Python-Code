from random import randint


#From 1-30  = Simple Mutliplication
#From 30-60 = Two Digit Mutliplication
#From 60-80 = Three Digit Mutliplication
from datetime import datetime
from ResultWriter import writeToResultsFile
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

correct_counter = 0
wrong_counter = 0

for m in range(70):
    a = 0
    b = 0
    if(m<=30):
        a = randint(0, 10)
        b = randint(1, 10)

    elif(30<m<=50):
        a = randint(0, 99)
        b = randint(20, 99)
        
    elif(50<m<70):
        a = randint(100, 999)
        b = randint(100, 999)

    print("Question number: " + str(m))
    print("What is: "+ str(a) + " X " + str(b))
    user_anwser = input("Enter Anwser: ")
    if(str(user_anwser) == str(a*b)):
        print("\033[1;32m Correct!  \n")
        correct_counter +=1 
    else:
        print("\033[1;31;40m Wrong!  \n")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(a) + " X " + str(b))
            user_anwser = input("Enter Anwser: ")
            if(str(user_anwser) == str(a*b)):
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


writeToResultsFile("Test is: Multiplication",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)