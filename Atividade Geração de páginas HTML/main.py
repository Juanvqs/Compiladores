from antlr4 import *
from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from HtmlGeneratorVisitor import HtmlGeneratorVisitor

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = HtmlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HtmlParser(stream)
    tree = parser.html()

    html_generator = HtmlGeneratorVisitor()
    html_content = html_generator.visit(tree)

    with open('output.html', 'w') as file:
        file.write(html_content)

    print("HTML generated successfully in output.html")

if __name__ == '__main__':
    import sys
    main(sys.argv)
