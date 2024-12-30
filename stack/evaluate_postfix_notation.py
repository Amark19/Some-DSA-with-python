class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def perform_operation(op1, op2, operator):
            if operator == "+":
                return op1 + op2
            elif operator == "*":
                return op1 * op2
            elif operator == "-":
                return op1 - op2
            else:
                return int(op1 / op2)

        operators = ['+', '-', '*', '/']
        stack = []
        for val in tokens:
            if val in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                ans = perform_operation(int(op2), int(op1), val)
                stack.append(str(ans))
            else:
                stack.append(val)
        return int(stack[0])
