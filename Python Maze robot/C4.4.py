import grobot
import random
d = grobot.NewRobot("cat", 27, 9, "Green")
x = 27
y = 9
heading = "north"
print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
print()
xd = int(input('Enter your destionation x coordinate: '))
yd = int(input('Enter your destionation y coordinate: '))
count = 10000
while count > 0:
  print()
  f = d.look()[2]
  l = d.look()[0]
  ld = d.look()[1]
  rd = d.look()[3]
  r = d.look()[4]
  All = [l,ld,f,rd,r]
  print(All)
  if f == None:
    nn = random.randint(0,7)
    if nn == 0:
      if l == 'Wall' and ld == 'Wall' and f == None and rd == 'Wall' and r == None:
        print(d.right())
        if heading == 'west':
          heading = 'north'
        elif heading == 'north':  
          heading = 'east'
        elif heading == 'east':
          heading = 'south'
        else:
          heading = 'west'
    elif nn == 1:
      if l == 'Wall' and ld == None and f == None and rd == 'Wall' and r == None:
        n = random.randint(0,2)
        if n == 0:
          print(d.right())
          if heading == 'west':
            heading = 'north'
          elif heading == 'north':
            heading = 'east'
          elif heading == 'east':
            heading = 'south'
          else:
            heading = 'west'
        else:
          print(d.forward())
          print('If statement 9')
          if heading == 'north':
            y = y + 1
            if x == xd and y == yd:
              print('Reached Goal Destination:',xd,yd)
              break
            print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
          elif heading == 'east':
            x = x + 1
            if x == xd and y == yd:
              print('Reached Goal Destination:',xd,yd)
              break
            print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
          elif heading == 'south':
            print()
            y = y - 1
            if x == xd and y == yd:
              print('Reached Goal Destination:',xd,yd)
              break
            print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
          else:
            x = x - 1
            if x == xd and y == yd:
              print('Reached Goal Destination:',xd,yd)
              break
            print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
    else:
      print(d.forward())
      print('If statement 9')
      if heading == 'north':
        y = y + 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
      elif heading == 'east':
        x = x + 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
      elif heading == 'south':
        print()
        y = y - 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
      else:
        x = x - 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))

###################################################################################
  elif l == None:
    n = random.randint(0,7)
    print('Random:',n)
    
    if n == 1:
      if l == None and ld == 'Wall' and f == 'Wall' and rd == 'Wall' and r == None:
       print(d.right())
       print('If statement 6')
       if heading == 'west':
         heading = 'north'
       elif heading == 'north':
         heading = 'east'
       elif heading == 'east':
         heading = 'south'
       else:
         heading = 'west'
    elif n == 2:
      print(d.right())
      if heading == 'west':
        heading = 'north'
      elif heading == 'north':
        heading = 'east'
      elif heading == 'east':
        heading = 'south'
      else:
        heading = 'west'
    else:
      print(d.left())
      print('If statement 7')
      if heading == 'west':
        heading = 'south'
      elif heading == 'south':
        heading = 'east'
      elif heading == 'east':
        heading = 'north'
      else:
        heading = 'west'
##################################################################
  elif f == None and l == None:
    n = random.randint(0,2)
    print('Random',n)
    if n <= 1:
      print(d.forward())
      print('If statement 1')
      if heading == 'north':
        y = y + 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
      elif heading == 'east':
        x = x + 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
      elif heading == 'south':
        print()
        y = y - 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
      else:
        x = x - 1
        if x == xd and y == yd:
          print('Reached Goal Destination:',xd,yd)
          break
        print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
    else:
      print(d.left())
      print('If statement 2')
      if heading == 'west':
        heading = 'south'
      elif heading == 'south':
        heading = 'east'
      elif heading == 'east':
        heading = 'north'
      else:
        heading = 'west'
 
###############################################################  

  elif ld == 'Wall' and rd == 'Wall' and f == None:
    print(d.forward())
    print('If statement 8')
    if heading == 'north':
      y = y + 1
      if x == xd and y == yd:
        print('Reached Goal Destination:',xd,yd)
        break
      print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
    elif heading == 'east':
      x = x + 1
      if x == xd and y == yd:
        print('Reached Goal Destination:',xd,yd)
        break
      print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
    elif heading == 'south':
      print()
      y = y - 1
      if x == xd and y == yd:
        print('Reached Goal Destination:',xd,yd)
        break
      print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
    else:
      x = x - 1
      if x == xd and y == yd:
        print('Reached Goal Destination:',xd,yd)
        break
      print('Current heading & location\nHeading: {0}\nx:{1}\ny:{2}'.format(heading,x,y))
##################################################      
 
###################################################
  elif r == None:
      print(d.right())
      print('If statement 10')
      if heading == 'west':
        heading = 'north'
      elif heading == 'north':
        heading = 'east'
      elif heading == 'east':
        heading = 'south'
      else:
        heading = 'west'
##################################################
  elif l == 'Wall' and f == 'wall' and r == 'Wall' or ld == 'Wall' or rd == 'Wall':
    print(d.left())
    print('If statement 11')
    if heading == 'west':
      heading = 'south'
    elif heading == 'south':
      heading = 'east'
    elif heading == 'east':
      heading = 'north'
    else:
      heading = 'west'
    print(d.left())
    print('If statement 12')
    if heading == 'west':
      heading = 'south'
    elif heading == 'south':
      heading = 'east'
    elif heading == 'east':
      heading = 'north'
    else:
      heading = 'west'
      print()
##############################################################   

  if f == "tom" or f == "bob" or f == "hamza":
        print(hamza.right())
        
  count -= 1
  print(count)
