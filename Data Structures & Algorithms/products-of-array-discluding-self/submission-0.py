class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # [1, 1, 1, 1]
        # nums = [1, 2, 3, 4]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # [1, 1, 2, 6]
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # [1, 4, 12, 24]
            postfix *= nums[i]
        return res