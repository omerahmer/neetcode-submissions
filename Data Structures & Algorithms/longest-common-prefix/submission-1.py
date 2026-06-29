class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s[i]
        return res"""
        res = strs[0]
        for s in strs[1:]:
            for i in range(len(strs[0])):
                i = 0
                while i < len(res) and i < len(s) and res[i] == s[i]:
                    i += 1
                res = res[:i]
        return res