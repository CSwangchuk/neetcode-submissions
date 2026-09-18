class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))+"#"+word
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        start= 0
        while start<len(s):
            move = start
            while s[move]!="#":
                move+=1
            length = int(s[start:move])
            word = s[move+1:length+move+1]
            result.append(word)
            start = length+move+1
        return result
