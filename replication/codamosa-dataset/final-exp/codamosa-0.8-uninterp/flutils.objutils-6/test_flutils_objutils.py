# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    float_0 = -1126.781889
    bool_0 = module_0.has_attrs(float_0)

def test_case_1():
    set_0 = set()
    bool_0 = module_0.has_any_callables(set_0)

def test_case_2():
    var_0 = dict()
    str_0 = 'keys'
    list_0 = [str_0, str_0, str_0]
    bool_0 = module_0.has_any_callables(var_0, *list_0)

def test_case_3():
    complex_0 = None
    str_0 = 'chmod'
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = module_0.has_attrs(complex_0, *list_0)

def test_case_4():
    float_0 = -1126.781889
    bool_0 = module_0.has_callables(float_0)

def test_case_5():
    float_0 = 462.950597
    str_0 = '8-4^5b\rqeUz\t6MY'
    str_1 = '4/7R1p\t#x>{*9)GW/AkL'
    list_0 = [str_0, str_0, str_1, str_0]
    bool_0 = module_0.has_callables(float_0, *list_0)
    set_0 = {float_0, float_0, float_0, float_0}
    str_2 = 'x1-kUoHE'
    str_3 = None
    list_1 = [str_2, str_2, str_3]
    bool_1 = module_0.has_callables(set_0, *list_1)

def test_case_6():
    str_0 = 'J#Te@]$`eZmT.|b8;=I$'
    bool_0 = module_0.is_list_like(str_0)

def test_case_7():
    list_0 = []
    bool_0 = module_0.is_list_like(list_0)

def test_case_8():
    float_0 = 173.072396
    bool_0 = module_0.is_subclass_of_any(float_0)

def test_case_9():
    int_0 = 1670
    str_0 = '[6,XAM]\rGI@y !PO'
    list_0 = [str_0]
    bool_0 = module_0.has_any_attrs(int_0, *list_0)
    bool_1 = module_0.has_any_attrs(int_0)

def test_case_10():
    var_0 = dict()
    str_0 = 'keys'
    list_0 = [str_0, str_0, str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)