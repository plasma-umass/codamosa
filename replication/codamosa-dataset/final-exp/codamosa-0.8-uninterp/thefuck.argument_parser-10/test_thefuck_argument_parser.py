# Automatically generated by Pynguin.
import thefuck.argument_parser as module_0

def test_case_0():
    parser_0 = module_0.Parser()

def test_case_1():
    str_0 = 'm'
    parser_0 = module_0.Parser()
    var_0 = parser_0.parse(str_0)

def test_case_2():
    parser_0 = module_0.Parser()
    var_0 = parser_0.print_usage()

def test_case_3():
    parser_0 = module_0.Parser()
    str_0 = ',^G_.R!K>TiPKE.LH9'
    list_0 = [parser_0, str_0, parser_0, str_0]
    var_0 = parser_0.parse(list_0)
    var_1 = parser_0.print_help()