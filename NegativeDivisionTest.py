
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
#ADJUST THIS AND MAKE A PLAN 
#First Lvl: Make him do the easy ones for all 70 questions
#Second Lvl: Make him do the midLevel ones after question 20
#Third Lvl: Make him do the medium ones after question 40
#Fourth Lvl: Make him do the programme as designed
for m in range(70):
    a = 0
    b = 0
    c = randint(0, 1)
    d = randint(0, 1)
    if(m<=20):
        a = randint(0, 10)
        b = randint(1, 10)
        
    
    elif(20<m<=40):
        a = randint(10, 50)
        b = randint(1, 15)
    elif(40<m<=60):
        a = randint(100, 700)
        b = randint(1, 20)
        
    elif(60<m<=70):
        a = randint(150, 1000)
        b = randint(10, 50)
    if(c==1):
        a=-a
    if(d==1):
        b=-b
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





    

correctStr = "You got " + str(correct_counter) +" Correct!"
wrongStr = "You got " + str(wrong_counter) +" Wrong!"
print(correctStr)
print(wrongStr)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
EndTimeStr = "End Time: "+ str(current_time)
print(EndTimeStr)

writeToResultsFile("Test is: NegativeDivision",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)
