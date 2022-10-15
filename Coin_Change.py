#Time_Complexity: O(m*n)
#Space_Complexity: O(m*n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount+1)] for s in range(len(coins)+1)]    #Initialize a 2 Dimenisonal array as dp with 0s in it 
        
        for j in range(1, amount+1):
            dp[0][j]= amount+1      #For every column in the first row set the value as amount+1 i.e., infinity in this case
            
        for i in range(1, len(coins)+1):    #For every element in the table
            for j in range(amount+1):
                
                if j < coins[i-1]:  #If the incoming coin value is less than the previous row's value then copy all the values from the previous row till the column
                    dp[i][j] = dp[i-1][j]
                    
                else:   #Else set the value as minimum between the sum of 1 and dp[i][j-coins[i-1]] and dp[i-1][j]
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                    
        if dp[-1][-1] == amount+1:      #If the the last element in the tbale is amount +1 then return -1
            return -1
        
        return dp[-1][-1]       #Return the last element in the table
        