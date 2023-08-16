
def isPalindrome(x: int) -> bool:
    y = [] #O(n) where n is the number of digits
    for num in str(x):
        y.append(num)

    while len(y) >= 0: #O(n/2)
        if len(y) == 1 or len(y) == 0:
            return True
        
        if y[0] == y[len(y)-1]:
            y.pop(0)
            y.pop()
            continue

        return False
    

def isPalindromeString(x: int) -> bool:

    y = str(x)

    while True: #O(n/2)
        if len(y) == 1 or len(y) == 0:
            return True
        
        if y[0] == y[len(y)-1]:
            y = y.replace(y[0],"")
            y = y.replace(y[len(y)-1],"")
            continue

        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(str(x)) == 1 or len(str(x)) == 0:
            return True
        
        if str(x)[0] == str(x)[len(str(x))-1]:
            return self.recursivePalindrome(str(x)[1:len(str(x))-1])
        return False
    
solution = Solution()
print(solution.recursivePalindrome(10001))

            


