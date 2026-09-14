class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        new_s = ""
        clean_s = ""
        for char in s.lower():
            if char.isalnum():
                stack.append(char)
        for c in s.lower():
            if c.isalnum():
                clean_s +=c
        while stack:
            new_s +=stack.pop()
        
        if new_s == clean_s:
            return True
        else:
            return False
            
        