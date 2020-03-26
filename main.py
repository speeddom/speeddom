from lexer import Lexer


text_input = """
((λx.(f x))a)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
for token in tokens:
    print(token)
