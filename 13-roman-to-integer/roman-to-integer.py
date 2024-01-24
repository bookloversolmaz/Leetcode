class Solution:
    def romanToInt(self, s: str) -> int:
        # create dictionary of roman numberals paired to digits
        roman_to_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        IV = 5
        IX = 9
        XL = 50
        XC = 90
        CD = 500
        CM = 900
        # Replace the exceptions with their roman counterpart
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # create for loop that iterates over s and adds the number from dictionary
        for char in s:
            number += roman_to_numerals[char]
        return number

        
        # add the values together
