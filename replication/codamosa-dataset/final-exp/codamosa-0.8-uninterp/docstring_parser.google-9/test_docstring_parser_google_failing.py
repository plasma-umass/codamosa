# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    try:
        section_0 = None
        google_parser_0 = module_0.GoogleParser()
        var_0 = google_parser_0.add_section(section_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "This is a class.\n\nArgs:\n  arg1 (str): bla bla\n  arg2 (str, optional): ble ble. Defaults to 'HELLO'.\n  arg3 (str): bli bli.\n  arg4 (str): bla bla.\n\nExample:\n  >>> instance = Klass(my_arg1, my_arg2)\n  >>> instance.method_a(my_arg3)"
        docstring_0 = module_0.parse(str_0)
        google_parser_0 = module_0.GoogleParser(docstring_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        docstring_0 = module_0.parse(str_0)
        optional_0 = None
        google_parser_0 = None
        google_parser_1 = module_0.GoogleParser(optional_0, google_parser_0)
        list_0 = []
        google_parser_2 = module_0.GoogleParser(list_0)
        google_parser_3 = module_0.GoogleParser(list_0)
        docstring_1 = google_parser_3.parse(str_0)
        section_0 = module_0.Section()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "v/'s@]\\ZOKHX[fi"
        float_0 = -2786.71
        list_0 = [str_0, str_0, float_0]
        str_1 = None
        docstring_0 = module_0.parse(str_1)
        google_parser_0 = module_0.GoogleParser()
        float_1 = None
        google_parser_1 = module_0.GoogleParser(float_1)
        str_2 = 'rn '
        str_3 = 'iW={M'
        docstring_1 = google_parser_1.parse(str_0)
        str_4 = '=5F'
        str_5 = ' '
        dict_0 = {str_3: docstring_0, str_4: docstring_1, str_2: docstring_0, str_5: float_0}
        google_parser_2 = module_0.GoogleParser(dict_0, list_0)
        docstring_2 = google_parser_2.parse(str_3)
        section_0 = module_0.Section(*list_0)
        str_6 = 'y\x0c<zrO.MW-z6)u%'
        docstring_3 = google_parser_1.parse(str_6)
        var_0 = google_parser_1.add_section(section_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "This is a\x0bclass.\n\nArgs:\n  arg1 (str): bla bla\n  arg2 (str, optional): ble ble. Defaults to 'HELLO'\n  arg3 str): bli bli.%  arg4 (str): bla bla.\n\nExample:\nj >>> instance= Klass(my_arg1, my_arg2)\n  >>> instance.method_a(my_arg3)"
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass