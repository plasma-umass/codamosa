# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'x,lD'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    tuple_0 = None
    list_0 = [tuple_0, tuple_0, tuple_0]
    var_0 = module_0.safe_eval(list_0)

def test_case_3():
    str_0 = 'found interpreters: {0}'
    var_0 = module_0.safe_eval(str_0)

def test_case_4():
    str_0 = "{'sub': [{'subsub': {'value': 'test'}}, 'foo', 'bar']}"
    var_0 = module_0.safe_eval(str_0)

def test_case_5():
    str_0 = 'h&K%-e'
    float_0 = 981.9236963120109
    var_0 = module_0.safe_eval(str_0, float_0, float_0)

def test_case_6():
    bytes_0 = b'\xc3\xfc\xa4\xd5M\x01\x8c\x1d\x88\x82\xaf\xfb+\xd1\x11\xe3\xf2\x02\x82'
    list_0 = [bytes_0]
    str_0 = '1u7sJKFuR9zxWa'
    tuple_0 = (str_0,)
    var_0 = module_0.safe_eval(list_0, list_0, tuple_0)
    int_0 = -2376
    var_1 = module_0.safe_eval(bytes_0, int_0)

def test_case_7():
    str_0 = 'h&K%-e'
    var_0 = module_0.safe_eval(str_0, str_0)

def test_case_8():
    float_0 = 0.0
    bytes_0 = b'x\xc2\xe7\x97\xc1'
    var_0 = module_0.safe_eval(float_0, bytes_0)
    str_0 = '1'
    var_1 = module_0.safe_eval(str_0)
    str_1 = 'True'
    str_2 = 'True and False'
    set_0 = {str_2, var_1}
    var_2 = module_0.safe_eval(set_0)
    bytes_1 = b''
    float_1 = 0.0001
    list_0 = [str_2, str_1, float_1]
    int_0 = -2643
    var_3 = module_0.safe_eval(bytes_1, list_0, int_0)
    var_4 = module_0.safe_eval(set_0)
    tuple_0 = None
    str_3 = 'xo>Rlk^lLm\rZ'
    var_5 = module_0.safe_eval(str_1, tuple_0, str_3)
    str_4 = 'b'
    var_6 = module_0.safe_eval(str_4)
    str_5 = '8=m7s'
    bytes_2 = b'V\xba\x86\xa0\x127'
    var_7 = module_0.safe_eval(str_5, bytes_2)