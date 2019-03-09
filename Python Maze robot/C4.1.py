import grobot

print('This is a simple user interface where you\ncan control a robot using few simple commands')
print('Commands\nf = Forward\nl = Go Left\nr = Go Right')
h = grobot.NewRobot("Hamza", 2, 2, "Red")
count = 100
while count > 0:
  print(h.look())
  option = str(input('Enter command: '))
  if option == 'f':
    print(h.forward())
    if h.look() == ['Broken', 'Broken', 'Broken', 'Broken', 'Broken']:
      break
  elif option == 'l':
    print(h.left())
  elif option == 'r':
    print(h.right())
  elif option != 'Up' or option != 'Left' or option != 'Right':
    print()
    print('**ONLY COMMANDS ARE ACCEPTED***')
    print()
    count = count + 1
  count -= 1

  


