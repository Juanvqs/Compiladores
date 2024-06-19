from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.root()

    eval_visitor = EvalVisitor()
    result = eval_visitor.visit(tree)

    print(result)

if __name__ == '__main__':
    import sys
    main(sys.argv)
