
def reverse_string(s):
	"""
    :type s: str
    :rtype: str
    """
	words=s.split(" ")
	news=''
	i=len(words)-1
	while i>0:
	    
	    news+=words[i]+' '
	    i-=1

	return news+words[0]

print reverse_string("I am a pig")