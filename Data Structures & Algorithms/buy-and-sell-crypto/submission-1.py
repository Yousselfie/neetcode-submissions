class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers, left starts at first price and right at second
        #Left price should be less than right price
        # if right is less than left, update left to next price
        # store best_max and update it if a new max is found

        best_max=0
        left = 0
        right = 0
        while(right+1 < len(prices)):
            right += 1
            if(prices[right] < prices[left]):
                left = right
            best_max=max(best_max, (prices[right]-prices[left]))

        return best_max


        