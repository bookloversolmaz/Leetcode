class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window algorithm
        # use two pointers, each pointed to the first two characters
        # move the right pointer along the string, until it meets a character that is has     already met
        # then move the left pointer, and starter the process again with the right pointer
        # check each substring to see if it has a greater number of character than the first substring

        # Create dictionary to keep track of the indices of characters that we have seen before
        # Key character, value, last known index
        repeat = {}
        # left pointer starts at first character in the string
        left = 0
        # initialise length to 0, which contains lenght of longest substring encountered
        length = 0
        # loop through entire string using right, the right pointer
        for right in range(len(s)):
            # Adding character at right index, call this char
            char = s[right]
            # if character seen before AND its last known position is greater than or equal to the index
            # left: means to start a slice from the left pointer
            if char in repeat and repeat[char] >= left:
                # if true, then the left index needs to be moved up by one from its last known index
                # repeat[char] = right is updated with the value of the latest index for the repeated character
                left = repeat[char] + 1
            # else find the length of the substring by finding the length of the right pointer minus left pointer plus one 
            else:
                # this will be used to update length, which stores the maximum length variable. Right and left is the index!
                length = max(length, right - left + 1)
            # At the end of each loop, record the position of the character we just added
            # for instance in string of 'abcadd' the values below will be a:0
            repeat[char] = right
        # After going through loop once, return the length, which stored the value of the greatest substring
        return length 


