# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    try_0 = module_0.Try(bool_0, bool_0)
    str_0 = try_0.__str__()

def test_case_2():
    str_0 = '1U8rRAH[HEZ:P/\n'
    bool_0 = True
    try_0 = module_0.Try(str_0, bool_0)
    bool_1 = try_0.__eq__(bool_0)

def test_case_3():
    bool_0 = False
    str_0 = '\n        Transform Validation to Either.\n\n        :returns: Right monad with previous value when Validation has no errors, in other case Left with errors list\n        :rtype: Right[A] | Left[E]\n        '
    try_0 = module_0.Try(str_0, bool_0)
    var_0 = try_0.bind(bool_0)

def test_case_4():
    tuple_0 = ()
    bool_0 = False
    bool_1 = True
    float_0 = -1496.6456
    try_0 = module_0.Try(float_0, bool_0)
    var_0 = try_0.filter(bool_1)
    bool_2 = True
    str_0 = '=|'
    bool_3 = True
    try_1 = module_0.Try(str_0, bool_3)
    var_1 = try_0.get_or_else(tuple_0)
    var_2 = try_1.get()
    try_2 = module_0.Try(bool_0, bool_2)
    var_3 = try_2.on_fail(tuple_0)

def test_case_5():
    bytes_0 = b'\xae\xac\xc2\xf3ozO\xa2\xe5\x9fV\x03'
    bool_0 = True
    dict_0 = None
    float_0 = -2713.510549
    try_0 = module_0.Try(float_0, bool_0)
    bool_1 = try_0.__eq__(dict_0)
    try_1 = module_0.Try(bytes_0, bool_0)
    var_0 = try_1.get()

def test_case_6():
    set_0 = None
    bool_0 = None
    bytes_0 = b'z\xab{\x83\x8f'
    try_0 = module_0.Try(set_0, bool_0)
    var_0 = try_0.filter(bytes_0)
    dict_0 = {set_0: set_0, set_0: bool_0, set_0: set_0}
    try_1 = module_0.Try(dict_0, bool_0)
    str_0 = try_1.__str__()
    var_1 = try_1.get_or_else(try_1)

def test_case_7():
    float_0 = 476.22239
    set_0 = {float_0}
    str_0 = 'hiT-6J<ijE)/&aGR,&'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = False
    bool_1 = False
    try_0 = module_0.Try(dict_0, bool_1)
    bool_2 = try_0.__eq__(bool_0)
    bool_3 = True
    bool_4 = False
    try_1 = module_0.Try(set_0, bool_4)
    var_0 = try_1.get_or_else(str_0)
    try_2 = module_0.Try(dict_0, bool_3)
    bool_5 = True
    str_1 = '\n        Take mapper function and return value of Left.\n\n        :returns: Stored value\n        :rtype: A\n        '
    tuple_0 = (dict_0, bool_5, str_1)
    var_1 = try_1.map(tuple_0)
    var_2 = try_2.get_or_else(set_0)