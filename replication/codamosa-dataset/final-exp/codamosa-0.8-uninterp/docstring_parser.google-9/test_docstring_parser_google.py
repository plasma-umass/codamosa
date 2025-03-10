# Automatically generated by Pynguin.
import docstring_parser.google as module_0
import docstring_parser.common as module_1

def test_case_0():
    pass

def test_case_1():
    google_parser_0 = module_0.GoogleParser()

def test_case_2():
    str_0 = 'fA[nQ7Nt2g\x0c%{pi'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    optional_0 = None
    str_0 = ''
    docstring_0 = module_0.parse(str_0)
    google_parser_0 = module_0.GoogleParser(optional_0, docstring_0)

def test_case_4():
    str_0 = 'Short description.\n\nLong description.\n\nArgs:\n    name (tr): The name.\n\nRaises:\n    ValueError: An exception occurs.\n\nRturns:\n    str: A string.\n    '
    str_1 = "This is a class.\n\nArgs:\n  arg1 (str): bla bla\n  arg2 (str, optional): ble ble. Defaults to 'HELLO'.\n  arg3 (str): bli bli.\n  arg4 (str): bla bla.\n\nExample:\n  >>> instance = Klass(my_arg1, my_arg2)\n  >>> instance.method_a(my_arg3)"
    docstring_0 = module_0.parse(str_0)
    str_2 = None
    docstring_1 = module_0.parse(str_2)
    str_3 = '`F.2#Q>KUKpiz|ZQ'
    google_parser_0 = module_0.GoogleParser()
    docstring_2 = google_parser_0.parse(str_1)
    docstring_3 = module_0.parse(str_3)
    str_4 = ' '
    docstring_4 = google_parser_0.parse(str_4)

def test_case_5():
    str_0 = "This is a class.\n\nArgs:\n  arg1 (str): bla bla\n  arg2 (str, optional): ble ble. Defaults to 'HELLO'.\n  arg3 (str): bli bli.\n  arg4 (str): bla bla.\n\nExample:\n  >>> instance = Klass(my_arg1, my_arg2)\n  >>> instance.method_a(my_arg3)"
    docstring_0 = module_0.parse(str_0)

def test_case_6():
    str_0 = 'Short description.\n\nLong description.\n\nArgs:\n    name (str): The name.\n\nRaises:\n    ValueError: An exception occurs.\n\nReturns:\n    str: A string.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_7():
    str_0 = "This is a class.p\nArgs:\n Xarg1 (str): bla bla\n  arg2 (str, optional):Eble ble. Defaults to 'HELLO'.\n  arg3 (str)3 bli bli.\n  arg4 (str): bla bla.\n\nExample:\n  >>> instance = Klass(hy_arg1, my_arg2)\n  >>> instance.method_a(my_arg3)"
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = "\n    Short summary.\n\n    Long description.\n\n    Args:\n        arg1: description of 'arg1'\n        arg2 (int): description of 'arg2'\n        arg3 (:class:`int`, optional): description of 'arg3'\n        arg4 (int, optional, default=42): description of 'arg4'. Defaults to 3.\n        arg5 (int, optional, default=42): description of 'arg5'. Defaults to 'foo'\n\n    Returns:\n        description of return value\n    "
    docstring_0 = module_0.parse(str_0)
    var_0 = docstring_0.meta
    var_1 = len(var_0)

def test_case_9():
    str_0 = "This is a class.\n\nArgs:\n  arg1 (str): bla bla\n  arg2 (str, optional): ble ble. Defaults to 'HELLO'\n  arg3 str): bli bli.%  arg4 (str): bla bla.\n\nExample:\n  >>> instance= Klass(my_arg1, my_arg2)\n  >>> instance.method_a(my_arg3)"
    docstring_0 = module_0.parse(str_0)

def test_case_10():
    str_0 = 'Short description.\n\nLong description.\n\nArgs:\n    name (str) The name.\n\nRises:\n    ValueEr.r: An exception occurs.\n\nReturns:\n    str: Astring.\n    '
    docstring_0 = module_1.Docstring()
    docstring_1 = module_0.parse(str_0)
    str_1 = '%'
    docstring_2 = module_0.parse(str_1)
    str_2 = None
    docstring_3 = module_0.parse(str_2)