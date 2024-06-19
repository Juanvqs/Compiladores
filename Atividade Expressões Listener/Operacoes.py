from ExprParser import ExprParser
from ExprListener import ExprListener
import math

class EvalListener(ExprListener):
    def __init__(self):
        self.stack = []

    def exitParent(self, ctx:ExprParser.ParentContext):
        pass

    def exitPot(self, ctx:ExprParser.PotContext):
        right = self.stack.pop()
        left = self.stack.pop()
        self.stack.append(math.pow(left, right))

    def exitMultDiv(self, ctx:ExprParser.MultDivContext):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.op.type == ExprParser.MUL:
            self.stack.append(left * right)
        else:
            self.stack.append(left / right)

    def exitSomaSub(self, ctx:ExprParser.SomaSubContext):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.op.type == ExprParser.PLUS:
            self.stack.append(left + right)
        else:
            self.stack.append(left - right)

    def exitFunc(self, ctx:ExprParser.FuncContext):
        value = self.stack.pop()
        if ctx.abs_():
            self.stack.append(abs(value))
        else:
            self.stack.append(math.factorial(int(value)))

    def exitNumber(self, ctx:ExprParser.NumberContext):
        num = float(ctx.NUM().getText())
        if ctx.SUB():
            num = -num
        self.stack.append(num)

    def getResult(self):
        return self.stack[0] if self.stack else None
