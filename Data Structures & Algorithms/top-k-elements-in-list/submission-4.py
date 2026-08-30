class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dect = {}
        count = [[]for i in range(len(nums)+1)]
        for num in nums:
            if num in dect:
                dect[num]+=1
            else:
                dect[num]=1
        
        for value,freq in dect.items():
            count[freq].append(value)
        ans = []
        for i in range(len(nums),0 ,-1):
            for num in count[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
            