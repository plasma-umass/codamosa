# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    pass

def test_case_1():
    google_parser_0 = module_0.GoogleParser()

def test_case_2():
    str_0 = '!m$Pf/'
    list_0 = []
    dict_0 = {}
    google_parser_0 = module_0.GoogleParser(list_0, dict_0)
    docstring_0 = google_parser_0.parse(str_0)

def test_case_3():
    str_0 = '    Args:\n        name: str. The name to use.\n    Example:\n        Use like this.\n    '
    docstring_0 = module_0.parse(str_0)
    list_0 = [docstring_0, docstring_0, docstring_0]
    section_0 = module_0.Section(*list_0)
    section_type_0 = module_0.SectionType.SINGULAR
    google_parser_0 = module_0.GoogleParser(section_type_0)
    var_0 = google_parser_0.add_section(section_0)

def test_case_4():
    str_0 = '    Args:\n        name: str. The name to use.\n    Example:\n        Use like this.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = 'p$*'
    google_parser_0 = module_0.GoogleParser(str_0)
    docstring_0 = google_parser_0.parse(str_0)

def test_case_6():
    str_0 = '\n    A typical Google-style docstring.\n\n    Args:\n      param1: Description of `param1`.\n     param2: Description of `param2` [default: None].\n    Raises:\n      KeyError: if unknonw key i~ encountered.\n    Returns:\n      Description of return value.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_7():
    str_0 = '    Arg[:\n        name: str.The name to use.\n    Example:\n        Use like this.\n   '
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '    Args:\n        name: str. The name to use.\n    Example:\n        Use like this.\n    '
    google_parser_0 = module_0.GoogleParser()
    str_1 = None
    docstring_0 = google_parser_0.parse(str_1)
    docstring_1 = module_0.parse(str_0)

def test_case_9():
    str_0 = '\n    This is a module capable of classifying \n    several models of data, such as text,\n    images, audio, etc.\n\n    Args:\n        arg1 (str): a str variable\n        arg2 (str): a str variable\n        arg3 (int): a int variable\n   \n    Returns:\n        dict: a dict variable\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_10():
    str_0 = 'Parse the ReST-style docstring into its components.\n\n    :returns: parsed docstring\n    '
    google_parser_0 = module_0.GoogleParser()
    docstring_0 = google_parser_0.parse(str_0)
    str_1 = 'Summarize your function here.\n    Args:\n      param1: The first parameter.\n      param2: The second parameter.\n    Returns:\n      The return value. True for success, False otherwise.'
    google_parser_1 = module_0.GoogleParser()
    docstring_1 = google_parser_1.parse(str_1)

def test_case_11():
    str_0 = '    Args:\n        name:\x0bstr. The name to use.\n    Example:\n        Use like this.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_12():
    google_parser_0 = module_0.GoogleParser()
    str_0 = "\n        Args:\n            param1 (int): The first parameter.\n            param2 (str): The second parameter.\n            param3 (Optional[int]): The third parameter.\n                Defaults to 0. \n            param4 (str, optional): The fourth parameter.\n                Defaults to 'a'.\n            param5 (str, Optional[int]): The fifth parameter.\n                Defaults to 'word'.\n\n        Raises:\n            ValueError: If `bar` is less than `foo`.\n            ValueError: If `baz` is less than 10.\n"
    docstring_0 = google_parser_0.parse(str_0)

def test_case_13():
    str_0 = '\n    Args:\n        a: first param.\n        b (str): second param.\n        c (str, optional): third param. Defaults to None.\n'
    google_parser_0 = module_0.GoogleParser()
    docstring_0 = google_parser_0.parse(str_0)
    var_0 = docstring_0.meta
    var_1 = print(docstring_0)