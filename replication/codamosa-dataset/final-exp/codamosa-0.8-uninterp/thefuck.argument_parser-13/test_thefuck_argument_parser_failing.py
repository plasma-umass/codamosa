# Automatically generated by Pynguin.
import thefuck.argument_parser as module_0

def test_case_0():
    try:
        str_0 = 'dR@-2Yo'
        parser_0 = module_0.Parser()
        var_0 = parser_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        parser_0 = module_0.Parser()
        var_0 = parser_0.print_help()
        str_0 = '--enable-experimental-instant-mode'
        var_1 = parser_0.print_help()
        var_2 = parser_0.parse(str_0)
        var_3 = parser_0.parse(parser_0)
    except BaseException:
        pass