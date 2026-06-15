class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for num in nums:
            new_set.add(num)
        if len(new_set) != len(nums):
            return True
        return False