#Time_Complexity: O(m*n)
#Space_Complexity: O(m*n)

def knapSack(val, weight, m, n):
    dp = [[0 for _ in range(m+1)] for s in range(n+1)]  #Initialize a 2 Dimenisonal array as dp with 0s in it 
    
    for i in range(1,n+1):  
        for j in range(m+1):
            
            if j < weight[i-1]:     #If the incoming weught is less than the previous weight then copy all the values from the previous row till that column
                dp[i][j] = dp[i-1][j-1]
                
            else:   #Else insert the maximum between the sum of val[i-1], dp[i-1][j-weight[i-1]] and dp[i-1][j]
                dp[i][j] = max(val[i-1]+dp[i-1][j-weight[i-1]], dp[i-1][j])
                
    return dp[-1][-1]   #Return the last element in the table that gives the maximum value
    
    
    
    
    
    
    
    
    
    
    
val = [1,4,5,7]
weight = [1,3,4,5]
m = 7
n= len(val)
print(knapSack(val, weight, m, n))