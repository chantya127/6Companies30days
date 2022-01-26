# Question :Find the missing no in string
# Input: num = 9899100102
# Output: 101


# Approach : as the length of the number can be seven only ,so try each and every string upto size 7.
#  Then check if there is any missing number or not.

def missingNumber(string):
    # Code here
    
    size = len(string)

    for l in range(1,7,1):
        
        prev = int(string[:l])
        temp = ""
        
        ptr = l
        flag = 0
        ans = -1
        count = 0
        
        while(ptr < size):
            
            temp += string[ptr]
            # print(prev , temp)
            ptr +=1
            
            if(prev +1 == int(temp)):
                
                prev = int(temp)
                temp = ""
            
            elif (prev+2 == int(temp)):
                # print(prev , temp)
                count +=1
                ans = prev+1
                
                prev = int(temp)
                temp = ""
                
            elif (prev < int(temp)):
                flag = 1
                break

        if (count ==1 and flag ==0):
            break
        
    return ans

if __name__ == '__main__':

    s= "9899100102"
        
    ans = missingNumber(s)
    print(ans)