from antlr4 import *
from URLLexer import URLLexer
from URLParser import URLParser

class URLPrintListener(URLParser.Listener):
    def enterUrl(self, ctx):
        print("URL:")
    
    def exitProtocolo(self, ctx):
        print("Protocolo:", ctx.getText())
    
    def exitDominio(self, ctx):
        print("Domínio:", ctx.getText())
    
    def exitPorta(self, ctx):
        print("Porta:", ctx.getText())
    
    def exitCaminho(self, ctx):
        print("Caminho:", ctx.getText())
    
    def exitQuery(self, ctx):
        print("Query:", ctx.getText())
    
    def exitFragmento(self, ctx):
        print("Fragmento:", ctx.getText())

def main():
    input_url = input("Digite a URL: ")
    input_stream = InputStream(input_url)
    lexer = URLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = URLParser(token_stream)
    tree = parser.url()

    listener = URLPrintListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
