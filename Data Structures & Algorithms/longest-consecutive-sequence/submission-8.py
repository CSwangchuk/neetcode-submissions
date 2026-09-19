class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = {}
        longest = 0
        for num in nums:
            exists[num]=1


        count = 0
        for i in range(len(nums)):
            local_count = 0
            if nums[i]-1 not in exists:
                local_count+=1
                while(nums[i]+local_count) in exists:
                    local_count+=1
                longest = max(local_count,longest)
        return longest
            

        