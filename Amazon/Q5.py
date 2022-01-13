# Question : Given a list of contacts contact[] of length n where each contact is a string which exist in a phone directory and a query string s.
#  The task is to implement a search query for the phone directory. Run a search query for each prefix p of the query string s (i.e. from  index 1 to |s|) that prints all the distinct contacts which have the same prefix as p in lexicographical increasing order


# Input: 
# n = 3
# contact[] = {"geeikistest", "geeksforgeeks", 
# "geeksfortest"}
# s = "geeips"
# Output:
# geeikistest geeksforgeeks geeksfortest
# geeikistest geeksforgeeks geeksfortest
# geeikistest geeksforgeeks geeksfortest
# geeikistest
# 0
# 0
# Explaination: By running the search query on 
# contact list for "g" we get: "geeikistest", 
# "geeksforgeeks" and "geeksfortest".
# By running the search query on contact list 
# for "ge" we get: "geeikistest" "geeksforgeeks"
# and "geeksfortest".
# By running the search query on contact list 
# for "gee" we get: "geeikistest" "geeksforgeeks"
# and "geeksfortest".
# By running the search query on contact list 
# for "geei" we get: "geeikistest".
# No results found for "geeip", so print "0". 
# No results found for "geeips", so print "0".


# Approach : Use trie to store all the words and go on traversing each character in the string and add all poss words


class node:
    
    def __init__(self):
        
        self.child = {}
        
        self.words = []
        self.end = 1


class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        
        def insert(root ,word):
            
            temp = root
            for ch in word:
                
                if (ch not in temp.child):
                    temp.child[ch] = node()
                
                temp = temp.child[ch]
                temp.words.append(word)
            
            temp.end = 1
        
        def query(root):
            
            ans = []
            flag = 1
            temp = root
            for ch in s:
                
                if (ch not in temp.child) or (flag ==0):
                    ans.append([0])
                    flag = 0

                elif (flag):
                    
                    words = temp.child[ch].words
                    ans.append(words)
                    temp = temp.child[ch]
                    
            res = []
            
            for r in ans:
                
                vis = set()
                curr = []
                for w in sorted(r):
                    
                    if (w not in vis):
                        vis.add(w)
                        curr.append(w)
                
                res.append(curr)
            
            return (res)
                
            
            return (ans)
        
        root = node()
        root.end = 0
        
        for word in contact:
            
            insert(root ,word)
        
        size = len(s)
        
        ans = query(root)
        #print(ans)
        
        return ans
        

if __name__ == '__main__':

    contact= ["geeikistest", "geeksforgeeks", "geeksfortest"]
    s = "geeips"
    obj = Solution()
    ans = obj.displayContacts(len(contact),contact,s)
    
    print(ans)