class Solution:
    # leetcode 540
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            m = left + ((right-left)//2)
            if (m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m+1] != nums[m]):
                return nums[m]

            leftSize = m-1 if nums[m-1] == nums[m] else m

            if leftSize % 2:
                right = m-1
            else:
                left = m+1
