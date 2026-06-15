class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            j = i
            while (s[j] != "#"):
                j += 1
            length = int(s[i:j]) # i = 0, j = 1, length = 4
            strings.append(s[j + 1 : j + 1 + length]) # start after #, end after length
            i = j + 1 + length
        return strings
