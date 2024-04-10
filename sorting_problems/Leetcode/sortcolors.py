# leetcode 75
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = -1
        white = -1
        for blue in range(len(nums)):
            if nums[blue] == 1:
                white +=1
                nums[blue], nums[white] = nums[white], nums[blue]
            elif nums[blue] == 0:
                white +=1
                nums[blue], nums[white] = nums[white], nums[blue]
                red +=1
                nums[red], nums[white] = nums[white], nums[red]
        return nums
