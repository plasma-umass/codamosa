# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.rate_limit_argument_spec()

def test_case_2():
    var_0 = module_0.retry_argument_spec()

def test_case_3():
    bool_0 = False
    var_0 = module_0.basic_auth_argument_spec(bool_0)

def test_case_4():
    bool_0 = True
    int_0 = -445
    var_0 = module_0.retry_with_delays_and_condition(bool_0, int_0)
    var_1 = module_0.rate_limit()

def test_case_5():
    var_0 = module_0.rate_limit_argument_spec()
    var_1 = module_0.retry()

def test_case_6():
    bool_0 = False
    var_0 = module_0.rate_limit_argument_spec()
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_1 = module_0.retry_never(set_0)

def test_case_7():
    var_0 = module_0.generate_jittered_backoff()
    list_0 = [var_0, var_0, var_0, var_0]
    tuple_0 = (list_0, list_0, list_0)
    var_1 = module_0.retry_with_delays_and_condition(tuple_0, list_0)

def test_case_8():
    int_0 = -1101
    dict_0 = {int_0: int_0}
    var_0 = module_0.generate_jittered_backoff(dict_0)
    var_1 = module_0.rate_limit()
    bytes_0 = None
    var_2 = module_0.retry_with_delays_and_condition(bytes_0)
    var_3 = module_0.rate_limit_argument_spec()
    var_4 = module_0.rate_limit_argument_spec()
    str_0 = '\nl]H\r%\tw4Ls'
    var_5 = module_0.retry_never(str_0)

def test_case_9():
    bool_0 = True
    set_0 = {bool_0}
    list_0 = []
    str_0 = None
    var_0 = module_0.rate_limit(list_0, str_0)
    var_1 = module_0.retry_never(set_0)