# Automatically generated by Pynguin.
import builtins as module_0
import pymonet.maybe as module_1

def test_case_0():
    try:
        int_0 = 1835
        object_0 = module_0.object()
        bool_0 = False
        maybe_0 = module_1.Maybe(object_0, bool_0)
        var_0 = maybe_0.map(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        bool_0 = False
        list_0 = [var_0, bool_0, bool_0]
        bool_1 = False
        maybe_0 = module_1.Maybe(var_0, bool_1)
        var_1 = maybe_0.bind(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = None
        str_0 = '8K{%-T]D$5{Hd'
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_0 = True
        maybe_0 = module_1.Maybe(dict_0, bool_0)
        var_0 = maybe_0.filter(float_0)
        str_1 = '\n        If Maybe is empty return new empty Maybe, in other case\n        takes mapper function and returns result of mapper.\n\n        :param mapper: function to call with Maybe.value\n        :type mapper: Function(A) -> Maybe[B]\n        :returns: Maybe[B | None]\n        '
        bool_1 = False
        maybe_1 = module_1.Maybe(bool_1, bool_1)
        var_1 = maybe_1.ap(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = None
        bool_0 = True
        maybe_0 = module_1.Maybe(bool_0, bool_0)
        bool_1 = True
        maybe_1 = module_1.Maybe(maybe_0, bool_1)
        var_1 = maybe_1.to_box()
        bool_2 = False
        bool_3 = False
        maybe_2 = module_1.Maybe(bool_2, bool_3)
        var_2 = maybe_2.get_or_else(var_0)
        callable_0 = None
        var_3 = maybe_2.map(callable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xd7\x92Q\x13\xcf\xc3G2\xfa\x8aU(\x9a\xf2,F\xf02'
        str_0 = 'Lazy[T, W]'
        bool_0 = False
        maybe_0 = module_1.Maybe(str_0, bool_0)
        var_0 = maybe_0.to_try()
        set_0 = {bytes_0, bytes_0}
        bool_1 = True
        maybe_1 = module_1.Maybe(set_0, bool_1)
        maybe_2 = module_1.Maybe(maybe_1, bool_1)
        var_1 = maybe_2.filter(bytes_0)
        var_2 = maybe_1.to_lazy()
        var_3 = maybe_1.to_try()
        list_0 = []
        bool_2 = False
        maybe_3 = module_1.Maybe(list_0, bool_2)
        var_4 = maybe_3.to_validation()
        list_1 = None
        object_0 = module_0.object(*list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Sum[value={}]'
        bool_0 = False
        maybe_0 = module_1.Maybe(str_0, bool_0)
        var_0 = maybe_0.to_box()
        float_0 = 2073.0
        var_1 = maybe_0.filter(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1
        bool_0 = False
        maybe_0 = module_1.Maybe(int_0, bool_0)
        maybe_1 = module_1.Maybe(int_0, bool_0)
        bool_1 = None
        maybe_2 = module_1.Maybe(int_0, bool_1)
        maybe_3 = module_1.Maybe(int_0, bool_0)
        var_0 = maybe_2 == maybe_3
        maybe_4 = module_1.Maybe(int_0, bool_0)
        bool_2 = True
        bytes_0 = b'\xaf\x87\xf0n\x1eB\x03\xd9\x05'
        maybe_5 = module_1.Maybe(bytes_0, bool_2)
        var_1 = maybe_3.to_box()
        var_2 = maybe_4.to_lazy()
        float_0 = 3895.547
        var_3 = maybe_1.filter(float_0)
    except BaseException:
        pass