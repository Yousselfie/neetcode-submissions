class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Val : Idx
        for i, num in enumerate(nums):
            difference = target - num
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[num] = i
            