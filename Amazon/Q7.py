
# Question : First non-repeating character in a stream 

# Input: A = "aabc"
# Output: "a#bb"
# Explanation: For every character first non
# repeating character is as follow-
# "a" - first non-repeating character is 'a'
# "aa" - no non-repeating character so '#'
# "aab" - first non-repeating character is 'b'
# "aabc" - first non-repeating character is 'b'


# Approach :  Maintain a queue to find the odering of the chars
# also a vis array of size 26 to mark all the characters till now which are visited.

        
#User function Template for python3
from collections import deque

class Solution:
	def FirstNonRepeating(self, s):
	    
		# Code here
		
		ququ = deque()
		
		vis = [0]*(26)
		ans= ""
		for ch in s:
			idx = ord(ch) - ord('a')
			if (vis[idx] == 0):
				vis[idx]=1
				ququ.append(ch)
			else:
				vis[idx] +=1
			
			while(ququ and vis[ord(ququ[0]) - ord('a')]>1):
				ququ.popleft()
			
			if(len(ququ) > 0):
				first = ququ[0]
				ans += first
			
			else:
				ans += "#"
		    
		    
		return ans		


if __name__ == '__main__':

    A = "aabc"
    obj = Solution()
    ans = obj.FirstNonRepeating( A)
    print(ans)