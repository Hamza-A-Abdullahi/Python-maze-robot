import grobot
import random


hamza = grobot.NewRobot("hamza", 2,2, "Orange")
count = 20
iff1 = 0
iff2 = 0
iff3 = 0
iff4 = 0
iff5 = 0
iff6 = 0
iff7 = 0
iff8 = 0
iff9 = 0
iff10 = 0
iff11 = 0
iff12 = 0
iff13 = 0
iff14 = 0
iff15 = 0
iff15 = 0
iff16 = 0
iff17 = 0
iff18 = 0
iff19 = 0
iff20 = 0
iff21 = 0
iff22 = 0
iff23 = 0
iff24 = 0
iff25 = 0
iff26 = 0
iff27 = 0
iff28 = 0
iff29 = 0
iff30 = 0
iff31 = 0
iff32 = 0
iff33 = 0
iff34 = 0
iff35 = 0
iff36 = 0
iff37 = 0
iff38 = 0
iff39 = 0
iff40 = 0
iff41 = 0
iff42 = 0
iff43 = 0
iff44 = 0
iff45 = 0
iff46 = 0
iff47 = 0
iff48 = 0
iff49 = 0
iff50 = 0
while count > 0:
    f = hamza.look()[2]
    l = hamza.look()[0]
    ld = hamza.look()[1]
    rd = hamza.look()[3]
    r = hamza.look()[4]
    All = [f,l,ld,rd,r]
    print(All)
    
    if f == None and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
        print(hamza.forward())
        print('If statement - 1')
        iff1 = iff1 + 1
    elif f == None and l == None and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
        n = random.randint(0,1)
        print('Random no:',n)
        if n == 0:
            print(hamza.forward())
            print('If statement - 2,1')
            iff2 = iff2 + 1
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 3')
            iff3 = iff3 + 1
    elif f == None and l == None and ld == None and rd == 'Wall' and r == 'Wall':
        n = random.randint(0,2)
        print('Random no:',n)
        if n == 0:
            print(hamza.forward())
            print('If statement - 4')
            iff4 = iff4 + 1
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 5')
            iff5 = iff5 + 1
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 6')
            iff6 = iff6 + 1
    elif f == None and l == None and ld == None and rd == None and r == 'Wall':
        n = random.randint(0,3)
        print('Random no:',n)
        if n == 0:
            print(hamza.forward())
            print('If statement - 7')
            iff7 = iff7 + 1
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 8')
            iff8 = iff8 + 1
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 9')
            iff9 = iff9 + 1
        elif n == 3:
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 10')
            iff10 = iff10 + 1
    elif f == None and l == None and ld == None and rd == None and r == None:
        n = random.randint(0,4)
        print('Random no:',n)
        if n == 0:
            nn = random.randint(1,4)
            print('Random no:',nn)
            if nn == 1:
                print(hamza.forward())
                print('If statement - 11')
                iff11 = iff11 + 1
            elif nn == 2:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    print('If statement - 12')
                    iff12 = iff12 + 1
            elif nn == 3:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        print('If statement - 13')
                        iff13 = iff13 + 1
            elif nn == 4:
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
                            print('If statement - 14')
                            iff14 = iff14 + 1
        elif n == 1:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 15')
            iff15 = iff15 + 1
        elif n == 2:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 16')
            iff16 = iff16 + 1
        elif n == 3:
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 17')
            iff17 = iff17 + 1
        elif n == 4:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 18')
            iff18 = iff18 + 1

                
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == None:
        print(hamza.right())
        print(hamza.forward())
        print('If statement - 19')
        iff19 = iff19 + 1
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == None and r == None:
        n = random.randint(0,1)
        print('Random no:',n)
        if n == 0:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 20')
            iff20 = iff20 + 1
        else:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 21')
            iff21 = iff21 + 1
    elif f == 'Wall' and l == 'Wall' and ld == None and rd == None and r == None:
        n = random.randint(0,2)
        print('Random no:',n)
        if n == 0:
            ff = hamza.look()[2]
            print(ff)
            print('If statement - 22')
            iff22 = iff22 + 1
            if ff == None:
                print(hamza.forward())
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 23')
                iff23 = iff23 + 1
        elif n == 1:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 24')
            iff24 = iff24 + 1
        else:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 25')
            iff25 = iff25 + 1
    elif f == 'Wall' and l == None and ld == None and rd == None and r == None:
         n = random.randint(0,3)
         print('Random no:',n)
         if n == 0:
            ff = hamza.look()[2]
            print(ff)
            print('If statement - 26')
            iff26 = iff26 + 1
            if ff == None:
                print(hamza.forward())
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 27')
                iff27 = iff27 + 1
         elif n == 1:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 28')
            iff28 = iff28 + 1
         elif r == 2:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 29')
            iff29 = iff29 + 1
         else:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 30')
            iff30 = iff30 + 1
    elif f == 'Wall' and l == 'Wall' and ld == 'Wall' and rd == 'Wall' and r == 'Wall':
        print(hamza.right())
        print(hamza.right())
        ff = hamza.look()[2]
        print('Forward:',ff)
        nn = random.randint(1,4)
        print('Random no:',nn)
        if nn == 1:
            print(hamza.forward())
            print('If statement - 31')
            iff31 = iff31 + 1
        elif nn == 2:
            print(hamza.forward())
            f = hamza.look()[2]
            if f == None:
                print(hamza.forward())
                print('If statement - 32')
                iff32 = iff32 + 1
        elif nn == 3:
            print(hamza.forward())
            f = hamza.look()[2]
            if f == None:
                print(hamza.forward())
                f = hamza.look()[2]
                if f == None:
                    print(hamza.forward())
                    print('If statement - 33')
                    iff33 = iff33 + 1
        elif nn == 4:
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
                        print('If statement - 34')
                        iff134 = iff34 + 1
            
    

    elif f == None:
        ran = random.randint(0,1)
        print('Random no:',ran)
        if ran == 0:
            print(hamza.forward())
            print('If statement - 35')
            iff35 = iff35 + 1
        elif ran == 1:
            rr = hamza.look()[4]
            ll = hamza.look()[0]
            if rr == None and ll == None:
                nn = random.randint(1,2)
                print('Random no:',nn)
                if nn == 1:
                    print(hamza.right())
                    print(hamza.forward())
                    print('If statement - 38')
                    iff38 = iff38 + 1
                elif nn == 2:
                    print(hamza.left())
                    print(hamza.forward())
                    print('If statement - 39')
                    iff39 = iff39 + 1
            elif rr == None:
                print(hamza.right())
                print(hamza.forward())
                print('If statement - 36')
                iff36 = iff36 + 1
            elif ll == None:
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 37')
                iff37 = iff37 + 1
    elif l == None:
        if f and ld == None:
            ran = random.randint(0,2)
            print('Random no:',ran)
            if ran == 0 or ran == 1:
                print(hamza.forward())
            else:
                print(hamza.left())
                print(hamza.forward())
                print(hamza.right())
                print(hamza.forward)
        else:
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 40')
        iff40 = iff40 + 1
        f = hamza.look()[2]
        l = hamza.look()[0]
        ld = hamza.look()[1]
        rd = hamza.look()[3]
        r = hamza.look()[4]
        print(f,l,ld,rd,r)
        if r == None:
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 41')
            iff41 = iff41 + 1
        elif rd == None:
            r = hamza.look()[4]
            if r == None:
                print(hamza.right())
                print(hamza.forward())
                print(hamza.left())
                print(hamza.forward())
                print('If statement - 42')
                iff42 = iff42 + 1
        elif ld == None:
            l = hamza.look()[0]
            if l == None:
                print(hamza.left())
                print(hamza.forward())
                print(hamza.right())
                print(hamza.forward())
                print('If statement - 43')
                iff43 = iff43 + 1
        elif f == None and l == None and ld == None and rd == None and r == None:
            n = random.randint(0,4)
            print('Random no:',n)
            if n == 0:
                nn = random.randint(1,4)
                print('Random no:',nn)
                if nn == 1:
                    print(hamza.forward())
                    print('If statement - 44')
                    iff44 = iff44 + 1
                elif nn == 2:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        print('If statement - 45')
                        iff45 = iff45 + 1
                elif nn == 3:
                    print(hamza.forward())
                    f = hamza.look()[2]
                    if f == None:
                        print(hamza.forward())
                        f = hamza.look()[2]
                        if f == None:
                            print(hamza.forward())
                            print('If statement - 46')
                            iff46 = iff46 + 1
                elif nn == 4:
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
                                print('If statement - 47')
                                iff47 = iff47 + 1
    elif ld == None:
        l = hamza.look()[0]
        if l == None:
            print(hamza.left())
            print(hamza.forward())
            print(hamza.right())
            print(hamza.forward())
            print('If statement - 48')
            iff48 = iff48 + 1
    elif rd == None:
        r = hamza.look()[4]
        if r == None:
            print(hamza.right())
            print(hamza.forward())
            print(hamza.left())
            print(hamza.forward())
            print('If statement - 49')
            iff49 = iff49 + 1
    elif r == None:
        print(hamza.right())
        print(hamza.forward())
        print('If statement - 50')
        iff5 = iff50 + 1

        

    count -= 1
    print(1000-count,'Move')
    print(count,'Moves left')
    
print(iff1,iff2,iff3,iff4,iff5,iff6,iff7,iff8,iff9,iff10,iff11,iff12,iff13,iff14,iff15,iff15,iff16,iff17,iff18,iff19,iff20,iff21,iff22,iff23,iff24,iff25,iff26,iff27,iff28,iff29,iff30,iff31,iff32,iff33,iff34,iff35,iff36,iff37,iff38,iff39,iff40,iff41,iff42,iff43,iff44,iff45,iff46,iff47,iff48,iff49,iff50) 
