#You have an array of numbers. 
#For example: [-5, 1, 7, -3, 4] Find the pair with the greatest product.
#In the example above, it would be 28(7x4). 

def max_product(array):
	max=0;
	nextmax=0;
	min=0;
	nextmin=0;
	for i in array:
		if i>max:
			nextmax=max
			max=i
			
		elif i>nextmax:
			nextmax=i

		elif i<min:
			nextmin=min
			min=i
			

		elif i<nextmin:
			nextmin=i
		else:
			continue
	if max*nextmax>min*nextmin:
		print max, nextmax
		return max*nextmax
	else:
		print min, nextmin
		return min*nextmin

i=[0,-1,-2,4,6,-8,-20]
print max_product(i)