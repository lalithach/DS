class Solution:
    # Leetcode 724
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(0, len(nums)):
            pivot = nums[i]
            # keep adding i to the leftsum
            leftSum += nums[i-1] if i> 0 else 0
            # subtracting pivot and leftsum from total would give rightsum
            rightSum = total-leftSum-pivot
            if leftSum == rightSum:
                return i
        return -1    
