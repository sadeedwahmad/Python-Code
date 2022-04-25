from random import randint



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
    if(m<=20):
        a = randint(1, 10)
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

    c = a*b
    print("Question number: " + str(m))
    print("What is: "+ str(c) + "/" + str(b))
    user_answer = input("Enter answer: ")
    if(str(user_answer) == str(a)):
  
        print("\033[1;32m Correct!  \n")
        correct_counter +=1 
    else:
        print("\033[1;31;40m Wrong!  \n")
     
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(c) + "/" + str(b))
            user_answer = input("Enter answer: ")
            if(str(user_answer) == str(a)):
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


writeToResultsFile("Test is: Division",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)
