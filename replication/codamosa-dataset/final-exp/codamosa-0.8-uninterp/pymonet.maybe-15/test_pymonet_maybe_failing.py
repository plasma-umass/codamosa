# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    try:
        int_0 = False
        str_0 = None
        list_0 = [str_0, int_0]
        bool_0 = False
        maybe_0 = module_0.Maybe(list_0, bool_0)
        var_0 = maybe_0.to_validation()
        maybe_1 = module_0.Maybe(list_0, bool_0)
        var_1 = maybe_1.to_box()
        object_0 = module_1.object()
        bool_1 = maybe_1.__eq__(object_0)
        var_2 = maybe_1.map(object_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n        Returns failed Validation with None as value and errors list.\n\n        :params errors: list of errors to store\n        :type value: List[E]\n        :returns: Failed Validation\n        :rtype: Validation[None, List[E]]\n        '
        bool_0 = True
        dict_0 = {bool_0: str_0, str_0: str_0}
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        bool_1 = True
        maybe_1 = module_0.Maybe(maybe_0, bool_1)
        var_0 = maybe_1.to_box()
        var_1 = maybe_1.to_validation()
        var_2 = maybe_1.to_box()
        str_1 = ''
        dict_1 = {str_1: str_1}
        callable_0 = None
        var_3 = maybe_1.filter(callable_0)
        bool_2 = False
        maybe_2 = module_0.Maybe(dict_1, bool_2)
        var_4 = maybe_2.bind(maybe_2)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'#G'
        float_0 = 1812.1546
        bool_0 = False
        maybe_0 = module_0.Maybe(float_0, bool_0)
        var_0 = maybe_0.ap(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xa2\xae\x9b\x7f-\xad\xcbk!\xb3\x15*D\xda\xfb\x89\xe3\x9bi'
        object_0 = module_1.object()
        bool_0 = True
        maybe_0 = module_0.Maybe(object_0, bool_0)
        var_0 = maybe_0.to_either()
        float_0 = -1805.7
        bool_1 = False
        maybe_1 = module_0.Maybe(float_0, bool_1)
        var_1 = None
        maybe_2 = module_0.Maybe(var_1, bool_1)
        var_2 = maybe_1.to_either()
        var_3 = maybe_1.map(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = None
        list_0 = [set_0]
        bool_0 = False
        maybe_0 = module_0.Maybe(list_0, bool_0)
        var_0 = maybe_0.to_try()
        list_1 = [set_0, set_0, set_0]
        bool_1 = True
        maybe_1 = module_0.Maybe(list_1, bool_1)
        var_1 = maybe_1.to_either()
        object_0 = module_1.object()
        float_0 = 2577.57
        bool_2 = False
        maybe_2 = module_0.Maybe(float_0, bool_2)
        var_2 = maybe_2.to_either()
        bool_3 = maybe_2.__eq__(object_0)
        bytes_0 = b''
        var_3 = maybe_2.to_lazy()
        var_4 = maybe_2.bind(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = set()
        bool_0 = False
        str_0 = 'Q=O|O+!~5gZ.mr('
        bool_1 = True
        maybe_0 = module_0.Maybe(str_0, bool_1)
        var_0 = maybe_0.filter(maybe_0)
        maybe_1 = module_0.Maybe(set_0, bool_0)
        var_1 = maybe_1.filter(str_0)
    except BaseException:
        pass