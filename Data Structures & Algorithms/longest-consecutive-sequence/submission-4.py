class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist = {}
        longest = 0
        for i in range(len(nums)):
            if nums[i] in exist:
                exist[nums[i]]+=1
            exist[nums[i]]=1
        
        for j in range(len(nums)):
            count=0
            if nums[j] in exist:
                if nums[j]-1 not in exist:
                    for k in range(len(nums)):
                        if nums[j]+k in exist:
                            count+=1
                        else:
                            break
            if count>longest:
                longest = count
        return longest
            
                        
                    
            


    