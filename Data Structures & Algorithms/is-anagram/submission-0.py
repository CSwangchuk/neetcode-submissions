class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Understand
        input: two strings 
        output : boolean 
        edge case: empty string either or invalid data type
        logic: check if two strings are anagrams we could use dict 
        Plan
        1. create a func
        2. create a two new dict
        3. make a frequency mapping of the string s and t
        4. compare the two dicts if same then return true else false
        '''
        sdict = {}
        tdict = {}

        for char in s:
            if char in sdict:
                sdict[char]+=1
            else:
                sdict[char]= 1

        for char1 in t:
            if char1 in tdict:
                tdict[char1]+=1
            else:
                tdict[char1]= 1

        if sdict == tdict:
            return True
        else:
            return False