# Automatically generated by Pynguin.
import flutils.namedtupleutils as module_0
import types as module_1

def test_case_0():
    str_0 = 'x>Np#\ro\tU.0L'
    dict_0 = {str_0: str_0, str_0: str_0}
    list_0 = [dict_0]
    var_0 = module_0.to_namedtuple(list_0)

def test_case_1():
    simple_namespace_0 = module_1.SimpleNamespace()
    var_0 = module_0.to_namedtuple(simple_namespace_0)

def test_case_2():
    str_0 = 'b'
    int_0 = 1
    int_1 = {str_0: int_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(int_1)
    var_1 = module_0.to_namedtuple(var_0)

def test_case_3():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)

def test_case_4():
    bytes_0 = b'\xa1),\xc6\x16\xbd3\x95\xf6K>'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, bytes_0]
    var_0 = module_0.to_namedtuple(list_1)

def test_case_5():
    str_0 = 'b'
    int_0 = 1
    int_1 = {str_0: int_0, str_0: int_0}
    int_2 = {str_0: int_0, str_0: int_1}
    var_0 = module_0.to_namedtuple(int_2)
    var_1 = module_0.to_namedtuple(var_0)
    int_3 = (int_0, int_2, int_2)
    var_2 = module_0.to_namedtuple(int_3)

def test_case_6():
    str_0 = 'b'
    int_0 = -26
    int_1 = {str_0: int_0, str_0: str_0, str_0: int_0, int_0: int_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(int_1)
    var_1 = module_0.to_namedtuple(var_0)

def test_case_7():
    simple_namespace_0 = module_1.SimpleNamespace()
    var_0 = module_0.to_namedtuple(simple_namespace_0)
    var_1 = module_0.to_namedtuple(simple_namespace_0)
    list_0 = [var_1]
    str_0 = 'Rudl"" MzHRCb\\'
    var_2 = None
    dict_0 = {str_0: str_0, str_0: var_2, var_1: var_0}
    tuple_0 = (list_0, dict_0)
    var_3 = module_0.to_namedtuple(tuple_0)
    var_4 = module_0.to_namedtuple(simple_namespace_0)
    var_5 = module_0.to_namedtuple(simple_namespace_0)
    var_6 = module_0.to_namedtuple(simple_namespace_0)