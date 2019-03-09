import grobot
import random

d = grobot.NewRobot("Bob", 2, 2, "Green")

world = [ [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
          [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]]
def main():
  robot()
def print_world():
  for x in range(len(world)):
    a = ''
    for y in range(len(world[x])):
      if (world[x][y]):
        a = '#'
      else:
        a = ' '
      print(a,end="|")

def robot():
  global heading
  global x
  global y
  heading = "north"
  x = 2
  y = 2
  count = 50000
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
      wall()
    if f == None:
      nn = random.randint(0,6)
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
            if heading == 'north':
              y = y + 1
              
            elif heading == 'east':
              x = x + 1
              
            elif heading == 'south':
              y = y - 1
              
            else:
              x = x - 1
              
        
            
      else:
        print(d.forward())
        if heading == 'north':
          y = y + 1
          
        elif heading == 'east':
          x = x + 1
          
        elif heading == 'south':
          y = y - 1
          
        else:
          x = x - 1
          
        

  ###################################################################################
    elif l == None:
      n = random.randint(0,7)
      if n == 1:
        if l == None and ld == 'Wall' and f == 'Wall' and rd == 'Wall' and r == None:
         print(d.right())
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
        if heading == 'north':
          y = y + 1
          
        elif heading == 'east':
          x = x + 1
          
        elif heading == 'south':
          y = y - 1
          
        else:
          x = x - 1
          
        
      else:
        print(d.left())
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
      if heading == 'north':
        y = y + 1
        
      elif heading == 'east':
        x = x + 1
        
      elif heading == 'south':
        y = y - 1
        
      else:
        x = x - 1
        
      
      
  ##################################################      

    elif r == None:
        print(d.right())
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
      if heading == 'west':
        heading = 'south'
      elif heading == 'south':
        heading = 'east'
      elif heading == 'east':
        heading = 'north'
      else:
        heading = 'west'
      print(d.left())
      if heading == 'west':
        heading = 'south'
      elif heading == 'south':
        heading = 'east'
      elif heading == 'east':
        heading = 'north'
      else:
        heading = 'west'
      
      
  ##############################################################   
    elif f == None:
      print(d.forward())
      if heading == 'north':
        y = y + 1
        
      elif heading == 'east':
        x = x + 1
        
      elif heading == 'south':
        y = y - 1
        
      else:
        x = x - 1
        
    world[(30-x)-1][y-1] = False
	
    count -= 1
    print(count)
    print('x:',x,'y:',y)

def wall():
  if heading == 'north':
	  world[(30-x)-1][y+1] = False
  elif heading == 'east':
	  world[(30-x)][y-1] = False
  elif heading == 'south':
	  world[(30-x)-1][y-1] = False
  else:
	  world[(30-x)-2][y-1] = False
  print_world()
  print('x:',x,'y:',y)

  
main()
print_world()
