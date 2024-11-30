class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from the centre and one pointer left and the other right
        # if the two pointers on either side are the same, continue iterating
        def expand_from_centre(s, left, right):
            while left >= 0 and right< len(s) and s[left] == s[right]:
                # move the pointers across one char at a time
                left -= 1
                right += 1
            # then move back towards the centre
            return s[left + 1:right]
        # if there is more than one
        # find the longest palindrome, considering even and odd length strings
        # this acts as the main loop, as it checks for a substring
        longest_palindrome = ''
        for i in range(len(s)):
            # for odd lenght ps that are symmetrical. i represents the middle char and
            # the starting point      
            pal_odd = expand_from_centre(s, i, i)
            # check even length palindrome, so i if left and right of the centre
            pal_even = expand_from_centre(s, i, i + 1)
            # choose the longest palindrome from the two above
            current_longest = pal_odd if len(pal_odd) > len(pal_even) else pal_even
            # update the current longest
            if len(current_longest) > len(longest_palindrome):
                longest_palindrome = current_longest
        return longest_palindrome