from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

""" Here is the explanation for the code above:
1. We create a set and pass it to the set constructor and then check the length of the set.
2. If the length of the set is equal to the length of the list, then there are no duplicates.
3. If the length of the set is not equal to the length of the list, then there are duplicates. """
