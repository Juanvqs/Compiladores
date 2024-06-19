import sys
from antlr4 import *
from miniCLexer import miniCLexer
from miniCParser import miniCParser
from antlr4.tree.Tree import TerminalNodeImpl

def print_tree(tree, level=0):
    if isinstance(tree, TerminalNodeImpl):
        print("  " * level + str(tree))
    else:
        print("  " * level + type(tree).__name__)
        for child in tree.children:
            print_tree(child, level + 1)

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = miniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = miniCParser(stream)
    tree = parser.program()
    print_tree(tree)

if __name__ == '__main__':
    main(sys.argv)
