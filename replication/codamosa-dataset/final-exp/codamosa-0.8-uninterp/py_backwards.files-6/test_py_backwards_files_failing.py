# Automatically generated by Pynguin.
import py_backwards.files as module_0

def test_case_0():
    try:
        str_0 = 'input/foo.py'
        iterable_0 = module_0.get_input_output_paths(str_0, str_0, str_0)
        var_0 = list(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'input'
        str_1 = 'output/foo.py'
        str_2 = 'input/foo.py'
        iterable_0 = module_0.get_input_output_paths(str_2, str_1, str_2)
        var_0 = list(str_2)
        iterable_1 = module_0.get_input_output_paths(str_0, str_1, str_0)
        var_1 = list(iterable_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = './'
        var_0 = None
        str_1 = 'a/b.py'
        iterable_0 = module_0.get_input_output_paths(str_0, str_0, var_0)
        var_1 = list(iterable_0)
        iterable_1 = module_0.get_input_output_paths(str_0, str_1, var_0)
        var_2 = list(iterable_1)
    except BaseException:
        pass