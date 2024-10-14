# 2530. Maximal Score After Applying K Operations

# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

# In one operation:

# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.

# The ceiling function ceil(val) is the least integer greater than or equal to val.

#Code:

import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Max-heap (we negate values to simulate max-heap behavior)
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        
        score = 0
        
        # Perform k operations
        for _ in range(k):
            # Get the largest element (by negating to retrieve the max)
            maxVal = -heapq.heappop(maxHeap)
            
            # Add to the score
            score += maxVal
            
            # Replace the element with ceil(maxVal / 3)
            heapq.heappush(maxHeap, -math.ceil(maxVal / 3))
        
        return score
