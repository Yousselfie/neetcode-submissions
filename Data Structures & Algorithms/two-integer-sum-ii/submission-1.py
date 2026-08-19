class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #pointer on first element and pointer on last
        #if the sum is bigger than the target, move the second pointer to the left
        #if the sum is smaller than the target, move the first pointer to the right
        #return the indices each incremented by one
        left = 0
        right = len(numbers)-1
        
        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]

        