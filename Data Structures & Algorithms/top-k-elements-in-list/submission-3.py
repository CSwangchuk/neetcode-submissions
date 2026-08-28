class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dect = {}
        for num in nums:
            if num in dect:
                dect[num]+=1
            else:
                dect[num]=1

        ranked = sorted(dect, key=lambda x: dect[x], reverse=True)

        return ranked[:k]
           