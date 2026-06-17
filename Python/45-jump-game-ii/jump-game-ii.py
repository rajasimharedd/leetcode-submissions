class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        start = 0
        current = 0
        n = len(nums)-1
        for i in range(len(nums)-1):
            start = max(start, i+nums[i])
            if i == current:
                count+=1
                current = start
        return count 
