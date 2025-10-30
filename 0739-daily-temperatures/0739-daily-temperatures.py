class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =  [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                iPop = stack[-1]
                diff = i - iPop
                result[iPop] = diff
                stack.pop()
            stack.append(i)
        return result