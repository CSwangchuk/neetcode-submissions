class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Understand
        input: array of integers(list)
        output: boolean (true or false)
        edge cases: empty list, invalid datat type
        logic : using dict we can find the frequency and return true if it occurs more than once

        Plan
        1. creat a function 
        2. make an empty dict
        3. loop through the lst
        4. add the element to the dict as a key and the value being the times it occurs
        5.loop through the dict and check if any value is more than one
        if yes 
        return true
        if no 
        return false
        
        # brute force method
        for i in range(len(nums)-1):
                for j in range(i+1,len(nums)-1):
                    if i ==j:
                        return True
            return False
        s = set()
        for num in nums:
            if num in s :
                return True
            s.add(num)
        return False

        
        '''
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1

        for key, value in d.items():
            if value>1:
                return True
        return False
       
        
        
        