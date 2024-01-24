class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Add one to array of digits
        # Create new array
        # Iterate over array digits to last element
        # Add one to the final digit
        # Convert array to integer, add one, then convert back to list
        # Iterate over array, join them together as a string then convert into an integer
        number = int(''.join(str(i) for i in digits))
        number_plus = number + 1
        new_array = [int(x) for x in str(number_plus)]
        return new_array
