class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in map1:
                return [map1[num_to_find], i]
            map1[nums[i]] = i