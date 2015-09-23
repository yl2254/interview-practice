#Write a program that counts from 1 to 100. For each number, display fizz 
#if the number is divisible by 3 and buzz if the number is divisible by 5. 
#The output should be something like: 1 2 3 fizz 4 5 buzz 6 fizz 7 8 9 fizz 10 buzz 11 12 fizz 13 14 15 fizz buzz 

def count(N):
	div_3=0
	div_5=0
	s=""
	for i in range (1, N+1):
		div_3+=1
		div_5+=1
		if div_3==3 and div_5==5:
			div_5=0
			div_3=0
			s+= str(i) +" " + "fizz" +" "+"buzz" +" "
		elif div_5==5:
			div_5=0
			s+= str(i) +" " + "buzz" +" "
		elif div_3==3:
			div_3=0
			s+= str(i) +" " + "fizz" +" "
		else:
			s+=str(i)+" "

	print s

count(15)