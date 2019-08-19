count= 10
nums= []
def la_primera(count):
        for i in range (count):
            nums.insert(0,i) #posittion 0 put i

def la_segunda(count):
    for i in range(count):
        nums.append(i)
    return nums.reverse()

#la_segunda(count)
la_primera(count)
print(nums)
