#1. Two Sum
#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        l=len(nums)
        for _ in range(l):
            for c in range(_+1, l):
                if nums[_]+nums[c]==target:
                    return[_, c]
