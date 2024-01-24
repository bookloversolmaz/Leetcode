from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Remove duplicate values but leave the list in the same order
        # Create a new array
        nums[:]  = sorted(set(nums))
        print(nums)
        # Return the number of elements in the new list
        return(len(nums))