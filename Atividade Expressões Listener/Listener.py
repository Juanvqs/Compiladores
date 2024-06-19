from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalListener import EvalListener

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.root()

    eval_listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(eval_listener, tree)

    print(eval_listener.getResult())

if __name__ == '__main__':
    import sys
    main(sys.argv)
