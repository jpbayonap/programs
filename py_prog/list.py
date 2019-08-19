


def cool_range(start, stop,step):
    j= start
    while j< stop :
        yield j
        j += step

a=list(x/10 for x in cool_range(0,11,0.5))
print (a)
