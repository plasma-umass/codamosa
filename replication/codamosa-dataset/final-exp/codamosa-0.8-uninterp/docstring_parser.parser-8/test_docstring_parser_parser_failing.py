# Automatically generated by Pynguin.
import docstring_parser.parser as module_0
import docstring_parser.styles as module_1

def test_case_0():
    try:
        str_0 = ':>'
        docstring_0 = module_0.parse(str_0)
        style_0 = module_1.Style.rest
        docstring_1 = module_0.parse(str_0, style_0)
    except BaseException:
        pass