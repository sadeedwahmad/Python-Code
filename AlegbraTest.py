# generate random integer values

from random import randint



#def function get_anwser(a,b,c,d,x):
 #anwser = (a * x**3) + (b * x**2) + (c*x) +d
 #print(anwser)
    #return anwser

def get_anwser(a,b,c,d,x):
  return (a * x**3) + (b * x**2) + (c*x) + d

def get_working(a,b,c,d,x):
  return "[" + str(a) + "("+ str(x) + "^3): " + str((a * x**3)) + "]+ " + "[" + str(b) + "("+ str(x) + "^2): "+ str((b * x**2)) +   "]+ " +  "[" + str(c) + "("+ str(x) + "): "+ str((c*x)) + "]+ " + str(d) + " = " + str(get_anwser(a,b,c,d,x))
 
def get_question(a,b,c,d,x):
  return "y = " + str(a) + "(x^3) + "  + str(b) + "(x^2) + " + str(c) + "(x) + " + str(d) + " WHEN X = " + str(x)



# generate some integers



for m in range(5):
  a = randint(0, 10)
  b = randint(0, 10)
  c = randint(0, 10)
  d = randint(0, 10)
  x = randint(-10, 10)
  print("Question Number: "+ str(m))
  print(get_question(a,b,c,d,x))
  user_anwser = input("Enter Anwser: ")
  real_anwser =  get_anwser(a,b,c,d,x)
  if(int(user_anwser) == real_anwser):
     print("Correct")
  else:
    
    print("Wrong, The Anwser is:" + get_working(a,b,c,d,x) )
 


##print(get_anwser(a,b,c,d,x))


#a(x^3) + b(x^2) + c(x) + d


