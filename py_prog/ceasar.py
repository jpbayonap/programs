text= input("Enter the message:")
code= list(text.encode("ascii")) #encode the message in ascii language
k= int(input("enter k:"))  # the parameter to be applyed  on the code

def enc(k,code):  # encoding function
	for i in range(len(code)): #check  for all elements in the array code
	#ascii for a = 97 ,ascii for z=122
		if code[i] >=97 and code[i] <=122-k:  # check the ascii value for the i element
			code[i]= code[i] +k               # if this value is k units less than  z ascii code  the encription is simply adding k units

		if code[i]>122 -k and code[i] <=122: # if the value is k not in the previous range addition of k units will return a value outside the alphabet
			code[i] = 97+ (code[i]+k -122)   #to solve this we find the distance  between the previous interval  and the value to be coded (code[i]+k-122)
                                             # this difference the amount of digits to be added in the first
	return code

codex=[str(a)for a in code]  #change the integer values into a string  in order for printing the answer


print( ','.join(codex)) #, is used to differenciate each values cypher
