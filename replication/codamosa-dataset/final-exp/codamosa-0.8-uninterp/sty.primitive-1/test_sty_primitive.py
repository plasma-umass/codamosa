# Automatically generated by Pynguin.
import sty.primitive as module_0

def test_case_0():
    register_0 = module_0.Register()

def test_case_1():
    style_0 = module_0.Style()

def test_case_2():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    str_0 = '\nThese are the default registers that sty provides out of the box.\n'
    register_0.mute()
    style_0 = module_0.Style()
    var_0 = register_0.__setattr__(str_0, style_0)
    str_1 = register_1.__call__()

def test_case_3():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    var_0 = register_1.as_namedtuple()
    str_0 = '\nThese are the default registers that sty provides out of the box.\n'
    style_0 = module_0.Style()
    var_1 = register_0.__setattr__(str_0, style_0)
    register_2 = module_0.Register()
    str_1 = register_2.__call__()

def test_case_4():
    register_0 = module_0.Register()
    register_1 = module_0.Register()
    register_0.mute()
    str_0 = register_1.__call__()

def test_case_5():
    int_0 = None
    list_0 = [int_0, int_0, int_0]
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    str_0 = register_1.__call__(*list_0)
    register_2 = module_0.Register()
    register_3 = module_0.Register()

def test_case_6():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    register_1.mute()
    style_0 = module_0.Style()
    type_0 = None
    callable_0 = None
    register_1.set_renderfunc(type_0, callable_0)

def test_case_7():
    register_0 = module_0.Register()
    register_0.mute()
    register_1 = module_0.Register()

def test_case_8():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    dict_0 = register_1.as_dict()

def test_case_9():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    register_2 = register_1.copy()
    var_0 = register_2.as_namedtuple()

def test_case_10():
    register_0 = module_0.Register()
    register_1 = register_0.copy()