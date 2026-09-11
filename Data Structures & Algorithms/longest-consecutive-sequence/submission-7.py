class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist = {}
        longest = 0
        for i in range(len(nums)):
            exist[nums[i]]=1
        
        for num in exist:
            count=1
            if num-1 not in exist:
                current = 1
                while num + current in exist:
                    count += 1
                    current += 1
            if count>longest:
                longest = count
        return longest
            
                        
                    
            


    