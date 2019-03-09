import grobot

print('This is a simple user interface where you\ncan control a robot using few simple commands.')
print()
print('Commands\nf = Forward\nl = Turn Left\nr = TurnRight')
print()
h = grobot.NewRobot("Hamza", 2, 2, "Red")
x = 2
y = 2
heading = "north"
print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
print()

count = 40
while count > 0:
  print()
  print(h.look())
  
  option = str(input('Enter command: '))
  if option == 'f':
    print(h.forward())
    if heading == 'north':
      y = y + 1
      print()
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
      print()
    elif heading == 'east':
      x = x + 1
      print()
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
      print()
    elif heading == 'south':
      print()
      y = y - 1
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
      print()
    else:
      x = x - 1
      print()
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
      print()

    if h.look() == ['Broken', 'Broken', 'Broken', 'Broken', 'Broken']:
      break
  elif option == 'l':
    print(h.left())
    print()
    if heading == 'west':
      heading = 'south'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    elif heading == 'south':
      heading = 'east'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    elif heading == 'east':
      heading = 'north'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    else:
      heading = 'west'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
  elif option == 'r':
    print(h.right())
    print()
    if heading == 'east':
      heading = 'south'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    elif heading == 'south':
      heading = 'west'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    elif heading == 'west':
      heading = 'north'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    else:
      heading = 'east'
      print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))


  elif option != 'f' or option != 'l' or option != 'r':
    print()
    print('**ONLY COMMANDS ARE ACCEPTED***')
    print()
    count = count + 1
  count -= 1

def outofBounds(heading,x,y):
  if x + 1 > 30 and heading == "east":
    heading = turnRight(heading)
    heading = turnRight(heading)
  elif x -1 < 1 and currHead == "eest":
    heading = turnRight(heading)
    heading = turnRight(heading)
  elif y - 1 <= 0 and currHead == "south":
    heading = turnRight(heading)
    heading = turnRight(heading)
  elif y +1 > 30 and currHead == "north":
    heading = turnRight(heading)
    heading = turnRight(heading)
  return heading


def turnRight(heading):
  h.right()
  if heading == "north":
    heading = "east"
  elif heading == "east":
    heading = "south"
  elif heading == "south":
    heading = "west"
  elif heading == "west":
    heading = "north"
  return heading 

def turnLeft(heading):
  h.left()
  if heading == "north":
    heading = "west"
  elif heading == "west":
    heading = "south"
  elif heading == "south":
    heading =  "east"
  elif heading == "east":
    heading = "north"
  return heading  
  

 
