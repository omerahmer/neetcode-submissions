class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let set1 = new Set();
        for (let i = 0; i < nums.length; i++) {
            let numToFind = target - nums[i]
            if (set1.has(numToFind)) {
                return [i, nums.indexOf(numToFind)];
            }
            set1.add(nums[i])
        }
    }
}
