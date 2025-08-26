'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    res = first + second
                elif token == '-':
                    res = first - second
                elif token == '*':
                    res = first * second
                else:
                    res = first / second
                    if res < 0:
                        res = math.ceil(res)
                    else: 
                        res = math.floor(res)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()