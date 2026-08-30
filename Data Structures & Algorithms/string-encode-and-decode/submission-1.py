class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for word in strs:
            new_str+= f"{len(word)}#{word}"
        return new_str


    def decode(self, s: str) -> List[str]:
        i = 0
        result=[]
        while i<len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i = j+1+length
        return result
