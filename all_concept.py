#print 
"""print("shagun amol tembhurne")"""

#taking input and formatted string concept
"""s=int(input("what is your age:"))
print(f'your age is {s}')"""

#car game
"""start_comnmand = "start"
stop_command= "stop"
quit_command = "quit"
print(f'you have these choices:\n {start_comnmand}- will start the car \n {stop_command}-will stop the car\n {quit_command}-will quit the game ')
running = True
while running:
    command = input("command:")
    if command == start_comnmand:
        print('your car is started')
    elif command == stop_command:
        print('your car is stopped')
    elif command == quit_command:
        print("you quit")
           break
        min_tries += 1
        if min_tries== max_tries:
            print(f'well you lost and the number was {random_number}')
    except ValueError:
        print("invalid input")     running = False
    else:
        print("you gave invalid input")"""

#for loop
"""for s in range (4):
    print(s)"""

"""for s in range (4):
    for y in range (5):
        print(f'{s},{y}')"""
#here to make an f using for loop
"""r = (5,2,5,2,2)
for num in r:
    s = num * "x"
    print(s)"""
#add the prices there are in the shooping cart 
"""price = [40,50,100,130]
total = 0
for prices in price:
    total += prices 
print (f"the ammount in the basket is{total}")"""

#guess game
"""import random
random_number = random.randint(1,100)
max_tries = 5
min_tries =0
print ('WELCOME TO THIS GUESS GAME\n max tries are 5 \n so lets start')
while min_tries < max_tries:
    try:
        guess = int(input('GUESS:'))
        if guess < random_number:
            print("higher!!!")
        elif guess > random_number:
            print("lower!!!")
        else:
            print("you won")

    """
#make it small with just while and if loop with 0-10

#calculator 
"""def ADD (x,y):
    return x+y
def MUL (x,y):
    return x*y
def SUB (x,y):
    return x-y
def DIV (x,y):
    if y==0:
        print('0 in denominator is a invalid input')
    return x/y
def CALCULATOR ():
    print("WELCOME TO THE PYTHON CALCULATOR")
    print('these are your instructions')
    print('1.ADD')
    print('2.MUL')
    print("3.SUB")
    print('4.DIV')
    continue_cal = "yes"
    while True:
        try:
            options = int(input("choose one option:"))
            if options in (1,2,3,4):
                num1 = float(input('give num1:'))
                num2 = float(input("give num2:"))
                if options == 1:
                    results = ADD (num1,num2)
                    print(results)
                elif options == 2:
                    results = MUL (num1,num2)
                    print(results)
                elif options == 3:
                    results = SUB (num1,num2)
                    print(results)
                elif options == 4:
                    results = DIV (num1,num2)
                    print(results)
                else:
                    continue_cal = input('do you wanna continue yes/no')
                if continue_cal.lower() != "yes":
                    break
            else:
                print('choose from 1-4')
        except ValueError:
            print('the input is not valid. choose from 1-4')
CALCULATOR()"""

#list method 
#basically its about using list and .operator 
"""list = [2,3,4,5,6]
list.insert(0,10)
print(list)
"""# well play with all the operators later
#to remove duplicates from a list method 1
"""s = [2,2,3,3,4,4,5,5]
list2 = list(set(s))
print(list2)"""#so this is the method one but in method 2 we can use 1 list can iterate over
#another list and then we can jsut put that into another list
"""l = [2,2,3,3,4,4,5,5,]
s = []
for l in l:
    if l not in s:
        s.append(l)
print(s)"""

#these are the dictonarties we can create and the ones which we can use and i have to practice

"""phone = input("tell me the input")
digits_mapping = {
    "1": 'one',
    "2": 'two',
    "3": 'three',
    "4": "four" 

}   
output= "" 
for ch in phone:
    output += digits_mapping.get(ch,"!")
print(output)
    """
"""message = input('>')
words = message.split
emojis = {
    ":)" : "😁",
    ":(" : "🙃"
}
output = ""
for words in words:
    output += emojis.get(words,words)
print(output)"""#practice this shit
 
 #defining function
"""def number():# bascically we are defining a functiona nd callin it out later 
 print("hello")

print('world')
number()
print('eeee')"""
"""def num(name):#here we are giving a value and maiking a fucntion and understanding the concept
    print(f'hi {name} welcome aboard')
print ('helo world')
num("shagun")#use comma and you can use two shit at same time too
num("s")#basically this is a parameter and we have to work under these parameters
"""
#there is a concept of positionnal and keyword argument in this 
#so what you are doing is first_name = shagun can be done and to numeric values we can give x=5 for better code 
 

#CLASSES
"""class Point:
    def move():
        print("move")
    def draw():
        print("draw")
Point1 = Point()
Point1.x = 10
Point1.y = 20
print(Point1.x)
Point1.draw()
"""

"""prrice of the house is 1 mil
if the buyer has good credit they need to put down 10 percent 
if the buyer has bad credit they need to put down 20 percent 
print the down payment """
"""price = 1000000
good_credit = True
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down payment: ${down_payment}")"""

"""enter = int(input('weight'))
weight_kg = enter / 2.20462
weight_lb = enter * 2.20462
options = input('is your weight in lb or kg')
while options == "kg":
    print(weight_kg)
    if options == "lb":
        print(weight_lb)
        break
else:
    print("i dont get you")"""
#this is what we made and now we are gonna take inspiration and do next style code
"""continue_conversion = True
while continue_conversion:
    try:
        enter = float(input('please enter your weight'))
        options = input("convert weight into kg or lbs?").lower()
        
        if options == "kg":
            weight_kg = enter / 2.20
            print(weight_kg)
            
        elif options == "lbs":
            weight_lb = enter * 2.20
            print (weight_lb)
            
        else:
            print("please only select kg or lbs")
        
        another_try = input("do you still wanna continue yes or no").lower()
        if another_try != "yes":
            break
    except ValueError:
        print("invalid input please put a valid input in")"""

"""import random
secret_mumnber = random.randint(1,100)
max_tries = 5
min_tries = 0

print("WELCOME TO THIS GAME YOU WILL HAVE 5 TRIES TO GUESS THE SECRET NUMBER")
while min_tries < max_tries:
    try:
        guess = int(input("guess the number"))

        if guess < secret_mumnber:
            print('higher')
        
        elif guess > secret_mumnber:
                print('lower')
        else:
                print("yayy!! you guessed it")
                break
        min_tries += 1
    except ValueError:
        print("invalid error")
if max_tries == min_tries and guess != secret_mumnber:
              print('sorry you failed at this too hahhaha')"""
  
            


        
    
