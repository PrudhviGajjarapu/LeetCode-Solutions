# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Solution1:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        b = []
        for i in range(len(nums)):
            if nums[i] == target:
                b.append(i)
        c = len(b)
        if c == 0:
            b = [-1, -1]
        d = [b[0], b[-1]]
        return d


# Solution2:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        b = []
        for i in range(len(nums)):
            if nums[i] == target:
                f = i
                break
        else:
            return[-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                l = j
                break
        return[f, l]
