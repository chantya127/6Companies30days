# Question :Given an array of strings, return all groups of strings that are anagrams. 
# The groups must be created in order of their appearance in the original array.


# input = ['act', 'god', 'cat', 'dog', 'tac']
# output = [[act cat tac] , [god dog]]

# Approach : As anagram as same characters and order does not matter
#            So use a hashmap with key as sort of word and value as original word.


from collections import defaultdict

class Solution:
    def Anagrams(self, words, n):
        
        # to store words
        mapping = defaultdict(list)
        
        for w in words:
            
            ww = ''.join(sorted(w))
            mapping[ww].append(w)
        
        ans = []
        
        for (key) in mapping.values():
            
            ans.append(key)
        
        return (ans)

if __name__ == '__main__':

    
    words = ['act', 'god', 'cat', 'dog', 'tac']
    size = len(words)

    obj = Solution()
    ans = obj.Anagrams(words,size)
    print(ans)