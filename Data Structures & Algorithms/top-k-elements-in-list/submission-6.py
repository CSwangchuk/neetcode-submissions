class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = [[] for i in range(len(nums)+1)]
        freq = {}   
        ans = []
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        for key,value in freq.items():
            index[value].append(key)
            

        for i in range(len(index)-1,0,-1):
            for n in index[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
            



        