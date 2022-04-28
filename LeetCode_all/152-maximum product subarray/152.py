class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]
        max_so_far = maxp
        min_so_far = maxp

        for i in range(1, len(nums)):
            current = nums[i]
            tem = max(current, max_so_far * current, min_so_far * current)
            min_so_far = min(current, max_so_far * current, min_so_far * current)

            max_so_far = tem

            maxp = max(maxp, max_so_far)

        return maxp