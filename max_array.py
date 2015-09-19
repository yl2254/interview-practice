
"""Given two arrays were digits of one array represent a number,maxmise the number by replacing it with elements of second array. 
eg: 
arr={3,1,4,5,6} 
rep={1,9,5,2,3} 

after replacement 
arr={9,5,4,5,6} 
one digit of rep can be used to replace only once."""




def max_array(array1,array2):
	
	array2=sorted(array2)
	print array2
	i=len(array2)-1
	j=0
	while i>=0 and j<len(array1):
		
		if array1[j]<array2[i]:
			array1[j]=array2[i]
			i-=1
			j+=1
		else:
			j+=1

	return array1

a=[3,1,4,5,6]
b=[1,9,5,2,3]
print max_array(a,b)