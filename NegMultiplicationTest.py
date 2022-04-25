
from random import randint


#From 1-40  = Simple Fraciton Addition

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


correct_counter = 0
wrong_counter = 0

for m in range(75):
    a = 0
    b = 0
    c = randint(0, 1)
    if(m<=30):
        a = randint(0, 10)
        if(c==1):
            b=randint(-10, 1)
        else:
            b=randint(0, 10)
    elif(30<m<=60):
        a = randint(0, 99)
        #b = randint(20, 99)
        if(c==1):
            b=randint(-99, -20)
        else:
            b=randint(20, 99)
        
    elif(60<m<=75):
        a = randint(100, 999)
        #b = randint(100, 999)
        if(c==1):
            b=randint(-999,-100)
        else:
            b=randint(100, 999)

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





    
correctStr = "You got " + str(correct_counter) +" Correct!"
wrongStr = "You got " + str(wrong_counter) +" Wrong!"
print(correctStr)
print(wrongStr)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
EndTimeStr = "End Time: "+ str(current_time)
print(EndTimeStr)

writeToResultsFile("Test is: NegativeMultiplication",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)