from sly import Lexer

class BETPLParser(Lexer):
    tokens = [STRING_TOGGLE, OPEN_PAREN, CLOSE_PAREN, ATOM]
    ignore = r" \t"
    STRING_TOGGLE = r"\""
    OPEN_PAREN = r"[\[{(]"
    CLOSE_PAREN = r"[\]})]"
    ATOM = r"[AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz_-]+"

if __name__ == "__main__":
    data = "(function data data [function data data {function data data \"string\"}])"
    lexer = BETPLParser()
    for token in lexer.tokenize(data):
        print(token)