from HtmlParser import HtmlParser
from HtmlVisitor import HtmlVisitor

class HtmlGeneratorVisitor(HtmlVisitor):
    def __init__(self):
        self.html = ""

    def visitHtml(self, ctx:HtmlParser.HtmlContext):
        self.html += "<html>\n<body>\n"
        self.visitChildren(ctx)
        self.html += "</body>\n</html>"
        return self.html

    def visitMenu(self, ctx:HtmlParser.MenuContext):
        menu_id = ctx.ID().getText()
        menu_label = ctx.LABEL().getText().strip('"')
        self.html += f'<label for="{menu_id}">{menu_label}</label>\n'
        self.html += f'<select name="{menu_id}" id="{menu_id}">\n'
        self.visitChildren(ctx)
        self.html += '</select>\n'
        return None

    def visitMenuOption(self, ctx:HtmlParser.MenuOptionContext):
        option_id = ctx.ID().getText()
        option_label = ctx.LABEL().getText().strip('"')
        self.html += f'  <option value="{option_id}">{option_label}</option>\n'
        return None

    def visitButton(self, ctx:HtmlParser.ButtonContext):
        button_label = ctx.LABEL().getText().strip('"')
        alert_message = ctx.STRING().getText().strip('\'')
        self.html += f'<button type="button" onclick="alert(\'{alert_message}\')">{button_label}</button>\n'
        return None
