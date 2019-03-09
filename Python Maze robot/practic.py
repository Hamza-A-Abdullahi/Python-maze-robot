import grobot

print('This is a simple user interface where you\ncan control a robot using few simple commands')
print('Commands\nf = Forward\nl = Go Left\nr = Go Right')
h = grobot.NewRobot("Hamza", 2, 2, "Blue")

h.forward() * (5)
