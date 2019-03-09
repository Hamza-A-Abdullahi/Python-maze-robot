import grobot
import random
x = 4
y = 2
xx = 15
yy = 15
bob = grobot.NewRobot("bob", x,y,"Purple")
tom = grobot.NewRobot("tom", xx, yy, "Red")
bob.right()
tom.left()
def move_bob(bl,bld,bf,brd,br,beyes):
    if bf == "tom" or bf == "d" or bf == "hamza":
              print('Hi tom, how you doing?')
              print(bob.right())
              print(bob.forward())
    if beyes == [None,None,None,None,None]:
        r = random.randint(0,10)
        if r == 0:
            print(bob.left())
        elif r == 2:
            print(bob.left())
            print(bob.forward())
            print(bob.right())
            print(bob.forward())

        elif r == 3:
            print(bob.right())
            print(bob.forward())
            print(bob.left())
            print(bob.forward())
        elif r == 1:
            print(bob.right())
        else:
            print(bob.forward())
    elif beyes == [None,None,'Wall','Wall','Wall']:
        print(bob.left())

    elif beyes == [None,None,None,'Wall','Wall']:
        r = random.randint(0,1)
        if r == 0:
            print(bob.left())
        else:
            print(bob.forward())
    elif beyes == ['Wall','Wall',None,None,None]:
        r = random.randint(0,1)
        if r == 0:
            print(bob.right())
        else:
            print(bob.forward())
            
        
    elif bf == None:
         print(bob.forward())

    elif bl == None:
        print(bob.left())

    elif br == None:
        print(bob.right())

    if beyes == ['Wall','Wall','Wall','Wall','Wall']:
      print(bob.right())
      print(bob.right())

     

def move_tom(tl,tld,tf,trd,tr,teyes):
    if tf == "bob" or tf == "d" or tf == "hamza":
            print('Not bad, thanks for asking bob')
            print(tom.right())
            print(tom.forward())

    if teyes == [None,None,None,None,None]:
        r = random.randint(0,10)
        if r == 0:
            print(tom.left())

        elif r == 2:
            print(tom.left())
            print(tom.forward())
            print(tom.right())
            print(tom.forward())

        elif r == 3:
            print(tom.right())
            print(tom.forward())
            print(tom.left())
            print(tom.forward())
        elif r == 1:
            print(tom.right())
        else:
            print(tom.forward())

    elif teyes == [None,None,'Wall','Wall','Wall']:
        print(tom.left())

    elif teyes == [None,None,None,'Wall','Wall']:
        r = random.randint(0,1)
        if r == 0:
            print(tom.left())
        else:
            print(tom.forward())

    elif teyes == ['Wall','Wall',None,None,None]:
        r = random.randint(0,1)
        if r == 0:
            print(tom.right())
        else:
            print(tom.forward())
            
    elif tf == None:
        print(tom.forward())
        
    elif tl == None:
        print(tom.left())
        
    elif tr == None:
        print(tom.right())
    if teyes == ['Wall','Wall','Wall','Wall','Wall']:
      print(tom.right())
      print(tom.right())
    

def main():
    count = 500
    while count > 0:
        tl = tom.look()[0]
        tld = tom.look()[1]
        tf = tom.look()[2]
        trd = tom.look()[3]
        tr = tom.look()[4]
        teyes = tom.look()
        print('tom Red: ',teyes)
        bl = bob.look()[0]
        bld = bob.look()[1]
        bf = bob.look()[2]
        brd = bob.look()[3]
        br = bob.look()[4]
        beyes= bob.look()
        print('Bob Purple: ',beyes)

        move_bob(bl,bld,bf,brd,br,beyes)
        move_tom(tl,tld,tf,trd,tr,teyes)
        

        count -= 1

main()

