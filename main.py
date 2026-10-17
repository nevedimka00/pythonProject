# print("I like pizza!")
# print("Its really good!")

# first_name ="alik"
# print(first_name)
# print(f"Hello {first_name}")

# age=30
# is_name=True
# if(is_name): print(first_name)
# else:print(age)

# year ="1992"
# year=int(year)
# test="test"
# test=bool(test)


# name = input("what is your name? ")
# age = int(input("How old are you? "))
# print(f"Your name is {name}")
# age+=1
# print(f"You are {age} years old")

# name = ""

# if not name:print("name") 

# operator = input("Enter an operator(+ - * /) ")
# firstDigit = float(input("Enter the first digit "))
# secondDigit = float(input("Enter the second digit "))

# if operator=="+" : print(firstDigit+secondDigit)
# elif operator=="-":print(firstDigit-secondDigit) 
# elif operator=="*":print(firstDigit*secondDigit)
# else: print(firstDigit/secondDigit)

# num = 5
# print("five" if num<10 else "ten")

# a=39
# b=1
# max_result = a if a>b else b
# print(max_result)

# user_role="admin"
# access = "Full" if user_role=="admin" else "Limited"

# name = "alik petrosyan"
# result = len(name)
# result = name.find(" ")
# result = name.find("p")
# result = name.rfind("a")
# result = name.capitalize()
# result = name.upper()
# # false cause has space or number
# result = name.isalpha()
# result = name.count("a")
# result = name.replace("a","A")

# printUsername = False
# while not printUsername:
#     username = input("Please enter the username: ")
#     if len(username)>12 or not username.isalpha() :
#         print("Please enter correct form of username")
#     else : 
#         print(username) 
#         printUsername = True

# name = "alik petrosyan"
# print(name[0])
# print(name[:4])
# print(name[5:8])
# print(name[9:])
# print(name[-1])
# print(name[::2])

# credit_card = '1234-5678-9012-3456'
# print(credit_card[-4:])
# credit_card = credit_card[::-1]
# print(credit_card)

# pi = 3.14159265
# print(f"{pi:.2f}")   
# print(f"{0.506:%}")

# money = 1000000
# print(f"{money:,}")  
# print(f"{money:_d}")

# price = 49
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
# print(txt)

# price1=3000.3097057539
# print(f"{price1:+,.2f}")

# principle = 0
# rate = 0
# time = 0

# while  principle<=0:
#     principle=float(input("Enter the principal amount: "))
#     if principle <=0:
#         print("Principle cant be less than or equal to 0")


# while  rate<0:
#     rate=float(input("Enter the interest rate amount: "))
#     if rate <=0:
#         print("Interest rate  cant be less than or equal to 0")

# while  time<=0:
#     time=int(input("Enter the time in years: "))
#     if time <=0:
#         print("Time  cant be less than or equal to 0")
# total = principle * pow((1+rate/100),time)

# txt = f"Balance after {time} years/s is ${total:.2f}"
# print(txt)

# for x in reversed(range(1,11,2)):
#     print(x)

# credit_card = '1234-5678-9012-3456'

# for x in credit_card:
#     print(x)

# for x in range(1,15):
#     if(x==10):continue
#         # break
#     else:print(x)

# import time

# my_time=int(input("Enter time in seconds "))

# for x in range(my_time,0,-1):
#     minutes = int(x/60)%60
#     seconds = x%60
#     hours = int(x/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Boom")

 
# for x in range(3):
#     for y in range(1,10):
#         print(y,end='')
#     print()
    

# for x in range(10):
#     for y in range(x):
#         print('*',end="")
#     print()

# LIST ordered,changable, duplicates
# food= ['apple','orange','pizza','coconat']
#  for f in food:
#      print(f)
# food.insert(1,"pineapple")
# food.sort()
# print(food)
# print(food[::-1])

# SET unordered, immutable, add/rem ok
# food= {'apple','orange','pizza','coconat'}

# food[2]='banana'
# food.add("banana")
# food.add("banana")
# print(food)
# for f in food:
#     print(f)
# TUPLE ordered, immutable, duplicates
# my_tupple = (5,20,1,4,8)
# for m in my_tupple:
#     print(m)

