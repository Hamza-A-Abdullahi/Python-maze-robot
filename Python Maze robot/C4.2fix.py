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

def outofBounds(heading,x,y):
  if x + 1 > 30 and heading == "east":
    heading = turnRight(heading)
    heading = turnRight(heading)
  elif x -1 < 1 and heading == "eest":
    heading = turnRight(heading)
    heading = turnRight(heading)
  elif y - 1 <= 0 and heading == "south":
    heading = turnRight(heading)
    heading = turnRight(heading)
  elif y +1 > 30 and heading == "north":
    heading = turnRight(heading)
    heading = turnRight(heading)
  return heading

def forward(x,y,heading):
  print(h.forward())
  if heading == 'north':
    y = y + 1
  elif heading == 'east':
    x = x + 1
  elif heading == 'south':
    y = y - 1
  else:
    x = x - 1
  return (x,y)
  
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

count = 40
while count > 0:
  print()
  print(h.look())
  
  option = str(input('Enter command: '))
  if option == 'f':
    forward(x,y,heading)
    print()
    print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))
    print()
    outofBounds(heading,x,y)
    if h.look() == ['Broken', 'Broken', 'Broken', 'Broken', 'Broken']:
      break
    
  elif option == 'l':
    turnLeft(heading)
    print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))

  elif option == 'r':
    turnRight(heading)
    print('Current heading & location\nHeading: {0}\nx:{1} y:{2}'.format(heading,x,y))

  elif option != 'f' or option != 'l' or option != 'r':
    print()
    print('**ONLY COMMANDS ARE ACCEPTED***')
    print()
    count = count + 1
  count -= 1

  
  

 
