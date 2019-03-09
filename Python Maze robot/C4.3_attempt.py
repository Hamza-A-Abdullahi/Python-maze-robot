import grobot
import random
import itertools

hamza = grobot.NewRobot("hamza", 1,1, "Orange")
count = 5
while count > 0:
    f = hamza.look()[2]
    l = hamza.look()[0]
    ld = hamza.look()[1]
    rd = hamza.look()[3]
    r = hamza.look()[4]
    lst_f = [[l,ld,rd,r]]
    print(lst_f)
    for L in range(0, len(lst_f)+1):
        for subset_f in itertools.combinations(lst_f, L):
            print(subset_f)
    if f == None and subset_f == (['Wall', 'Wall', 'Wall', 'Wall']):
        print(hamza.forward())
     
    count -= 1

