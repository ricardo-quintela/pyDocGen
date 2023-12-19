from productions import lalr_parser

def test_docstring():
    """Tests the "DocString" production
    """

    token_buffer = [
        "QUOTES",
        "TEXT",
        "Arguments",
        "ReturnValue",
        "QUOTES"
    ]

    assert lalr_parser.parse(token_buffer) == "DocString"


def test_arguments():
    """Tests the "Arguments" production
    """
    token_buffer = [
        "ARGS",
        "COLON",
        "Params"
    ]

    assert lalr_parser.parse(token_buffer) == "Arguments"

def test_arguments_2():
    """Tests the "Arguments" production 1.2
    """
    token_buffer = [
        "ARGS",
        "COLON",
        "INDENT",
        "TEXT",
        "Type",
        "TEXT"
    ]

    assert lalr_parser.parse(token_buffer) == "Arguments"


def test_arguments_3():
    """Tests the "Arguments" production 1.3
    """
    token_buffer = [
        "ARGS",
        "COLON",
        "INDENT",
        "TEXT",
        "Type",
        "TEXT",
        "INDENT",
        "TEXT",
        "Type",
        "TEXT"
    ]

    assert lalr_parser.parse(token_buffer) == "Arguments"


def test_arguments_4():
    """Tests the "Arguments" production 1.4
    """
    token_buffer = [
        "ARGS",
        "COLON",
        "INDENT",
        "TEXT",
        "Type",
        "TEXT",
        "Params"
    ]

    assert lalr_parser.parse(token_buffer) == "Arguments"


def test_type1():
    """Tests the "Type" production 1
    """
    token_buffer = [
        "LPAR",
        "TEXT",
        "RPAR",
        "COLON"
    ]

    assert lalr_parser.parse(token_buffer) == "Type"


def test_type2():
    """Tests the "Type" production 2
    """
    token_buffer = [
        "TEXT",
        "COLON"
    ]

    assert lalr_parser.parse(token_buffer) == "Type"



def test_params1():
    """Tests the "Params" production 1
    """
    token_buffer = [
        "INDENT",
        "TEXT",
        "Type",
        "TEXT"
    ]

    assert lalr_parser.parse(token_buffer) == "Params"


def test_params2():
    """Tests the "Params" production 2
    """

    token_buffer = [
        "INDENT",
        "TEXT",
        "Type",
        "TEXT",
        "INDENT",
        "TEXT",
        "Type",
        "TEXT"
    ]

    assert lalr_parser.parse(token_buffer) == "Params"

def test_params2_1():
    """Tests the "Params" production 2.1
    """

    token_buffer = [
        "INDENT",
        "TEXT",
        "Type",
        "TEXT",
        "Params"
    ]

    assert lalr_parser.parse(token_buffer) == "Params"


def test_returnvalue():
    """Tests the "ReturnValue" production
    """

    token_buffer = [
        "RETURNS",
        "COLON",
        "INDENT",
        "Type",
        "TEXT"
    ]

    assert lalr_parser.parse(token_buffer) == "ReturnValue"
