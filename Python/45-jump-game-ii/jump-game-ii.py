class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0 #how far i can reach from current pos
        count = 0 # how many jumps taken so far.
        last_reached = 0 # where did i jump last to. 
        
        if len(nums)==1:
            return 0
        for i in range(len(nums)-1):
            reach = max(reach, i+nums[i])
            
            if i == last_reached:
                last_reached = reach
                count+=1
            
                if reach >= len(nums)-1:
                    return count
