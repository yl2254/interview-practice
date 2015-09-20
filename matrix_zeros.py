def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    m=len(matrix) #num of rows
    n=len(matrix[0]) #num of colums
    i=1
    first_row=False
    first_col=False
    for a in matrix[0]:
        if a ==0:
            print "should"
            first_row=True
    for b in range(m):
        if matrix[b][0]==0:
            first_col=True
    while i< m:
        j=1
        while j<n:
            
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0
                #j=1
                break
            else:
                j+=1
        i+=1
    for i in range (1,m):
        for j in range(1, n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if first_col:
        for b in range(m):
            matrix[b][0]=0
    if first_row:
        for b in range(n):
            matrix[0][b]=0
            print matrix[0][b]


    return matrix

m=[[1,2,3,0],[2,3,4,5]]
print setZeroes(m)