# foods =[]
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy(q to quit): ")
#     if food.lower()=="q": break
#     else:
#         price = float(input(f"Enter the price of a {food} "))
#         foods.append(food)
#         prices.append(price)
# print("-------YOUR CART-------")
# for f in foods:
#     print(f,end=" ")

# for p in prices:
#     total+=p
# print()
# print(f"Your total is:{total}")

# fruits = ["apple","banana"]
# meats = ["chiken","ham"]

# food = [fruits,meats]

# for i in food:
#     for j in i :
#         print(j,end=" ")
#     print()

# questions = ("whats my name",
#              "how old i am",
#              "whats my dogs name",
#              "where i live",
#              "where i am from")

# options = (("A. aaa1","B. bbb1","C. alik","D. ddd1"),
#            ("A. 5","B. 11","C. 29","D. 38"),
#            ("A. una","B. bbb2","C. ccc2","D. ddd2"),
#            ("A. aaa3","B. irpin","C. ccc3","D. ddd3"),
#            ("A. batumi","B. bbb4","C. ccc4","D. ddd4"))
# answer = ("C","D","A","B","A")
# guesses = []
# score=0


# for q in questions:
#     print("--------------------")
#     print(q)
#     for o in options[questions.index(q)]:
#         print(o)
#     guess=input("Enter (A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess==answer[questions.index(q)]:
#         print("Correct!")
#         score+=1
#     else :
#         print("Incorrect!")
#         print(f"Correct answer is {answer[questions.index(q)]}")
# print("--------------------") 
# print(f"Your score is {score}")
# print(f"Your guesses were {guesses}")
# print(f"Correct answers were {answer}")

# --- DICTIONARY------
# capitals = {"Ukraine":"Kyiv",
#             "Georgia":"Tbilisi",
#             "France":"Paris",
#             "Germany":"Berlin"}
# print(capitals.get("Ukraine"))

# for key,value in capitals.items():
#     print(key + " " +  value)

# menu = {"pizza":3.00,
#         "nachos": 4.50,
#         "popcorn":6.00,
#         "fries":2.5,
#         "chips":1.00,
#         "pretzel":3.50,
#         "soda":3.00,
#         "lemonade":4.25}

# cart = []
# total = 0

# print("-----MENU-------")
# for key,value in menu.items():
#     print(f"{key:10} ${value:.2f}")
# print("----------------")

# food=""

# while not (food == str.lower("q")):
#     food=input("Select an item (q to quit): ")
#     if(menu.get(food)):
#         cart.append(food)
#         total+=menu.get(food)
#     else: print("Such item does not exist")
# print(f"Your order is {cart}")
# print(f"Total price is ${total}")

# ----RANDOM------
import random

# number = random.randint(1,6)
# number = random.random()
# print(number)
# options = ("rock","paper","scissors")
# print(random.choice(options))
# cards = ["2","3","4","5","6","7"]
# random.shuffle(cards)
# print(cards)

# GAME 1

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num,highest_num)
# guesses = 0
# is_running = True

# print("Welcome to the Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:
#     user_guess = input("Enter your number: ")
#     if(user_guess.isdigit()):
#         user_guess=int(user_guess)
#         if(user_guess>=lowest_num and user_guess<=highest_num):
#             if(user_guess<answer):
#                 print("Too low")
#                 guesses+=1
#             elif(user_guess>answer):
#                 print("Too high")
#                 guesses+=1
#             else:
#                 guesses+=1 
#                 print(f"YOU WON IN {guesses} GUESSES")
#                 is_running=False
#         else:print("Please enter the correct guess") 
#     elif(user_guess.lower()=="q"):
#         print(f"Number was {answer}")
#         print(f"You had {guesses} guesses")
#         is_running=False    
#     else:print("Please enter the correct guess") 

# GAME 2

# options = ("rock","paper","scissors")
# score = {"computer":0,"player":0}
# is_running = True

