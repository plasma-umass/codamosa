# Automatically generated by Pynguin.
import ansible.module_utils.api as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.rate_limit_argument_spec()

def test_case_2():
    var_0 = module_0.retry_argument_spec()

def test_case_3():
    var_0 = module_0.basic_auth_argument_spec()

def test_case_4():
    var_0 = module_0.rate_limit()

def test_case_5():
    var_0 = module_0.retry()

def test_case_6():
    str_0 = 'TYPE'
    var_0 = module_0.retry(str_0)
    var_1 = module_0.retry()
    list_0 = None
    var_2 = module_0.retry(list_0)
    str_1 = ''
    var_3 = module_0.retry_argument_spec(str_1)
    var_4 = module_0.basic_auth_argument_spec()
    int_0 = 3600
    var_5 = module_0.rate_limit(int_0)
    bool_0 = True
    var_6 = module_0.retry_never(bool_0)

def test_case_7():
    bytes_0 = b'\xdd\x1aC\xed&}'
    tuple_0 = None
    var_0 = module_0.retry_with_delays_and_condition(bytes_0, tuple_0)

def test_case_8():
    var_0 = module_0.rate_limit_argument_spec()
    var_1 = module_0.basic_auth_argument_spec()
    var_2 = module_0.retry()
    var_3 = module_0.basic_auth_argument_spec()
    bytes_0 = b'\xda\x96\xca\xd2G\n?\x02\x92jC\x1f'
    var_4 = module_0.rate_limit(bytes_0)