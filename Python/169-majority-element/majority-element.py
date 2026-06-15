class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        limit = (len(nums)//2) +1
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
            if dict[i] == limit:
                return i