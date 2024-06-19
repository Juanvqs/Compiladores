import math
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):

    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visit(ctx.expr())

    def visitParent(self, ctx:ExprParser.ParentContext):
        return self.visit(ctx.expr())

    def visitPot(self, ctx:ExprParser.PotContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math.pow(left, right)

    def visitMultDiv(self, ctx:ExprParser.MultDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprParser.MUL:
            return left * right
        else:
            return left / right

    def visitSomaSub(self, ctx:ExprParser.SomaSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprParser.PLUS:
            return left + right
        else:
            return left - right

    def visitFunc(self, ctx:ExprParser.FuncContext):
        value = self.visit(ctx.expr())
        if ctx.abs_():
            return abs(value)
        else:
            return math.factorial(int(value))

    def visitNumber(self, ctx:ExprParser.NumberContext):
        num = float(ctx.NUM().getText())
        if ctx.SUB():
            num = -num
        return num
