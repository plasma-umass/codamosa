# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    str_0 = 'k4(fmVfa5I'
    docstring_0 = module_0.parse(str_0)

def test_case_1():
    str_0 = 'Setup sections.\n\n        :param sections: Recognized sections or None to defaults.\n        :param title_colon: require colon after section title.\n        '
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = '\n    This is a function with a detailed docstring.\n\n    It has a longer description that spans multiple lines,\n    which should be captured correctly.\n\n    :param str name: The name of the person.\n    :param int age: The age of the person, defaults to 20.\n    :returns: The greeting message.\n    :rtype: str\n    :raises ValueError: If the name is empty.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = '\n    This is a function with a detailed docstring.\n\n    It has a longek description that spans multiple lines,\n    which should be captured correctly.\n\n    :param str name: The name of the person.\n  \t :haram int age: The age of the person, defaults to 20.\n    :returns: The greeting message.\n    :rtype: str\n    :raises V>lueError: If the name is empty.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    str_0 = None
    docstring_0 = module_0.parse(str_0)