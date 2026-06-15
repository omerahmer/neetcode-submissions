from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 # to map a to 0, b to 1, etc
            
            key = tuple(count) # to make it immutable
            # key : value
            anagrams_dict[key].append(s) # key is the frequency of certain letters for a given word
            # [0, 1, 0, 1, 0, 0, 0, 1...] : [bdh, dbh, hbd, ...]
        return anagrams_dict.values()