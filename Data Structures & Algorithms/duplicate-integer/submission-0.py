class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            sub_nums = [x for x in nums if x != num]
            if len(sub_nums) != len(nums)-1:
                return True
        return False