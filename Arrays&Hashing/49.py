Approach 1
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The dictionary to hold our groups. {key: [list_of_anagrams]}
        groups = {}
        
        # Loop through each word in the input list.
        for word in strs:
            # Create the key (a sorted, immutable version of the word).
            key = tuple(sorted(word))
            
            # Check if this key is already in our dictionary.
            if key not in groups:
                # If not, create a new list for this key.
                groups[key] = []
            
            # Append the current word to the list for this key.
            groups[key].append(word)
            
        # After the loop has finished, return all the lists (values) from the dictionary.
        return list(groups.values())

# --- Example ---
solver = Solution()
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solver.groupAnagrams(input_strs))
# Expected Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
Approach 2
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) handles the check for us.
        groups = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            # No 'if' check needed. Just append.
            # If the key is new, an empty list is created automatically before appending.
            groups[key].append(word)
            
        return list(groups.values())
