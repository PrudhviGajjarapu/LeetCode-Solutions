#7. Reverse Integer
#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        if x>=0:
            a=int(y[::-1])
        else:
            a=int(y[:0:-1])
            a=-1*a
        if a in range(-2147483648, 2147483647):
            return a
        else:
            return 0
            