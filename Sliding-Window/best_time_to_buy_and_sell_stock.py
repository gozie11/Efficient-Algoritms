class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # This is what we're looking for in this problem.
        min_buy = float('inf') # This is the attribute that will be used to update the tail end of our sliding window.

        for element in prices:
            if element < min_buy:
                min_buy = element #move the sliding window up the the smallest element so far.
            else:
                profit = max(profit, (element - min_buy)) # calculate a new profit
        return profit

  #This implementation has a BigO runtime of O(n). n is the number of prices.
  # Space complexity : O(1) becasue we don't use any additional data structures or stack frames.
