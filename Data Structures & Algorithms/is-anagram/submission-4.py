class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = [0]*26
        count_t = [0]*26
        if len(s)!=len(t):
            return False
        
        for char in s:
            count_s[ord(char)-ord("a")]+=1

        for char in t:
            count_t[ord(char)-ord("a")]+=1

        if count_s !=count_t:
            return False
        else:
            return True

        