# Automatically generated by Pynguin.
import thefuck.corrector as module_0
import pathlib as module_1

def test_case_0():
    try:
        var_0 = module_0.get_rules()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'F_\nZ}7\\E9'
        var_0 = module_0.get_corrected_commands(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        path_0 = module_1.Path()
        var_0 = [path_0]
        var_1 = module_0.get_loaded_rules(var_0)
        var_2 = list(var_1)[var_1]
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 0
        path_0 = module_1.Path()
        str_0 = '__init__.py'
        path_1 = module_1.Path()
        var_0 = path_1 / str_0
        var_1 = var_0 / str_0
        path_2 = module_1.Path()
        var_2 = path_2 / str_0
        var_3 = var_2 / str_0
        var_4 = [var_1, var_3]
        var_5 = module_0.get_loaded_rules(var_4)
        var_6 = list(var_5)[int_0]
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 772.7956
        var_0 = module_0.organize_commands(float_0)
        var_1 = list(var_0)[var_0]
    except BaseException:
        pass