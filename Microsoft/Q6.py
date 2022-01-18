# Question : Given a keypad as shown in the diagram, and an N digit number which is represented by array a[ ], the task 
# is to list all words which are possible by pressing these numbers.


# Input: N = 3, a[] = {2, 3, 4}
# Output:
# adg adh adi aeg aeh aei afg afh afi 
# bdg bdh bdi beg beh bei bfg bfh bfi 
# cdg cdh cdi ceg ceh cei cfg cfh cfi 
# Explanation: When we press 2,3,4 then 
# adg, adh, adi, ... cfi are the list of 
# possible words.


# Approach : Use recursion and go on adding all the characters in the current path.


dd = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]

class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,arr,n):
        #Your code here
        
        def solve(ptr , path):
            
            if (ptr == n):
                ans.append(path)
                
                return 
            
            idx = arr[ptr]
            curr_words = dd[idx]
            
            for w in curr_words:
                solve(ptr+1 , path+w)
        
        ans = []
        
        solve(0,'')
        return ans
        

if __name__ == '__main__':

    arr = [2,3,4]
    n = len(arr)
    obj = Solution()
    ans = obj.possibleWords(arr,n)
    
    print(ans)