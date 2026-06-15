class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        pairs = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key, val in freq.items():
            pairs.append((val, key))
        pairs.sort(reverse=True)
        for i in range(k):
            res.append(pairs[i][1])
        return res
