# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    try:
        tuple_0 = ()
        bool_0 = True
        str_0 = "'3tia\x0cv4N'o/l~k"
        try_0 = module_0.Try(tuple_0, bool_0)
        var_0 = try_0.get()
        set_0 = {tuple_0, str_0, str_0}
        bytes_0 = b'\x9at_\x89\\1\xd2\xb6w\xc6>\xcd\xc3\xfd\x18\xdc\x83'
        bool_1 = None
        try_1 = module_0.Try(bytes_0, bool_1)
        bool_2 = False
        try_2 = module_0.Try(set_0, bool_2)
        bool_3 = try_2.__eq__(try_2)
        str_1 = 'VR2_n/p\rR'
        bool_4 = False
        var_1 = try_2.filter(bool_4)
        var_2 = try_0.filter(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = False
        list_0 = [int_0, int_0, int_0]
        bytes_0 = b'z\x07\t\xa3\x86B\xa2\x9f\xa6\x1c\xf0\xc1\xf6\x8fy'
        bytes_1 = b'OYi\xe6\ns\xb5$\x9f !\xd0\xbf\xfa\x9a\x81\xc5\xf2 '
        bytes_2 = b'jtplQ[\xa4\x10c\xb5\xbc\x07_\xecP\xa0"'
        bool_0 = False
        try_0 = module_0.Try(bytes_2, bool_0)
        var_0 = try_0.map(bytes_1)
        bool_1 = True
        try_1 = module_0.Try(bytes_0, bool_1)
        var_1 = try_1.filter(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'lR1'
        set_0 = {str_0, str_0, str_0}
        bytes_0 = b'\xcfu*s\xcfL/&\xf0.v\xd4\xa8\xfa$'
        bool_0 = False
        try_0 = module_0.Try(bytes_0, bool_0)
        var_0 = try_0.bind(set_0)
        tuple_0 = ()
        int_0 = 4096
        bool_1 = True
        tuple_1 = (int_0, bool_1)
        try_1 = module_0.Try(tuple_1, bool_1)
        var_1 = try_1.map(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        str_0 = '\n        Transform Validation to Either.\n\n        :returns: Right monad with previous value when Validation has no errors, in other case Left with errors list\n        :rtype: Right[A] | Left[E]\n        '
        bool_1 = True
        try_0 = module_0.Try(str_0, bool_1)
        var_0 = try_0.bind(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = None
        bytes_0 = b''
        float_0 = 2899.5
        tuple_1 = (bytes_0, float_0, float_0)
        dict_0 = {tuple_1: bytes_0, tuple_1: bytes_0, float_0: float_0}
        list_0 = [dict_0]
        tuple_2 = (dict_0, list_0)
        bool_0 = False
        try_0 = module_0.Try(tuple_2, bool_0)
        var_0 = try_0.on_success(tuple_0)
        int_0 = True
        bool_1 = True
        try_1 = module_0.Try(int_0, bool_1)
        bool_2 = True
        var_1 = try_1.bind(bool_2)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 758
        bool_0 = False
        set_0 = {int_0, bool_0, int_0}
        bool_1 = True
        try_0 = module_0.Try(bool_0, bool_1)
        var_0 = try_0.on_success(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        float_0 = 3275.364978
        bytes_0 = b'\x0cl%'
        bytes_1 = b''
        bool_0 = False
        try_0 = module_0.Try(bytes_1, bool_0)
        var_0 = try_0.bind(bytes_0)
        dict_1 = {float_0: float_0, float_0: float_0}
        bool_1 = False
        try_1 = module_0.Try(dict_1, bool_1)
        var_1 = try_1.on_fail(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '('
        bool_0 = False
        try_0 = module_0.Try(str_0, bool_0)
        var_0 = try_0.filter(try_0)
        bool_1 = True
        try_1 = module_0.Try(try_0, bool_1)
        var_1 = try_1.filter(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        list_0 = []
        bool_1 = None
        try_0 = module_0.Try(bool_1, bool_1)
        float_0 = -817.426
        bool_2 = True
        try_1 = module_0.Try(float_0, bool_2)
        bool_3 = try_1.__eq__(try_0)
        try_2 = module_0.Try(list_0, bool_0)
        bytes_0 = b''
        var_0 = try_2.map(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        str_0 = 'Error!'
        var_0 = Exception(str_0)
        bool_1 = True
        try_0 = module_0.Try(bool_0, bool_1)
        var_1 = lambda x: x
        var_2 = try_0.filter(var_1)
        try_1 = module_0.Try(bool_0, bool_1)
        try_2 = module_0.Try(bool_0, bool_1)
        var_3 = try_2.filter(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        str_0 = 'Error!'
        var_0 = Exception(str_0)
        bool_1 = True
        try_0 = module_0.Try(bool_0, bool_1)
        var_1 = lambda x: x
        var_2 = try_0.filter(var_1)
        try_1 = module_0.Try(bool_0, bool_1)
        bool_2 = False
        var_3 = lambda x: x == bool_2
        var_4 = try_0.filter(var_3)
    except BaseException:
        pass