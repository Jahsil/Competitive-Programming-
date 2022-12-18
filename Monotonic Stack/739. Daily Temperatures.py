class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        temp.reverse()
        print(temp)
        ans = []
        stack = []

        for i , t in enumerate(temp):
            
            while len(stack) > 0 and stack[-1][1] <= t:
                stack.pop()

            if len(stack) == 0:
                ans.append(0)
            else:
                ans.append(i - stack[-1][0])
            
            stack.append((i , t))

        ans.reverse()
        return ans
