class Solution:
    operations = {
            '+':lambda a,b: a + b, 
            '-':lambda a,b: a - b,
            '*':lambda a,b: a * b,
            '/':lambda a,b: int(a / b),
        }
    operands = set(operations.keys())
    @staticmethod
    def evaluate(num1:int,num2:int,operand:str)-> int:
        return Solution.operations[operand](num1,num2)
    def evalRPN(self, tokens: List[str]) -> int:
        operands = Solution.operands
        evaluate = Solution.evaluate
        stack = []
        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = evaluate(num1,num2,t)
                stack.append(result)
        return stack[0]