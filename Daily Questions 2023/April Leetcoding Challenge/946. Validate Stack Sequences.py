class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        start = 0
        i = 0
        while i <= len(pushed):
            while len(stack) > 0 and stack[-1] == popped[start]:
                stack.pop()
                start += 1
            if i < len(pushed):
                stack.append(pushed[i])
            i += 1
        return True if len(stack) == 0 else False
