class Solution:
    def mySqrt(self, x: int) -> int:
        # x is a positive integer
        # Find square root of x
        # Round the answer to the nearest whole number
        return int(floor(sqrt(x)))