class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Change in place i.e change original array
        # Array is nums, integer is val
        # Remove val from nums. Order of elements may be changed
        # Return new array and number of elements in array
        while val in nums:
            nums.remove(val)
        print(len(nums)) 

        