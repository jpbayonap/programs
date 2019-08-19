import queue

#length
n =int(input("length please :"))
#FIFO vector
s = queue.Queue()
#LIFO vector
t = queue.LifoQueue()

#fill it
for i in range(n):
    s.put(i)

for j in range(n):
    t.put(j)

def result(s):
    while not s.empty():
        print(s.get())
    if s.empty():
        break




print( result(s))
print(result(t))
while not s.empty():
    print(s.get())
