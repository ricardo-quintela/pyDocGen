from tokens import lexer
from productions import lalr_parser

from pprint import pprint


def test_compose_normal():
    with open("test/normal.txt", "r", encoding="utf-8") as test_file:
        text = test_file.read()

    token_buffer = lexer.tokenize(text)

    assert lalr_parser.parse(token_buffer) == "DocString"
