class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert string a and b to binary
        # Add the binary strings together
        # Convert string to int with base 2, as binary is base 1 (0,1), then convert to binary
        c = bin(int(a, 2) + int(b, 2))
        # [2:] means to slice off first two elements, which are 0b
        string_c = (c[2:])
        return str(string_c)