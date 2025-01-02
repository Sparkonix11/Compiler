from lex import *

def main():
    source = "IF+-123 foo*THEN/"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(f"Token: {token.kind} (Text: {token.text})")
        token = lexer.getToken()


main()
