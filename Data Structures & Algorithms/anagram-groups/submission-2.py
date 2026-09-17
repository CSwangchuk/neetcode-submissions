class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            count = [0]*26
            for char in word:    
                count[ord(char)-ord("a")]+=1
            tup = tuple(count)
            if tup not in freq:
                freq[tup] = [word]
            else:
                freq[tup].append(word)
        lst = list(freq.values())
        return lst

                


        