#1470. Shuffle the Array
#https://leetcode.com/problems/shuffle-the-array/

#Solution1:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        b=nums[0:n]
        c=nums[n:n*2]
        ans=[]
        for i in range(n):
            ans.append(b[i])
            ans.append(c[i])
        return ans