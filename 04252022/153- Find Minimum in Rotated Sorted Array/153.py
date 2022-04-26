class Solution:
    def findMin(self, nums: List[int]) -> int:
        lef, rig = 0, len(nums) - 1

        while lef < rig:
            mid = lef + (rig - lef) // 2
            if nums[mid] < nums[rig]:
                rig = mid
            else:  # nums[mid] >= nums[rig]
                lef = mid + 1
        return nums[lef]
        # find the minimum value for combing two ascend array
        # binary search
        # turning point devide the two array
        # nums[mid] < nums[rig] (not including equal)--> search left part
        # else(including equal) --> right part