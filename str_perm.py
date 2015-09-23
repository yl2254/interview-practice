def permute(self, s):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if s == None:
            return []
        if len(s)==1:
            return [s]
        if len(s)==2:
    		s2=[s[1],s[0]]
    		if s2==s:
    			return [s]
    		else:
    			return [s,s2]
    	else:
    		new_list=[]
    		for i in range(len(s)):
    			perm_list=permute(s[:i] + s[i+1:])
    			
    			#print perm_list, i
    			for p in perm_list:
    			    #print p
    			    n1=[s[i]]+p
    			    #print n1
    			    n2=p+[s[i]]
    			    if n1 not in new_list:
    					new_list.append(n1)
    			    if n2 not in new_list:
    					new_list.append(n2)
    			   
    		return new_list
  


s="all"
print permute(s)