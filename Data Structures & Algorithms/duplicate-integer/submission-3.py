class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dect = {}

        for num in nums:
            if num in dect:
                dect[num]+=1
            else:
                dect[num]=1
        for key,value in dect.items():
            if value >=2:
                return True
        return False
        
        