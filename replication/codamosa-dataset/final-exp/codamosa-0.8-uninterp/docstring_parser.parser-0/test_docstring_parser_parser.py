# Automatically generated by Pynguin.
import docstring_parser.parser as module_0
import docstring_parser.styles as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'examples'
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = '9'
    style_0 = module_1.Style.rest
    str_1 = 'Yields'
    docstring_0 = module_0.parse(str_1)
    docstring_1 = module_0.parse(str_0, style_0)

def test_case_3():
    style_0 = module_1.Style.google
    str_0 = ':E<TO@'
    docstring_0 = module_0.parse(str_0, style_0)
    docstring_1 = module_0.parse(str_0)