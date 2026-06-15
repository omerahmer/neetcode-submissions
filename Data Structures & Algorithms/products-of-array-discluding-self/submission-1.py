class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            # [1,2,4,6]
            res[i] = prefix # [1,1,2,8]
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # [48,24,12,8]
            postfix *= nums[i]
        return res