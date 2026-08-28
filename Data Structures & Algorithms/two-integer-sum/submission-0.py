class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Understand
        input: list and a target (int)
        output: indices of the sum of target (list)
        edge cases: empty list, invalide target
        logic: find the two elemnets which added up give the target 

        plan
        1. create a function
        2. create an empty dict
        3. iterate throught the lsit 
        4. check if a pair exists
        5. return the list of index answer
        '''
        d = {}
        lst= []
        for i,num in enumerate(nums):
            diff = target - num
            if diff in d:
                lst.append(d[diff])
                lst.append(i)
                return lst 
            d[num] = i
                        

            