class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            num_to_get = target - nums[i]
            if num_to_get in nums_map:
                return [nums_map[num_to_get], i]
            nums_map[nums[i]] = i