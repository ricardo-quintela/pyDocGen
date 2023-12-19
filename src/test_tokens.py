from tokens import lexer

def test_args():
    """Tests the arguments part of the docstring
    """
    string = "Args:\n\tvar (type): description with multiple words"

    assert lexer.tokenize(string) == [
        "ARGS",
        "COLON",
        "INDENT",
        "TEXT",
        "LPAR",
        "TEXT",
        "RPAR",
        "COLON",
        "TEXT"
    ]
