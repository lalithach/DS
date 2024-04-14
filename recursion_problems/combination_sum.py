class Solution:
    # leetcode 39
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        globalArray = []
        def helper(index, slate, slateSum):
            #backtracking cases 
            if slateSum == target:
                globalArray.append(slate[:])
                return
            if slateSum > target:
                return

            # leaf
            if index == len(candidates):
                return

            #internal node worker
            # include
            slate.append(candidates[index])
            # we are not incrementing index because, we want unlimited no of times
            helper(index, slate, slateSum+ candidates[index])
            slate.pop()
            # exclude
            helper(index+1, slate, slateSum)
        helper(0, [], 0)
        return globalArray
