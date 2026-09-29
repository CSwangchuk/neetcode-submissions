class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums)+1)] 
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num]=1
        
        for key, value in freq.items():
            count[value].append(key)
        ans  = []
        for i in range(len(count)-1,-1,-1):
            for j in range(len(count[i])):
                ans.append(count[i][j])
            if len(ans) == k:
                return ans
        