# Automatically generated by Pynguin.
import httpie.context as module_0

def test_case_0():
    pass

def test_case_1():
    environment_0 = module_0.Environment()

def test_case_2():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()

def test_case_3():
    float_0 = None
    environment_0 = module_0.Environment()
    var_0 = environment_0.log_error(float_0)

def test_case_4():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__str__()
    var_1 = environment_0.__repr__()

def test_case_5():
    str_0 = 'stdin'
    int_0 = -789
    dict_0 = {str_0: str_0}
    environment_0 = module_0.Environment(int_0, **dict_0)
    var_0 = environment_0.__repr__()

def test_case_6():
    environment_0 = module_0.Environment()
    var_0 = environment_0.__repr__()