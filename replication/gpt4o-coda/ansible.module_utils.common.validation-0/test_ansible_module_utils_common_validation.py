# Automatically generated by Pynguin.
import ansible.module_utils.common.validation as module_0

def test_case_0():
    str_0 = '.e]\rST1b<E'
    var_0 = module_0.count_terms(str_0, str_0)

def test_case_1():
    str_0 = '1 + 1'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    str_0 = '8+!W#pC\nr*6_?%*R|z.F'
    tuple_0 = (str_0,)
    var_0 = module_0.safe_eval(tuple_0)
    int_0 = -1899
    var_1 = module_0.check_missing_parameters(int_0)

def test_case_3():
    float_0 = None
    dict_0 = {float_0: float_0}
    var_0 = module_0.check_mutually_exclusive(dict_0, dict_0)
    var_1 = module_0.check_type_dict(dict_0)

def test_case_4():
    str_0 = 'oWb'
    list_0 = [str_0, str_0, str_0, str_0]
    float_0 = 0.04335664631387344
    set_0 = set()
    tuple_0 = (float_0, list_0, str_0, set_0)
    var_0 = module_0.check_required_if(list_0, tuple_0)
    dict_0 = {str_0: str_0}
    var_1 = module_0.check_required_one_of(dict_0, list_0, set_0)

def test_case_5():
    tuple_0 = ()
    var_0 = module_0.check_required_together(tuple_0, tuple_0)

def test_case_6():
    str_0 = '/rV_["AzlJ'
    var_0 = module_0.check_required_together(str_0, str_0)

def test_case_7():
    bool_0 = None
    var_0 = module_0.check_required_together(bool_0, bool_0)

def test_case_8():
    dict_0 = {}
    var_0 = module_0.check_required_if(dict_0, dict_0)

def test_case_9():
    bytes_0 = b'\xdc\x06\x8d\xb9\xd3'
    var_0 = module_0.check_missing_parameters(bytes_0)

def test_case_10():
    float_0 = 2.40199
    var_0 = module_0.check_type_path(float_0)

def test_case_11():
    str_0 = 'CKFEqB@({qe7 j[UMyyr'
    var_0 = module_0.check_type_str(str_0)

def test_case_12():
    str_0 = '5'
    var_0 = module_0.check_type_list(str_0)

def test_case_13():
    float_0 = 0.0001
    var_0 = module_0.check_type_list(float_0)

def test_case_14():
    str_0 = '&OSTNAME=%s\n'
    var_0 = module_0.check_type_dict(str_0)

def test_case_15():
    float_0 = 3.14
    var_0 = module_0.check_type_float(float_0)

def test_case_16():
    tuple_0 = ()
    var_0 = module_0.check_type_raw(tuple_0)

def test_case_17():
    str_0 = "?xrL'[/p7CnO=,8Xp"
    var_0 = module_0.check_type_jsonarg(str_0)

def test_case_18():
    str_0 = 'oWb'
    list_0 = [str_0, str_0, str_0, str_0]
    int_0 = -1243
    var_0 = module_0.check_type_list(int_0)
    float_0 = 454.621
    set_0 = set()
    tuple_0 = (float_0, list_0, str_0, set_0)
    var_1 = module_0.check_required_if(list_0, tuple_0)

def test_case_19():
    str_0 = 'WY9'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.check_required_if(list_0, list_0)

def test_case_20():
    str_0 = 'WY9'
    list_0 = [str_0, str_0]
    var_0 = module_0.check_required_if(list_0, list_0)
    list_1 = []
    var_1 = module_0.check_type_list(list_1)

def test_case_21():
    str_0 = 'PoWb'
    list_0 = [str_0, str_0, str_0, str_0]
    int_0 = None
    str_1 = 'p\n}8D%>RE.a#8iHL'
    var_0 = module_0.check_required_arguments(int_0, str_1)
    float_0 = -0.7733465881102719
    set_0 = set()
    tuple_0 = (float_0, list_0, str_0, set_0)
    var_1 = module_0.check_required_if(list_0, tuple_0)

def test_case_22():
    bool_0 = False
    var_0 = module_0.check_type_int(bool_0)

def test_case_23():
    str_0 = None
    str_1 = 'oy-|.'
    var_0 = module_0.check_required_by(str_0, str_1)

def test_case_24():
    str_0 = "lR\n`G|IUVf'"
    tuple_0 = None
    dict_0 = {tuple_0: tuple_0, str_0: tuple_0}
    float_0 = None
    dict_1 = {}
    bool_0 = False
    var_0 = module_0.check_required_one_of(float_0, dict_1, bool_0)
    var_1 = module_0.check_required_by(dict_0, dict_0)

def test_case_25():
    bytes_0 = b'\x94\xfa\xf0a\x14w]\x84\xa6\x94\x90m\xba\x9eZeZ\xc93M'
    str_0 = 'c%k\t4#O )M'
    list_0 = [str_0, bytes_0, bytes_0]
    float_0 = 3257.0
    var_0 = module_0.safe_eval(str_0, list_0, float_0)

def test_case_26():
    str_0 = 'lWY9'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.check_required_if(list_0, list_0)

def test_case_27():
    str_0 = "']rr7\\}Mo};=FI_-c^B"
    var_0 = module_0.check_type_dict(str_0)

def test_case_28():
    str_0 = 'key'
    str_1 = {str_0: str_0}
    var_0 = module_0.check_type_dict(str_1)
    str_2 = '{"key": "value"}'
    var_1 = module_0.check_type_dict(str_2)
    str_3 = '[vy=valuL'
    var_2 = module_0.check_type_dict(str_3)
    str_4 = 'key1="value1", key2=\'value2\''
    var_3 = module_0.check_type_dict(str_4)

def test_case_29():
    str_0 = "lR\n`G|IUVf'"
    tuple_0 = None
    dict_0 = {tuple_0: tuple_0, str_0: tuple_0}
    var_0 = module_0.check_required_by(dict_0, dict_0)

def test_case_30():
    dict_0 = {}
    str_0 = '^'
    var_0 = module_0.check_required_by(dict_0, str_0)

def test_case_31():
    str_0 = '5'
    var_0 = module_0.safe_eval(str_0)

def test_case_32():
    str_0 = "os.syEKeLm('iY')"
    var_0 = module_0.safe_eval(str_0)

def test_case_33():
    str_0 = "{'key': 'value'}"
    var_0 = module_0.safe_eval(str_0)
    str_1 = '[1, 2, 3]'
    var_1 = module_0.safe_eval(str_1)
    bool_0 = False
    var_2 = module_0.safe_eval(str_1, bool_0)
    var_3 = module_0.safe_eval(str_0, bool_0)
    var_4 = module_0.safe_eval(str_1, bool_0)
    str_2 = 'import os'
    var_5 = module_0.safe_eval(str_2, bool_0)