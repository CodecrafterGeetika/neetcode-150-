import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in a list of numbers.

        Args:
            nums: The input list of integers.
            k: The number of top frequent elements to return.

        Returns:
            A list containing the k most frequent elements.
        """
        # Step 1: Create a frequency map of the numbers.
        # For nums = [1,2,2,3,3,3], this becomes Counter({3: 3, 2: 2, 1: 1}).
        freq_map = Counter(nums)
        
        # Step 2: Use heapq.nlargest to get the k keys with the largest values (frequencies).
        # The `key=freq_map.get` tells nlargest to use the frequency of each number for comparison.
        return heapq.nlargest(k, freq_map.keys(), key=freq_map.get)

# --- Example Usage ---
solver = Solution()
nums = [1, 2, 2, 3, 3, 3]
k = 2
result = solver.topKFrequent(nums, k)
print(f"Input: nums = {nums}, k = {k}")
print(f"Output: {result}")
