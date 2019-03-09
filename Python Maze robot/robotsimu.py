import grobot
import random
"""
Sia = grobot.NewRobot("Sia",1,2,"green")

count = 100
while count > 0:
    user = str(input("Enter a command: "))
    if user == "f":
        print("Sia forward", Sia.forward())
        if Sia.look == ["Broken", "Broken", "Broken", "Broken", "Broken"]:
            break
    elif user == "r":
        print("Sia right", Sia.right())
    elif user == "l":
        print("Sia left", Sia.left())
    exit1 = str(input("Exit = E"))
    if exit1 == "E":
        print("Exiting...")
        break
    count -= 1


f = Sia.forward()
r = Sia.right()
l = Sia.left()

print("Sia forward", Sia.forward())
print("Sia right", Sia.right())
print("Sia left", Sia.left())
"""
"""
Sia = grobot.NewRobot("Sia",1,1,"green")

count = 100
x=1
y=1
heading = "North"
print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
while count > 0:
    user = str(input("Enter a command: "))
    if user == "f":
        print("Sia forward", Sia.forward())
        if heading == "North":
            y = y + 1
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "South":
            y = y - 1
            print("Heading: {0}\nx is {1}\ny is {2}".format(heading, x,y))
        elif heading == "East":
            x = x + 1
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y)) 
        elif heading == "West":
            x = x - 1
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        if Sia.look == ["Broken", "Broken", "Broken", "Broken", "Broken"]:
            break
    elif user == "r":
        print("Sia right", Sia.right())
        if heading == "East":
            heading = "South"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "South":
            heading = "West"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "West":
            heading = "North"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "North":
            heading = "East"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
    elif user == "l":
        print("Sia left", Sia.left())
        if heading == "East":
            heading = "North"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "North":
            heading = "West"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "West":
            heading = "South"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
        elif heading == "South":
            heading = "East"
            print('Heading: {0}\nx is {1}\ny is {2}'.format(heading,x,y))
            
    exit1 = str(input("Exit = E"))
    if exit1 == "E":
        print("Exiting...")
        break
    count -= 1

Sia.init(x,y)

inc y when going north
dec y when going south

inc x when going east
dec x when going west 
"""

Sia = grobot.NewRobot("Sia",4,2,"green")

count = 500
while count > 0:
    f = Sia.look()[2]
    l = Sia.look()[0]
    ld = Sia.look()[1]
    r = Sia.look()[4]
    rd = Sia.look()[3]
    if f == None:
        print("Sia forward", Sia.forward())
    elif r == None:
        print("Sia right", Sia.right())
        print("Sia right", Sia.forward())
    elif l == None:
        print("Sia left", Sia.left())
        print("Sia left", Sia.forward())

    elif rd == None:
        if f == None:
            print("Sia right", Sia.forward())
            print("Sia right", Sia.right())
            print("Sia right", Sia.forward())

    elif ld == None:
        print("Sia right", Sia.forward())
        print("Sia right", Sia.left())
        print("Sia right", Sia.forward())

    count -= 1
    print(count)

#if Sia.look == ["Broken", "Broken", "Broken", "Broken", "Broken"]:
            #break





    
