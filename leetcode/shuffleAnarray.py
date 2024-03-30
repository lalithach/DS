class Solution:
    # leetcode 384
    def __init__(self, nums: List[int]):
        self.original = nums
        self.size = len(nums)        

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        src = self.original[:]
        for i in range(self.size-1, -1, -1):
            randIdx = random.randint(0, i)
            src[i], src[randIdx] = src[randIdx], src[i]
        return src
