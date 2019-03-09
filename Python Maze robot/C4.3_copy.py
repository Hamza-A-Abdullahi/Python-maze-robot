import grobot
import random


h = grobot.NewRobot("Ha", 2,2, "Red")
count = 500
while count > 0:
    f = h.look()[2]
    l = h.look()[0]
    ld = h.look()[1]
    rd = h.look()[3]
    r = h.look()[4]
    All = [f,l,ld,rd,r]
    print(All)
    if f == None:
        ran = random.randint(0,1)
        print('Ran:', ran)
        if ran == 0:
            print(h.forward())
            print('If statement - 10,2')
        elif ran == 1:
            rr = h.look()[4]
            ll = h.look()[0]
            if rr == None:
                print(h.right())
                print(h.forward())
            elif ll == None:
                print(h.left())
                print(h.forward())
    elif l == None:
      print(h.left())
      print(h.forward())
      print('If statement - 10,3')
      f = h.look()[2]
      l = h.look()[0]
      ld = h.look()[1]
      rd = h.look()[3]
      r = h.look()[4]
      print(f,l,ld,rd,r)
      if r == None:
          print(h.right())
          print(h.forward())
      elif rd == None:
          r = h.look()[4]
          if r == None:
              print(h.right())
              print(h.forward())
              print(h.left())
              print(h.forward())
      elif ld == None:
          l = h.look()[0]
          if l == None:
              print(h.left())
              print(h.forward())
              print(h.right())
              
              print(h.forward())
    elif ld == None:
      l = h.look()[0]
      if l == None:
          print(h.left())
          print(h.forward())
          print(h.right())
          print(h.forward())
          print('If statement - 10,4')
    elif rd == None:
      r = h.look()[4]
      if r == None:
          print(h.right())
          print(h.forward())
          print(h.left())
          print(h.forward())
          print('If statement - 11,1')
    elif r == None:
        print(h.right())
        print(h.forward())
        print('If statement - 12')
    elif f == None and l == None and ld == None and rd == None and r == None:
          n = random.randint(0,4)
          print(n)
          if n == 0:
              print(h.forward())
              print('If statement - 5,1')
          elif n == 1:
              print(h.left())
              print(h.forward())
              print('If statement - 5,2')
          elif n == 2:
              print(h.left())
              print(h.forward())
              print(h.right())
              print(h.forward())
              print('If statement - 5,3')
          elif n == 3:
              print(h.forward())
              print(h.right())
              print(h.forward())
              print('If statement - 5,4')
          elif n == 4:
              print(h.right())
              print(h.forward())
              print('If statement - 5,5')
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
          print(h.right())
          print(h.right())
          ff = h.look()[2]
          print(ff)
          if ff == None:
              print(h.forward())
              print('If statement - 10,1')



    count -= 1
    print(count)
