# Automatically generated by Pynguin.
import pymonet.utils as module_0

def test_case_0():
    try:
        var_0 = module_0.fn()
    except BaseException:
        pass

def test_case_1():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        var_0 = None
        list_0 = [callable_1, var_0, var_0]
        var_1 = module_0.identity(var_0)
        var_2 = module_0.pipe(var_1, *list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1, callable_0]
        var_0 = module_0.pipe(callable_0, *list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        var_0 = module_0.cond(list_0)
        complex_0 = None
        list_1 = [var_0, var_0, complex_0, complex_0]
        var_1 = module_0.pipe(complex_0, *list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        var_0 = module_0.cond(list_0)
        int_0 = -176
        list_1 = [var_0, list_0, var_0, var_0]
        var_1 = module_0.compose(int_0, *list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        str_0 = '\n        Returns True when errors list are empty.\n\n        :returns: True for empty errors list\n        :rtype: Boolean\n        '
        var_0 = module_0.curry(str_0, str_0)
        list_0 = [callable_1, callable_1, callable_1, callable_1, callable_1, callable_0, callable_1, callable_0, callable_0, callable_0, callable_1, callable_0, callable_0, callable_0, callable_1, callable_0, callable_1, callable_0, callable_1, callable_0, callable_1]
        var_1 = module_0.pipe(list_0, *list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        dict_1 = {}
        var_0 = module_0.curry(dict_0, dict_1)
        list_0 = None
        var_1 = module_0.cond(list_0)
        str_0 = '3xqamyg&=sIX[Y{\x0bj'
        list_1 = [var_0]
        tuple_0 = (str_0, list_1, dict_0)
        var_2 = module_0.pipe(tuple_0, *list_1)
    except BaseException:
        pass