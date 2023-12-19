from compyler import Lexer

lexer = Lexer()

# :
lexer.add_token(
    "COLON", r":"
)

# (
lexer.add_token(
    "LPAR", r"\("
)

# )
lexer.add_token(
    "RPAR", r"\)"
)

# description
lexer.add_token(
    "INDENT", r"\t|  {2,}"
)

#"""
lexer.add_token(
    "QUOTES", r"\"\"\""
)

# Args
lexer.add_token(
    "ARGS", r"Args"
)

# Returns
lexer.add_token(
    "RETURNS", r"Returns"
)

# description
lexer.add_token(
    "TEXT", r"[^\n\t:\(\)]+"
)