# while is_running:
#     player = input("Enter a choise (rock,paper,scissors) or q to exit ")
#     computer = random.choice(options)
#     if player in options:
#         print(f"Player: {player}")
#         print(f"Computer: {computer}")    
#         if (player=="rock" and computer=="paper"):
#             score.update(computer=score.get("computer")+1)
#         elif(player=="rock" and computer=="scissors"):
#             score.update(player=score.get("player")+1)
#         elif(player=="paper" and computer=="rock"):
#             score.update(player=score.get("player")+1)
#         elif(player=="paper" and computer=="scissors"):
#             score.update(computer=score.get("computer")+1)
#         elif(player=="scissors" and computer=="rock"):
#             score.update(computer=score.get("computer")+1)
#         elif(player=="scissors" and computer=="paper"):
#             score.update(player=score.get("player")+1) 
#         else: print("Its a draw!")
#         print(f"Score is: {score}")
#     elif(player.lower()=="q"):
#         print(f"Score is: {score}")
#         print("Bye!")
#         is_running=False
#     else: print("Please enter correct value")    

# GAME 3
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# "┌───────┐"
# "│       │"
# "│   ●   │"
# "│       │"
# "└───────┘"

# dice_art = {
#     1:( "┌───────┐",
#         "│       │",
#         "│   ●   │",
#         "│       │",
#         "└───────┘"),
#     2:( "┌───────┐",
#         "│ ●     │",
#         "│       │",
#         "│     ● │",
#         "└───────┘"),
#     3:( "┌───────┐",
#         "│ ●     │",
#         "│   ●   │",
#         "│     ● │",
#         "└───────┘"),
#     4:( "┌───────┐",
#         "│ ●   ● │",
#         "│       │",
#         "│ ●   ● │",
#         "└───────┘"),
#     5:( "┌───────┐",
#         "│ ●   ● │",
#         "│   ●   │",
#         "│ ●   ● │",
#         "└───────┘"),
#     6:( "┌───────┐",
#         "│ ●   ● │",
#         "│ ●   ● │",
#         "│ ●   ● │",
#         "└───────┘")   
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for i in range(num_of_dice):
#     dice.append(random.randint(1,6))

# # for j in dice:
# #     total+=j
# #     for e in dice_art.get(j):
# #         print(e)
# # print(f"Total: {total}")

# for i in range(5):
#     for j in dice:
#         print(dice_art.get(j)[i],end=" ")
#     print()
# print(dice)

# def sing_a_song(number:int,line:str):
#     for i in range(number):
#         print(line)

# number_of_times=3
# line_to_sing = "Happy Birthday"

# sing_a_song(number_of_times,line_to_sing)
# sing_a_song(number=2,line="Hello")

# def calculator(a:int,*,b:int,c=4):
#     return a+b+c

# print(calculator(2,b=3))

# import time

# def count(end,start=0):
#     for i in range(start,end+1):
#         print(i)
#         time.sleep(1)
#     print("Done!")

# count(5)


# def testKeywords(a:int|None=3):
#     print(a)

# testKeywords()

# def add(**a):
#     total=0
#     for i in a.values():
#         total+=int(i)
#     return total

# print(add(a=1,b=2,c=3))

# numbers:list[int] = [5,6,10,2,4]

# def myShuffle(a:list):
#     a.sort()
# myShuffle(numbers)
# print(numbers)

# def shipping_label(*args,**kwargs):
#    for a in args:
#       print(a,end=" ")
#    print()
#    for k in kwargs.values():
#       print(k,end=" ")
#    print(kwargs.get('zip',default="") )      

# shipping_label("mr","krasty","krabs",
#                street="oleni t",
#                apt="76",
#                city="Irpin",zip="1000")

# doubles = [x*2 for x in range(1,10)]
# print(doubles)

# fruits = ["apple","banana","pear"]
# fruits = [f.capitalize() for f in fruits]
# fruits_2 = [f.capitalize() for f in ["apple","banana","pear"]]
# # test_line="test line for title"

# print(fruits)

# numbers = [1,-2,-3,5,-7,4,3]
# positive = [num for num in numbers if num%2==0]
# print(positive)

# def day_of_week(day):
#     match day:
#         case 1 | 3 : return "One or Threee"
#         case 2 | 4 : return "Two or Four"
#         case _ : return "WTF Dude??"

# print(day_of_week(5))

# print(help("modules"))
# import math as m
# import test_module

# print(test_module.test_line)
# print(test_module.transformNumber(3))
# print(test_module.transformLine("my line"))

# import requests

# responce = requests.get("https://google.com")
# print(responce.connection)


def coordinates():
    x=5
    y=6
    return x,y

print(type(coordinates()))