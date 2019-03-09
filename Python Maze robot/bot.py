import grobot
import random

bot = grobot.NewRobot('Robot', 15,15,'Blue')

def start():
  loop()

def forwardd(x,y,heading):
  if heading == 'north':
    y += 1
  elif heading == 'east':
    x += 1
  elif heading == 'south':
    y -= 1
  else:
    x -= 1
  return x,y

def leftt(heading):
  if heading == 'north':
    heading == 'west'
  elif heading == 'west':
    heading = 'south'
  elif heading == 'south':
    heading = 'east'
  else:
    heading = 'north'
  return heading

def rightt(heading):
  if heading == 'north':
    heading == 'east'
  elif heading == 'east':
    heading = 'south'
  elif heading == 'south':
    heading = 'west'
  else:
    heading = 'north'
  return heading


def loop():
  heading = 'north'
  x = 15
  y = 15
  count = 50
  while count != 0:

    lv = bot.look()[0]
    ldv = bot.look()[1]
    fv = bot.look()[2]
    rdv = bot.look()[3]
    rv = bot.look()[4]
    view = bot.look()

    if view == [None,None,None,None,None]:
      rn = random.randint(0,2)
      if rn == 0:
        print(bot.forward())
        forwardd(x,y,heading)
      elif rn == 1:
        print(bot.left())
        print(bot.forward())
        leftt(heading)
        forwardd(x,y,heading)
      else:
        print(bot.right())
        print(bot.forward())
        rightt(heading)
        forwardd(x,y,heading)
        
    print('Heading:',heading)
    print('x:',x)
    print('y:',y)
      
    
    count -+ 1
start()
