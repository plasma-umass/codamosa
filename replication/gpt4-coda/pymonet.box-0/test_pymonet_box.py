# Automatically generated by Pynguin.
import pymonet.box as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    box_0 = module_0.Box(var_0)

def test_case_2():
    object_0 = module_1.object()
    box_0 = module_0.Box(object_0)
    bool_0 = box_0.__eq__(object_0)

def test_case_3():
    dict_0 = None
    box_0 = module_0.Box(dict_0)
    str_0 = "%Vq*OLe'O-i{w,\tR=,"
    bytes_0 = b''
    box_1 = module_0.Box(bytes_0)
    str_1 = box_1.__str__()
    dict_1 = {str_0: str_0}
    str_2 = box_1.__str__()
    box_2 = module_0.Box(dict_1)
    var_0 = box_2.to_either()

def test_case_4():
    float_0 = -2594.8
    set_0 = {float_0, float_0}
    box_0 = module_0.Box(set_0)
    box_1 = module_0.Box(box_0)
    var_0 = box_1.to_try()
    box_2 = module_0.Box(box_1)
    box_3 = module_0.Box(box_2)
    var_1 = box_3.to_maybe()
    object_0 = None
    bool_0 = box_3.__eq__(object_0)
    var_2 = box_0.to_maybe()

def test_case_5():
    str_0 = "\r<)[Rfk'bAQcVY3G/X7"
    dict_0 = {str_0: str_0}
    box_0 = module_0.Box(dict_0)
    var_0 = box_0.to_lazy()

def test_case_6():
    str_0 = 'I<?:%N+r/z'
    box_0 = module_0.Box(str_0)
    bool_0 = True
    box_1 = module_0.Box(bool_0)
    var_0 = box_1.to_validation()