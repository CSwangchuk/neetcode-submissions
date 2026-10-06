class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0]*26
        t_count = [0]*26

        if len(s) !=len(t):
            return False
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')]+=1
            t_count[ord(t[i])-ord('a')]+=1
        if s_count == t_count:
            return True
        else:
            return False