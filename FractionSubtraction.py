#Fraction Subtraction Non negative

from random import randint


#From 1-40  = Simple Fraciton Addition

from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)

#ADJUST THIS AND MAKE A PLAN 


correct_counter = 0
wrong_counter = 0
print("Example: Question 5/2 - 3/4  = 5*4/2*4 - 3*2/2*4 = 20/8 - 15/8 = 5/8")
print("a/b - c/d  = (a*d - c*b)/(b*d)")
print("You do NOT need to simplify // You do NOT need to simplify //You do NOT need to simplify //You do NOT need to simplify //You do NOT need to simplify //You do NOT need to simplify //")
for m in range(40):
    ##Anwser = a/b + c/d
    a = randint(0, 10) #numerator
    c = randint(0, 10) #numerator
    b = randint(1, 10) #denomenator
    d = randint(1, 10) #denomenator

    print("Question number: " + str(m))
    ab_bigger=False
    if(a*d> b*c):
        ab_bigger = True
    if(ab_bigger):
        print("What is: "+ str(a) + "/" + str(b) + " - " + str(c)  + "/" + str(d))
    else:
         print("What is: "+ str(c) + "/" + str(d) + " - " + str(a)  + "/" + str(b))
    user_anwser = input("Enter Anwser: ")
    if(b==d):
        if(ab_bigger):
            real_anwser = str(a-c) + "/" + str(d) 
        else:
            real_anwser = str(c-a) + "/" + str(d) 
    else: 
        if(ab_bigger):
            real_anwser = str(a*d-c*b) + "/" + str(b*d) 
        else:
            real_anwser = str(c*b-a*d) + "/" + str(b*d) 
    if(user_anwser == real_anwser):
        print("Correct");
        correct_counter +=1 
    else:
        print("Wrong!")
       # print("Correct Anwser is meant to be: " + str(real_anwser))
        wrong_counter +=1
        stuck = True
        while(stuck):
            if(ab_bigger):
                print("What is: "+ str(a) + "/" + str(b) + " - " + str(c)  + "/" + str(d))
            else:
                print("What is: "+ str(c) + "/" + str(d) + " - " + str(a)  + "/" + str(b))
            user_anwser = input("Enter Anwser: ")
            if(user_anwser == real_anwser):
                print("Correct");
                stuck = False
            else:
                print("Wrong!")
               # print(str(real_anwser))
                wrong_counter +=1

     
print("You got " + str(correct_counter) +" Correct!")
print("You got " + str(wrong_counter) +" Wrong!")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("End Time =", current_time)
