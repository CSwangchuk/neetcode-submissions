class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dect = {}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord("a")]+=1
            tup = tuple(count)
            if tup in dect:
                dect[tup].append(word)
            else:
                dect[tup] = [word]
        lst = list(dect.values())
        return lst
            