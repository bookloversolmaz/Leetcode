class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s consists of words and space, so characters
        # Use split to split string into list of words, which are separated by spaces
        # Find the last word in that list, but remeber that the last element could be a space!
        # split by space and convert to list
        # string to list and
        words = s.split()
        # returning last element in list
        if len(words) == 0:
            return 0
        return len(words[-1])

            
            
        