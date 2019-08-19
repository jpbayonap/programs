import sys, time
count = 100
i = 0
num = 0

def animation():
    global num
    if num == 0:
        num += 1
        return '[=      ]'
    elif num == 1:
        num += 1
        return '[ =     ]'
    elif num == 2:
        num += 1
        return '[  =    ]'
    elif num == 3:
        num += 1
        return '[   =   ]'
    elif num == 4:
        num += 1
        return '[    =  ]'
    elif num == 5:
        num += 1
        return '[     = ]'
    elif num == 6:
        num += 1
        return '[      =]'
    elif num == 7:
        num += 1
        return '[      =]'
    elif num == 8:
        num += 1
        return '[     = ]'
    elif num == 9:
        num += 1
        return '[    =  ]'
    elif num == 10:
        num += 1
        return '[   =   ]'
    elif num == 11:
        num += 1
        return '[  =    ]'
    elif num == 12:
        num += 1
        return '[ =     ]'
    elif num == 13:
        num = 0
        return '[=      ]'

while i < count:
    sys.stdout.write('\b\b\b')
    sys.stdout.write(animation())
    sys.stdout.flush()
    time.sleep(0.2)
