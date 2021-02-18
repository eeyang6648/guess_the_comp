import time
import sys
import random
f=0
score=0
x=("...")
print("loading", (x[0]), (x[1]),(x[2]))
time.sleep(5)
print("importing system", (x[0]), (x[1]),(x[2]))
time.sleep(5)
if random.random()<0.50:
 print("imported successfully")
else:
        print("\033[5;31;400m failed to import\n")
        sys.exit(print("try again")) 
time.sleep(2)
print("if you want random name just type random")
time.sleep(1)
print("what is your name")
time.sleep(1)
user= input ("type here:")
if user==("random"):
        listname=("Mike", "Tom", "CJ", "Jessica", "Terry", "Jerry")
        randomname=random.choice(listname)
        print("hi", randomname)
if user!=("random"):
        print("hi" , user)

def start():
         v=0
         v+=1

         
         
         if v==1:
                 
                 
                  
                 password=("user1234")
                 print("entering security system", (x[0]), (x[1]),(x[2]))
                 time.sleep(3)
                 h1=input("enter password:")
                 


         if h1 != password:
                 print("loading", (x[0]), (x[1]),(x[2])) 
                 time.sleep(3)
                 print("entering main system")
                 time.sleep(5)
                 print(("\033[5;31;400m failed to access  \n"))
                 time.sleep(1)
                 print("\033[5;37;400m there is something wrong with your password\n")
                 time.sleep(1)
                 print("please try again")
                 time.sleep(1)
                 print("loading", (x[0]), (x[1]),(x[2]))
                 time.sleep(3)
                 sys.exit()

         if h1==password:
                         print("loading", (x[0]), (x[1]),(x[2]))
                         time.sleep(3)
                         print("entering main system")
                         time.sleep(5)
                         print("entered successfully")
                   
         

start()
start=("""
$$$$$$$$$$$$$$$$$$$$$$$
$$$guessing the comp$$$
$$$$$$$$$$$$$$$$$$$$$$$
""")
print(start)
time.sleep(5)
print("you only had a six tries in total")

time.sleep(1)
print("your mission is to guess what the computer is thinking")
time.sleep(2)
print("see if you are likely enough to get the same question over and over")
time.sleep(1)
print("ready")
time.sleep(3)
print("start")                    
while True in range(6):
        
 randomword=("ball", "rope", "books", "pen", "fan", "chair")
 t1=random.choice(randomword)
 if t1==("ball") :
  print ("hint: is something round and it is a sphere shape")
 if t1==("rope") :
  print("hint: it is something long or it can be short but is often needed for tug a war")
 if t1 == ("books"):
  print("hint: it is something educational and is often needed for english lessons")

 if t1=="pen":
  print("hint: it is something often needed to write essays when you are a secondary student")
 if t1==("fan"):
  print("hint: it is something to cool you down after a long run")
 if t1=="chair":
  print("hint: it is something most likely be in your house ")

 ans=input("guess what the word is: ")
 print("checking answer...")
 time.sleep(1)
 print("loading...")
 time.sleep(5)
      
 if ans==t1:
  print("correct you guess it")
  print("loading. . .")
  time.sleep(1)
  score+=1
  f+=1
  print("your score is at", score)
  time.sleep(3)
 if ans != t1:
  print("wrong try again")
  print("loading. . .") 
  time.sleep(1)
  print("your score is still at", score)
  f+=1
 if f == 6:
         if user==("random"):
                 sys.exit(print("final score =", score,"bye", randomname))

         if user!=("random"):
                 sys.exit(print("final score =", score, " bye ", user))


         


    
