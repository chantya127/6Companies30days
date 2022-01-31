# Question :Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row,
#  and each pile has a positive integer number of stones piles[i]



# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we return true.



# Approach : Apply dynamic programming apporach, while alice has choice whether to pick from 
# front or back

class Solution:
    def stoneGame(self, piles):
        
        def solve(left , right):
            
            if (left > right):
                return 0
            
            if (left == right):
                return piles[left]
            
            if (left +1 == right):
                
                return max(piles[left] , piles[right])
            
            v1 = piles[left] + min(solve(left+2 , right) , solve(left+1 , right-1))
            v2 = piles[right] + min(solve(left , right-2) , solve(left + 1 , right-1))
            
            return max(v1,v2)
        
        summe = sum(piles)
        size = len(piles)
        alice = solve(0 , size-1)
        
        bob = summe - alice
        
        return (alice > bob)

if __name__ == '__main__':

    
    piles = [5,3,4,5]
    obj = Solution()
    ans = obj.stoneGame(piles)
    print(ans)

    # done