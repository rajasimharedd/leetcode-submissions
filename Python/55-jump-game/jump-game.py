class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        start = 0

        for each in nums:
            if start<0:
                return False

            elif each > start:
                start = each
            start -= 1
            
        return True