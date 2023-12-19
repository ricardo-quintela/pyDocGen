from compyler import LALRParser

lalr_parser = LALRParser()


lalr_parser.add_production(
    "DocString",
    {
        ("QUOTES", "TEXT", "Arguments", "ReturnValue", "QUOTES"): (1,2,3)
    }
)

lalr_parser.add_production(
    "Arguments",
    {
        ("ARGS", "COLON", "Params"): (1,2)
    }
)

lalr_parser.add_production(
    "Type",
    {
        ("LPAR", "TEXT", "RPAR", "COLON"): (1,),
        ("TEXT", "COLON"): (0,),
    }
)

lalr_parser.add_production(
    "Params",
    {
        ("INDENT", "TEXT", "Type", "TEXT", "Params"): (1,2,3,4),
        ("INDENT", "TEXT", "Type", "TEXT"): (1,2,3)
    }
)

lalr_parser.add_production(
    "ReturnValue",
    {
        ("RETURNS", "COLON", "INDENT", "Type", "TEXT"): (2,3),
    }
)
