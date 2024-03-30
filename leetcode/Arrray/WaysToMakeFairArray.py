class Solution:
    # 1664 leetcode
    def waysToMakeFair(self, nums: List[int]) -> int:
        # first calculate even arr
        even = [0] * len(nums)
        odd = [0] * len(nums)

        evenSum = 0
        oddSum = 0
        ans = 0
        for i in range(0, len(nums)):
            if i%2 == 0:
                # if even number increment evensum
                evenSum += nums[i]
            else:
                oddSum += nums[i]

            even[i] = evenSum
            odd[i] = oddSum

        for i in range(0, len(nums)):
            if i == 0:
                nes = odd[len(nums)-1]
                nos = even[len(nums)-1] - nums[0]

                if nes == nos:
                    ans += 1
                continue
            else:
                # when a number is removed, all evens become odd
                # presum remains same, newsum would be presum + ( if its a oddsum, it changes to evensum) viceversa
                nes = even[i-1] + odd[len(nums)-1] - odd[i] 
                nos = odd[i-1] + even[len(nums)-1] - even[i]
                if nes == nos:
                    ans += 1
        return ans
