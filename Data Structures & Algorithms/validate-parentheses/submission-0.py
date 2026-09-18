class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            elif not stack or stack.pop() != matching[bracket]:
                return False

        return not stack