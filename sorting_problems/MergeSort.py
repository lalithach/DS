class Solution:
     # leetcode 912
    def sortArray(self, nums: List[int]) -> List[int]:

        # doing in place without taking another
        def merge(nums, Left, Mid, Right):
            leftArr = nums[Left: Mid+1]
            RightArr = nums[Mid+1: Right+1]
            i, j, k = Left, 0, 0
            while j < len(leftArr) and k < len(RightArr):
                if leftArr[j] <= RightArr[k]:
                    nums[i] = leftArr[j]
                    j += 1
                else:
                    nums[i] = RightArr[k]
                    k += 1
                i += 1
            
            while j < len(leftArr):
                nums[i] = leftArr[j]
                i+=1
                j+=1
            
            while k < len(RightArr):
                nums[i] = RightArr[k]
                i+=1
                k+=1

        def mergeSort(nums, left, right):
            if left == right:
                return nums
            
            m = left + ((right-left)//2)
            mergeSort(nums, left, m)
            mergeSort(nums, m + 1, right)
            merge(nums, left, m, right)
            return nums
        return mergeSort(nums, 0, len(nums)-1) 
