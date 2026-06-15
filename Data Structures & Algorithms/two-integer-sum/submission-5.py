class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, n in enumerate(nums):
            num_to_find = target - n
            if num_to_find in prev_map:
                return [prev_map[num_to_find], i]
            prev_map[n] = i