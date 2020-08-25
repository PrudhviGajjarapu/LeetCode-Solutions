#1281. Subtract the Product and Sum of Digits of an Integer
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=list(map(int, str(n)))
        sum=0
        pro=1
        for _ in range(len(p)):
            pro *= p[_]
            sum += p[_]
        return(pro-sum)
     
