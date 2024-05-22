from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.appendleft(c)
            else:
                if len(stack)  > 0 :
                    if c == ')' and stack[0] != '(':
                        return False
                    elif c == ']' and stack[0] != '[':
                        return False
                    elif c == '}' and stack[0]!='{':
                        return False
                    stack.popleft()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
