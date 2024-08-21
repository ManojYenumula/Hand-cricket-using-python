import random

# it  is batting function 
# explained clearly in below
#it runs the function unitil batter out then it returns total runs 
#these total runs used in future operations by calling function

def user_batting():
    runs = 0
    ball = 1
    total_runs = 0
    while runs != ball:
        while True:
            runs = input("\nScore runs between 1 to 6: ")
            if runs not in("1","2","3","4","5","6"):
                print("\nINVALID RUNS .PLZ ENTER NUMBERS BETEEN 1 TO 6")
            else:
                break
        runs=int(runs)
        ball = random.randint(1, 6)
        if ball!=runs:
         total_runs += runs
         print("\nComputer ball:", ball)
         print("\nYOUR TOTAL SCORE IS:", total_runs)
        else:
         print("\n\n :(---------YOU ARE OUT------:(")
         print("\ncomputer ball:",ball)
         return total_runs
 
"""it is bowling function same like as batting function with small diifrences"""                     
           
def user_bowling():
  ball=1
  runs=0
  total_runs=0
  while ball!=runs:
    while True:
       ball=input("\n guess computer runs in next ball:")
       if ball not in("1","2","3","4","5","6"):
        print("\nINAVLID GUESS PLZ GUESS NUMBER BETWEEN 1 TO 6")
       else:
        break
           
    ball=int(ball)       
    runs=random.randint(1,6)
    if ball!=runs:
     total_runs +=runs
     print("\ncomputer scored runs in ball:",runs)
     print("\nCOMPUTER SCORED TOTAL RUNS",total_runs)
    else:
      print("\n\n:)----------COMPUTER IS OUT----------:)")
      print("\ncomputer scored runs in ball:",runs)
      return total_runs
      
      
     
 #if user batting in second innings
 
def user_batting2():
    runs = 0
    ball = 1
    total_runs = 0
    while runs != ball:
        while True:
            runs = input("\nScore runs between 1 to 6: ")
            if runs not in ("1", "2", "3", "4", "5", "6"):
                print("\nInvalid runs. Please enter a number between 1 and 6.")
            else:
                break
        runs = int(runs)
        ball = random.randint(1, 6)
        if ball != runs:
            total_runs += runs
            print("\nComputer ball:", ball)
            print("\nYour score is:", total_runs)
            if total_runs >com_runs:
                return total_runs
                break
        else:
            print("\nYou are out")
            print("\nComputer ball:", ball)
            return total_runs
 
 
 #if user bowling in second innings
 
def user_bowling2():
 ball=1
 runs=0
 total_runs=0
 while ball!=runs:
   while True:
       ball=input("\n guess computer runs in next ball:")
       if ball not in("1","2","3","4","5","6"):
           print("\ninvalid guess.plz enter guess between  1 to 6")
       else:
           break
           
   ball=int(ball)       
   runs=random.randint(1,6)
   if ball!=runs:
    total_runs +=runs
    print("\ncomputer scored runs in ball:",runs)
    print("\ncomputer scored total runs:",total_runs)
    if total_runs>user_runs:
    	return total_runs
    	break
   else:
     print("\ncomputer is out")
     print("\nucomputer scored runs in ball:",runs)
     return total_runs
 
 
     
#it taken input from user odd or even for toss

while True:
 toss=input("\nchoose even or odd for toss:").lower()
 if toss not in (["even","odd"]):
   print("\nINVALID INPUT PLZ ENTER ODD OR EVEN")
 else:
   break
print("\n you choosen:",toss)


#it takes number input between 1 to 6 for toss result

while True:
 user_choice=input("\nenter number between 1 to 6: ")
 if user_choice not in("1","2","3","4","5","6"):
 	print("\nINAVLID TOSS NUM.PLZ CHOOSE BETWEEN 1 TO 6")
 else:
 	break
user_choice=int(user_choice)
print ("\nuser choicen number:",user_choice)

com_choice=random.randint(1,6)
print("\ncomputer choosed number:",com_choice)
print("\n sum of",user_choice,"+",com_choice,"=",user_choice+com_choice)


#this block decides the the toss odd or even

total=user_choice+com_choice
if total%2==0:
	result="even"
else:
	result="odd"
print("\n toss result is is:",result)


#this block decides the toss winner

if toss==result:
 print("\nyou won the toss")
 
 
#it take input from user for bat ot bowl option 

 while True:
  user_option=input("\noption to bat or bowl:").lower() 
  if user_option not in(["bat","bowl"]):
   print ("\nINAVLID INPUT PLZ CHOOSE BAT OR BALL")
  else:
   break
   
  
 #if you select batting below block excuted
#we call above defined function here for batting and bowling operations   
   
 if user_option=="bat":
  print("\nyou selected batting\n\ncomputer is bowling")
  user_runs=user_batting()
  print("\n\nFINAL RUNS YOU SCORED:",user_runs)
  print("\n\nNow computer is batting")
  com_runs=user_bowling2()
  print("\n\nFINAL RUNS COMPUTER SCPRED:",com_runs)
  if com_runs>user_runs:
   print("\n\n************COMPUTER WON THE MATCH************")
  elif com_runs<user_runs:
   print("\n\n***********YOU WON THE MATCH***********")
  else:
   print("\n\n***********MATCH DRAWN*******")
 
 
#if you select bowling this block will excuted
 
 
 else:
  print("\nyou selected bowlling\n\ncomputer is battimg")
  com_runs=user_bowling()
  print("\n\nFINAL RUNS COMPUTER SCORED:",com_runs)
  print("\n\nNow you are batting")
  user_runs=user_batting2()
  print("\n\nFINAL RUNS you SCORED:",user_runs)
  if com_runs>user_runs:
   print("\n\n************COMPUTER WON THE MATCH************")
  elif com_runs<user_runs:
   print("\n\n***********YOU WON THE MATCH***********")
  else:
   print("\n\n***********MATCH DRAWN*******")

#if toss by computer the below  code will excuted


else:
 print("\ncomputer won the toss")
 com_option=random.choice(["bat","bowl"])
 
 
#computer batting first
  
 if com_option=="bat":
  print("\ncomputer selected batting\n\n you is bowling")
  com_runs=user_bowling()
  print("\n\nFINAL RUNS COMPUTER SCORED:",com_runs)
  print("\n\nNow you are batting")
  user_runs=user_batting2()
  print("\n\nFINAL RUNS you SCORED:",user_runs)
  if com_runs>user_runs:
   print("\n\n************COMPUTER WON THE MATCH************")
  elif com_runs<user_runs:
   print("\n\n***********YOU WON THE MATCH***********")
  else:
   print("\n\n***********MATCH DRAWN*******")

 
 #computer bowling first
  
 else:
  print("\ncomputer selected bowlling\n\nyou is battimg")
  user_runs=user_batting()
  print("\n\nFINAL RUNS YOU SCORED:",user_runs)
  print("\n\nNow computer is batting")
  com_runs=user_bowling2()
  print("\n\nFINAL RUNS COMPUTER SCPRED:",com_runs)
  if com_runs>user_runs:
   print("\n\n************COMPUTER WON THE MATCH************")
  elif com_runs<user_runs:
   print("\n\n***********YOU WON THE MATCH***********")
  else:
   print("\n\n***********MATCH DRAWN*******")