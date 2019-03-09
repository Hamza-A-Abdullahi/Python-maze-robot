import grobot
import random


hamza = grobot.NewRobot("hamza", 4,3, "Orange")
count = 500
while count > 0:
    f = hamza.look()[2]
    l = hamza.look()[0]
    ld = hamza.look()[1]
    rd = hamza.look()[3]
    r = hamza.look()[4]
    All = [f,l,ld,rd,r]
    print(All)
    if f == 'Wall' and l == None and ld == None and rd == 'Wall' and r == 'Wall':
        n = random.randint(0,1)
        if n == 0:
            print(hamza.left())
            print(hamza.forward())
        else:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward)
    elif f == None and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
        print(hamza.forward())
        print('If statement - 1')
    elif f == None and l == None and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
        n = random.randint(0,2)
        print('Random no:',n)
        if n <= 1:
            print(hamza.forward())
            print('If statement - 2,1')
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 2,2')
    elif f == None and l == None and ld == None and rd == 'Wall' and r == 'Wall':
        n = random.randint(0,3)
        print('Random no:',n)
        if n == 0 or n == 3:
            print(hamza.forward())
            print('If statement - 3,1')
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 3,2')
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 3,3')
    elif f == None and l == None and ld == None and rd == None and r == 'Wall':
        n = random.randint(0,4)
        print('Random no:',n)
        if n == 0 or n == 4:
            print(hamza.forward())
            print('If statement - 4,1')
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 4,2')
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 4,3')
        elif n == 3:
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 4,4')
    elif f == None and l == None and ld == None and rd == None and r == None:
        n = random.randint(0,5)
        print('Random no:',n)
        if n == 0 or n == 5:
            nn = random.randint(1,6)
            print('Random no:',nn)
            if nn == 1:
                print(hamza.forward())
                print('If statement - 5,1')
            elif nn == 2:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    print('If statement - 5,2')
            elif nn == 3:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        print('If statement - 5,3')
            elif nn == 4 and nn == 5 and nn == 6:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        f = hamza.look()[2]
                        if f == None:
                            print(hamza.forward())
                            print('If statement - 5,4')
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 5,2')
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 5,3')
        elif n == 3:
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 5,4')
        elif n == 4:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 5,5')

                
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == None:
        print(hamza.right())
        print(hamza.forward())
        print('If statement - 6')
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == None and r == None:
        n = random.randint(0,1)
        print('Random no:',n)
        if n == 0:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 7,1')
        else:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 7,2')
    elif f == 'Wall' and l == 'Wall' and ld == None and rd == None and r == None:
        n = random.randint(1,2)
        print('Random no:',n)
        if n == 1:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 8,2')
        else:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 8,3')
    elif f == 'Wall' and l == None and ld == None and rd == None and r == None:
         n = random.randint(1,15)
         print('Random no:',n)
         if n < 6:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 9,2')
         elif n > 5 and n < 11:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 9,3')
         else:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 9,4')
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
        hamza.init(random.randint(2,29),random.randint(2,29))
        print(hamza.right())
        print(hamza.right())
        ff = hamza.look()[2]
        print('Forward:',ff)
        nn = random.randint(0,5)
        print('Random no:',nn)
        if nn == 0:
            print(hamza.forward())
            print('If statement - 10,1')
        elif nn == 1:
            print(hamza.forward())
            f = hamza.look()[2]
            if f == None:
                print(hamza.forward())
                print('If statement - 10,2')
        elif nn == 2:
            print(hamza.forward())
            f = hamza.look()[2]
            if f == None:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    print('If statement - 10,3')
        elif nn > 2:
            print(hamza.forward())
            f = hamza.look()[2]
            if f == None:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        print('If statement - 10,4')
            
    
    elif f == None and ld == None and rd == None:
        ran = random.randint(0,3)
        if ran == 0 or ran == 3:
            print(hamza.forward())
            print('If statement - 10,5')
        elif ran == 1:
            if l == None:
                print(hamza.left())
                print(hamza.forward())
                print(hamza.right())
                print(hamza.forward())
                print('If statement - 10,6')
            else:
                print(hamza.forward())
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 10,7')
        elif ran == 2:
            if r == None:
                print(hamza.right())
                print(hamza.forward())
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 10,8')
            else:
                print(hamza.forward())
                print(hamza.right())
                print(hamza.forward())
                print('If statement - 10,9')
    elif r == None and l == None:
        n = random.randint(0,1)
        if n == 0:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 10,10')
        else:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 10,11')
    elif r == None and l == None and f == None:
        n = random.randint(0,3)
        if n == 0:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 10,12')
        elif n == 1 and n == 3:
            print(hamza.forward())
            print('If statement - 10,13')
        else:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 10,14')
    
    elif f == None:
        ran = random.randint(0,2)
        print('Random no:',ran)
        if ran == 0 or ran == 2:
            print(hamza.forward())
            print('If statement - 11')
        elif ran == 1:
            if r == None and l == None:
                nn = random.randint(1,2)
                print('Random no:',nn)
                if nn == 1:
                    print(hamza.right())
                    print(hamza.forward())
                    print('If statement - 11,3')
                elif nn == 2:
                    print(hamza.left())
                    print(hamza.forward())
                    print('If statement - 11,4')
            elif r == None:
                print(hamza.right())
                print(hamza.forward())
                print('If statement - 11,1')
            elif l == None:
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 11,2')
    elif l == None:
        if f and ld == None:
            ran = random.randint(0,10)
            print('Random no:',ran)
            if ran < 6:
                print(hamza.forward())
            else:
                print(hamza.left())
                print(hamza.forward())
                print(hamza.right())
                print(hamza.forward)
        else:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 12')
            
        f = hamza.look()[2]
        l = hamza.look()[0]
        ld = hamza.look()[1]
        rd = hamza.look()[3]
        r = hamza.look()[4]
        print(f,l,ld,rd,r)
        if r == None:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 12,1')
        elif rd == None:
            r = hamza.look()[4]
            if r == None:
                print(hamza.right())
                print(hamza.forward())
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 12,2')
        elif ld == None:
            l = hamza.look()[0]
            if l == None:
                print(hamza.left())
                print(hamza.forward())
                print(hamza.right())
                print(hamza.forward())
                print('If statement - 12,3')
        elif f == None and l == None and ld == None and rd == None and r == None:
            n = random.randint(0,3)
            print('Random no:',n)
            if n == 0:
                nn = random.randint(1,5)
                print('Random no:',nn)
                if nn == 1 :
                    print(hamza.forward())
                    print('If statement - 12,4')
                elif nn == 2:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        print('If statement - 12,5')
                elif nn == 3:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        f = hamza.look()[2]
                        if f == None:
                            print(hamza.forward())
                            print('If statement - 12,6')
                elif nn == 4 or nn == 5:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        f = hamza.look()[2]
                        if f == None:
                            print(hamza.forward())
                            f = hamza.look()[2]
                            if f == None:
                                print(hamza.forward())
                                print('If statement - 12,7') 
    elif ld == None:
        l = hamza.look()[0]
        if l == None:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 13')
    elif rd == None:
        r = hamza.look()[4]
        if r == None:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 14')
    elif r == None:
        print(hamza.right())
        print(hamza.forward())
        print('If statement - 15')

        

    count -= 1
    print(10000-count,'Move')
    print(count,'Moves left')
    

