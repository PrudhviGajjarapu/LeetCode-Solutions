#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y=str(x)
        if x>=0:
            a=int(y[::-1])
        else:
            a=int(y[:0:-1])
        return bool(x==a)
        