class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: array
        # output: array of arrays, each array is an anagram
        # for each string, store counts of character
        # res[count].append(string)
        # use dict to store counts of each character
        # if count is the same, it's an anagram, push to array, push array to res
        # chars - char: count
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())