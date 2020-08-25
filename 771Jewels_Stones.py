#771. Jewels and Stones
#https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        b=0
        for g in J:
            for h in S:
                if g==h:
                    b+=1
        return b
            
