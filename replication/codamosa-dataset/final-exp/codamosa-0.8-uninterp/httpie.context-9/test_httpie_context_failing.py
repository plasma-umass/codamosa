# Automatically generated by Pynguin.
import httpie.context as module_0

def test_case_0():
    try:
        dict_0 = None
        int_0 = -137
        environment_0 = module_0.Environment()
        var_0 = environment_0.__repr__()
        environment_1 = module_0.Environment()
        var_1 = environment_1.log_error(dict_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        str_1 = '1WgTY_n.x[q,:el<'
        int_0 = 2219
        dict_0 = {str_1: str_1, str_0: int_0, str_1: int_0}
        environment_0 = module_0.Environment(str_0, **dict_0)
    except BaseException:
        pass