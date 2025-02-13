# Automatically generated by Pynguin.
import docstring_parser.common as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    str_0 = 'Base parser for numpydoc sections with key-value syntax.\n\n    E.g. sections that look like this:\n        key\n            value\n        key2 : type\n            values can also span...\n            ... multiple lines\n    '
    docstring_raises_0 = module_0.DocstringRaises(list_0, str_0, str_0)

def test_case_2():
    str_0 = 'b"m;GtD~?O5@#hp!R[q'
    str_1 = 'l'
    list_0 = [str_0, str_1, str_0]
    int_0 = -325
    docstring_param_0 = module_0.DocstringParam(list_0, str_1, str_1, str_1, int_0, str_1)

def test_case_3():
    list_0 = []
    str_0 = '8Ht`GHVB \\|R4J"n\n'
    str_1 = '\x0cu;I@iowqt. 8oC<D{qW'
    bytes_0 = b'\x05eq\x83'
    docstring_param_0 = module_0.DocstringParam(list_0, str_0, str_1, str_0, bytes_0, str_0)
    str_2 = 'X_z>1c\t[K'
    bool_0 = True
    docstring_0 = module_0.Docstring()
    str_3 = 'Parser for numpydoc raises sections.\n\n    E.g. any section that looks like this:\n        return_name : type\n            A description of this returned value\n        another_type\n            Return names are optional, types are required\n    '
    docstring_param_1 = module_0.DocstringParam(list_0, str_2, str_3, str_2, bool_0, str_1)
    docstring_returns_0 = module_0.DocstringReturns(list_0, str_2, str_2, bool_0, str_2)

def test_case_4():
    list_0 = []
    parse_error_0 = module_0.ParseError()
    str_0 = ')'
    docstring_deprecated_0 = module_0.DocstringDeprecated(list_0, parse_error_0, str_0)
    str_1 = 'i=z(u'
    str_2 = 'A3`~=;B}\\'
    str_3 = '\\'
    list_1 = [str_3, str_3, str_3]
    docstring_raises_0 = module_0.DocstringRaises(list_1, str_3, str_1)
    docstring_raises_1 = module_0.DocstringRaises(list_1, str_1, str_3)
    docstring_raises_2 = module_0.DocstringRaises(list_1, str_3, str_3)
    list_2 = [str_1, str_2, str_1]
    docstring_meta_0 = module_0.DocstringMeta(list_2, str_1)

def test_case_5():
    docstring_0 = module_0.Docstring()