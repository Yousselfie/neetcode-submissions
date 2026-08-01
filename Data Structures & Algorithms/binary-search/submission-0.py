class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # split list in half:
        # check the middle num, if it is greater than the target, search the left half. if lesser, search the right half, if equal, return it
        middle_index = len(nums)//2
        middle_num = nums[middle_index]
        if (middle_num == target): return middle_index
        elif (middle_num > target):
            #check left
            for i in range(0, middle_index):
                if (nums[i] == target): return i
        else:
            #check right
            for i in range(middle_index, len(nums)):
                if (nums[i] == target): return i
        return -1
        