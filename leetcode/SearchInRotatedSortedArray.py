class Solution:
    #leetcode 33
    def search(self, nums: List[int], target: int) -> int:

        def helper(nums, left, right, target):
            if left> right:
                return -1
            
            mid = left + ((right-left)//2)

            if nums[mid] == target:
                return mid

            # check which half is sorted (lefthalf)
            if nums[mid] >= nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    return helper(nums, left, mid-1,target)
                else:
                    return helper(nums,mid+1,right, target)
            
            else: #right half
                if nums[mid]<=target and target<=nums[right]:
                    return helper(nums,mid+1,right,target)
                else:
                    return helper(nums,left,mid-1, target)

        return helper(nums,0, len(nums)-1,target)
