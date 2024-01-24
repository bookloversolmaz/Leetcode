class Solution:
    def isValid(self, s: str) -> bool:
        # Iterate over string and ensure that each bracket type is in the correct pair in the correct order
        stack = []
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != bracket_mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack