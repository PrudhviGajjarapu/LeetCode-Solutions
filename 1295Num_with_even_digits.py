#1295. Find Numbers with Even Number of Digits
#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        b=0
        for i in nums:
            a=len(str(i))
            if a%2==0:
                b+=1
        return b
