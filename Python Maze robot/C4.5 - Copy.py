import grobot
import random

d = grobot.NewRobot("Bob", 2, 2, "Green")

world = [ [True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]]
def main():
  head = "north"
  x = 2
  y = 2
  robot(head,x,y)

def robot(head,x,y):
  
  def print_world(x,y):
    for x in range(len(world)):
      a = ''
      for y in range(len(world[x])):
        if (world[x][y]):
          a = '#'
        else:
          a = ' '
        #print(a, end= "|")
  count = 2000
  while count > 0:
    print()
    f = d.look()[2]
    l = d.look()[0]
    ld = d.look()[1]
    rd = d.look()[3]
    r = d.look()[4]
    All = [l,ld,f,rd,r]
    print(All)
    if f == 'Wall':
      world[x][y] = True
      print('x:',x,'y:',y)
    if f == None:
      nn = random.randint(0,6)
      if nn == 0:
        if l == 'Wall' and ld == 'Wall' and f == None and rd == 'Wall' and r == None:
          print(d.right())
          head_right(head,x,y)
      elif nn == 1:
        if l == 'Wall' and ld == None and f == None and rd == 'Wall' and r == None:
          n = random.randint(0,2)
          if n == 0:
            print(d.right())
            head_right(head,x,y)
            print(d.forward())
            headin(head,x,y)
            
      else:
        print(d.forward())
        headin(head,x,y)

  ###################################################################################
    elif l == None:
      n = random.randint(0,7)
      if n == 1:
        if l == None and ld == 'Wall' and f == 'Wall' and rd == 'Wall' and r == None:
         print(d.right())
         head_right(head,x,y)
      elif n == 2:
        print(d.right())
        head_right(head,x,y)
      else:
        print(d.left())
        head_left(head,x,y)
  ##################################################################
    elif f == None and l == None:
      n = random.randint(0,2)
      print('Random',n)
      if n <= 1:
        print(d.forward())
        headin(head,x,y)
      else:
        print(d.left())
        head_left(head,x,y)  
  ###############################################################  

    elif ld == 'Wall' and rd == 'Wall' and f == None:
      print(d.forward())
      headin(head,x,y) 
  ##################################################      

    elif r == None:
        print(d.right())
        head_right(head,x,y)
        ############################################
    elif l == 'Wall' and f == 'wall' and r == 'Wall' or ld == 'Wall' or rd == 'Wall':
      print(d.left())
      head_left(head,x,y)
      print(d.left())
      head_left(head,x,y)
  ##############################################################   
    elif f == None:
      print(d.forward())
      headin(head,x,y)
    count -= 1
    print(count)

def headin(head,x,y):
  if head == 'north':
    y = y + 1
  elif head == 'east':
    x = x + 1
  elif head == 'south':
    y = y - 1
  else:
    x = x - 1
  world[x][y] = False
  print('x:',x,'y:',y)
    
def head_right(head,x,y):
  if head == 'west':
    head = 'north'
  elif head == 'north':
    head = 'east'
  elif head == 'east':
    head = 'south'
  else:
    head = 'west'
  world[x][y] = False
  print('x:',x,'y:',y)

def head_left(head,x,y):
  if head == 'west':
    head = 'south'
  elif head == 'south':
    head = 'east'
  elif head == 'east':
    head = 'north'
  else:
    head = 'west'
  world[x][y] = False
  print('x:',x,'y:',y)

main()
print_world()
