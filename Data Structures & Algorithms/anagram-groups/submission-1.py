class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord("a")]+=1
            tup = tuple(count)
            
            if tup in freq:
                freq[tup].append(word)
            else:
                freq[tup] = [word]
            
                
        lst = list(freq.values())
        return lst
        
    