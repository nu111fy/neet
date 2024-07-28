class Solution:
    def isValid(self, s: str) -> bool:
        hash = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if s[i] != hash[last]:
                    return False
        return len(stack) == 0
