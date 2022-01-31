# Question : Remove Colored Pieces if Both Neighbors are the Same Color

# Input: colors = "AAABABB"
# Output: true
# Explanation:
# AAABABB -> AABABB
# Alice moves first.
# She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

# Now it's Bob's turn.
# Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
# Thus, Alice wins, so return true.


# Approach : as we can delete only the middle characters , so count cont.characters
# and if freq is greater than 2 , add frequency of current character.


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        size = len(colors)
        
        count = {"A" :0 , "B" : 0}
        ptr = 0
        
        while(ptr <size):
            
            st  = ptr
            curr = colors[ptr]
            while(ptr < size and colors[ptr] == curr):
                ptr +=1
            
            length = ptr - st
            if (length > 2):
                
                count[curr] += length-2
            
        
        return (count["A"] > count["B"])

if __name__ == '__main__':

    obj = Solution()
    colors = "AAABABB"

    ans = obj.winnerOfGame(colors)
    print(ans)