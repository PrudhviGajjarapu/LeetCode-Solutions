#4. Median of Two Sorted Arrays
#https://leetcode.com/problems/median-of-two-sorted-arrays/

Solution1:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n3=sorted(nums1+nums2)
        m = len(n3) // 2
        if len(n3) % 2:
            b=(n3[m]/1.0)
            return b
        else:
            a=(n3[m - 1] + n3[m])/2.0
            return a


Solution2:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from statistics import median
        n3=sorted(nums1+nums2)
        return median(n3)
        

