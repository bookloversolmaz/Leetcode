class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Two strings needle and haystack
        # Compare two strings, needle in haystack
        # Return index of first ocurrence of needle in haystack
        # Or return -1 if needle not in haystack
        search_string = haystack.find(needle)
        if search_string != -1:
            return search_string
        else:
            return -1