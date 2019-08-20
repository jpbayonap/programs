#the objective of this programm is to compkute the division of one by a  random integer given by the user
#for repeated decimals the programm will print the repeated digits after reaching the first repetition
from time import sleep # used for defining the  intervals of time between each operation
d= int(input("Input a denominator:"))
print(f"1/{d} is computed")
myli =[0]*(d+1) #this array will play a critical role in the computation
#for any integer d , when we compute the division of it with one by recusion .
mel =[0]*(d+1)
count= 0 # tell us the number of operations carried out
done = False  # condition for finishing the computation
x=1  # first step of the division i.e. how many times is d contained in one  0
e = d//10
s = ""
while not done:

	x= x*10      #because the first quotient is zero we increase it by multiplying it by ten
	quotient= x//d  #how many  integer times can d fit in the increased value of x
	remainder= x%d  # units needed to add to the product of quotient and d for getting x

	print(quotient)
	myli[count]= quotient   #fill the array with the computed quotient
	mel[count] =remainder
	count  += 1   #tells the program to move towards the next operation
	print(f"{count}:{quotient}({remainder})") #show the user the result of the operation
	sleep(0.5)
	  # convert the array into a string in order to get the appropiate enviroment for printing the repeated decimals anwers

	if remainder ==0:  # if there is no units needed to add in the computation , the division is over and it yields a finite answer
		done= True     # stop the computation

	else:     # for other case bring the computation proccess to the next step  by changing the value of the expanded value with the remainder of the
	#previous  step

		x =remainder

	if any([b == remainder for b in mel[:count] ]) : #when computing the division of one and an integer  the values admitted for quotient are restricted
	#to 1,...,d . hence if in the computation  there is two values of quotient which coincide  the entries of myli between them will be repeated

		done= True

my= [str(a)for a in myli]
print("the result is")
print(''.join(my[:count]) + '('+''.join(my[my.index(my[count-1]):count])+')')
