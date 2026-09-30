class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = {}
        
        for num in nums:
            if num in store:
                store[num]+=1
            else :
                store[num] = 1
        
        longest = 0
        for i in range(len(nums)):
            count = 0
            if nums[i]-1 not in store:
                j = 0
                while nums[i] + j in store:
                    count+=1
                    j+=1
                longest = max(longest,count)
            
        return longest
            

        