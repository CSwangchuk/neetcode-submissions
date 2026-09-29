class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord("a")]+=1
            tup = tuple(count)
            if tup in ana:
                ana[tup].append(word)
            else:
                ana[tup] = [word]
        ans = list(ana.values())
        return ans


        
        