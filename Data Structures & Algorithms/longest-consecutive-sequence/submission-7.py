class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        #sort the array
        nums.sort()
        count = 1
        counts = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                counts.append(count)
                count = 1

        #append last count
        counts.append(count)
        
        if len(counts) > 1:
            return max(counts)
        return counts[0]