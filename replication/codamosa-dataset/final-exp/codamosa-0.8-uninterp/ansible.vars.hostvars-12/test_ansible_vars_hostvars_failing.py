# Automatically generated by Pynguin.
import ansible.vars.hostvars as module_0

def test_case_0():
    try:
        bytes_0 = b'R\xe6\x91\x8f\x19\xb8#\xbb\x18C\\\x87F\x194N '
        set_0 = set()
        bool_0 = False
        host_vars_0 = module_0.HostVars(bytes_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        float_0 = -863.407453
        list_0 = [float_0, float_0, float_0]
        set_0 = set()
        int_0 = -212
        str_0 = 'B\nijU",WH+jBl\x0c'
        float_1 = 512.0
        str_1 = '\t*\x0bmQ!mW]Ua'
        bytes_0 = b'\xa2\xc8\x04i\rA\x98'
        tuple_0 = (str_0, float_1, str_1, bytes_0)
        tuple_1 = (int_0, tuple_0, int_0)
        host_vars_vars_0 = module_0.HostVarsVars(set_0, tuple_1)
        host_vars_vars_1 = module_0.HostVarsVars(list_0, host_vars_vars_0)
        host_vars_vars_2 = module_0.HostVarsVars(float_0, host_vars_vars_1)
        var_0 = host_vars_vars_2.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1027
        float_0 = 865.0
        dict_0 = {float_0: float_0, float_0: int_0}
        tuple_0 = (dict_0,)
        set_0 = set()
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, set_0)
        var_0 = host_vars_vars_0.__repr__()
        bool_0 = True
        set_1 = {int_0, int_0, bool_0, bool_0}
        bytes_0 = None
        host_vars_vars_1 = module_0.HostVarsVars(bytes_0, bytes_0)
        var_1 = host_vars_vars_1.__getitem__(set_1)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -863.407453
        set_0 = set()
        int_0 = -204
        str_0 = 'B\nijU",WH+jBl\x0c'
        dict_0 = {int_0: float_0, str_0: int_0, str_0: str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, dict_0)
        var_0 = host_vars_vars_0.__contains__(int_0)
        host_vars_vars_1 = module_0.HostVarsVars(set_0, dict_0)
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_1, dict_0)
        var_1 = host_vars_0.__setstate__(dict_0)
        bytes_0 = b'\xa2\xc8\x04i\rA\x98'
        var_2 = host_vars_0.set_inventory(int_0)
        str_1 = 'HsW'
        bytes_1 = b'\xef\xceI\xe0\xfe/\x9d\n\xe0\x96\xa29\xa8\xda'
        host_vars_vars_2 = module_0.HostVarsVars(str_1, bytes_1)
        host_vars_1 = module_0.HostVars(host_vars_vars_2, host_vars_vars_2, float_0)
        var_3 = host_vars_1.set_host_facts(bytes_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'F g\\R=Q'
        bytes_0 = b'\xcc\x9cAfI\xaf9\x14\xad\x93\x05\xd8\xc2'
        host_vars_vars_0 = module_0.HostVarsVars(str_0, bytes_0)
        var_0 = host_vars_vars_0.__len__()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 737.53606
        int_0 = 63
        host_vars_vars_0 = module_0.HostVarsVars(float_0, int_0)
        var_0 = host_vars_vars_0.__repr__()
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        str_0 = '--flush-cache'
        int_0 = 1569
        set_0 = None
        dict_0 = {bool_0: int_0, set_0: str_0, bool_0: int_0, str_0: int_0}
        str_1 = None
        bytes_0 = b'9\xd3\x8a\x85Y\xa7\xd3\xfb\xf3\x97'
        str_2 = '?kqp|J@`@hLOG;+BI\x0cn\\'
        complex_0 = None
        tuple_0 = None
        tuple_1 = (bytes_0, str_2, complex_0, tuple_0)
        float_0 = -1818.95623
        tuple_2 = (str_1, tuple_1, float_0)
        set_1 = None
        list_0 = [tuple_1, set_1]
        int_1 = 82
        host_vars_vars_0 = module_0.HostVarsVars(list_0, int_1)
        host_vars_vars_1 = module_0.HostVarsVars(tuple_2, host_vars_vars_0)
        float_1 = 605.3
        host_vars_0 = module_0.HostVars(bool_0, host_vars_vars_1, float_1)
        var_0 = host_vars_0.set_nonpersistent_facts(str_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        str_0 = '`Uh\x0c0I;g\r='
        str_1 = 'Cj}J3I)D'
        bytes_0 = b'\x96\xd0)\xf3\x16!\x9c\xce'
        host_vars_vars_0 = module_0.HostVarsVars(bytes_0, tuple_0)
        host_vars_0 = module_0.HostVars(tuple_0, host_vars_vars_0, str_0)
        var_0 = host_vars_0.__getitem__(str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'foo'
        str_1 = 'bar'
        str_2 = 'baz'
        str_3 = {str_0: str_1, str_1: str_2}
        var_0 = None
        host_vars_vars_0 = module_0.HostVarsVars(str_3, var_0)
        var_1 = iter(host_vars_vars_0)
        var_2 = next(var_1)
        var_3 = next(var_1)
        var_4 = next(var_1)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = ()
        int_0 = 4418
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, int_0)
        var_0 = host_vars_vars_0.__iter__()
        bytes_0 = b'%'
        str_0 = ',z`"t'
        dict_0 = {int_0: bytes_0, var_0: int_0, bytes_0: tuple_0, str_0: var_0}
        host_vars_0 = module_0.HostVars(str_0, host_vars_vars_0, dict_0)
        var_1 = host_vars_0.__repr__()
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -863.407453
        set_0 = set()
        int_0 = -212
        str_0 = 'B\nijU",WH+jBl\x0c'
        dict_0 = {int_0: float_0, str_0: int_0, str_0: str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, dict_0)
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_0, dict_0)
        var_0 = host_vars_0.__setstate__(dict_0)
        bytes_0 = b'\xa2\xc8\x04i\x19A\x98'
        host_vars_1 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, float_0)
        var_1 = host_vars_1.set_host_facts(bytes_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = ()
        str_0 = '`Uh\x0c0I;g\r='
        bool_0 = True
        list_0 = [str_0]
        host_vars_vars_0 = module_0.HostVarsVars(list_0, bool_0)
        host_vars_0 = module_0.HostVars(list_0, host_vars_vars_0, host_vars_vars_0)
        var_0 = host_vars_0.__contains__(tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        tuple_0 = ()
        bytes_0 = b'\x0f'
        bool_0 = False
        str_0 = ''
        set_0 = {str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, tuple_0)
        host_vars_0 = module_0.HostVars(bool_0, host_vars_vars_0, host_vars_vars_0)
        var_0 = host_vars_0.set_inventory(bytes_0)
        bool_1 = False
        str_1 = "Gfg'"
        host_vars_1 = module_0.HostVars(bool_1, bool_1, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        tuple_0 = ()
        bytes_0 = b'\x0f'
        bool_0 = False
        str_0 = ''
        set_0 = {str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, tuple_0)
        host_vars_0 = module_0.HostVars(bool_0, host_vars_vars_0, host_vars_vars_0)
        var_0 = host_vars_0.set_inventory(bytes_0)
        var_1 = host_vars_0.set_variable_manager(host_vars_0)
        bool_1 = False
        str_1 = "Gfg'"
        host_vars_1 = module_0.HostVars(bool_1, bool_1, str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        tuple_0 = ()
        str_0 = '\x0b\t\x0c'
        bytes_0 = b'\x0f'
        bool_0 = False
        str_1 = ''
        set_0 = {str_1}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, tuple_0)
        host_vars_0 = module_0.HostVars(bool_0, host_vars_vars_0, host_vars_vars_0)
        var_0 = host_vars_0.set_inventory(bytes_0)
        var_1 = host_vars_0.set_host_variable(str_0, host_vars_vars_0, host_vars_vars_0)
    except BaseException:
        pass

def test_case_15():
    try:
        tuple_0 = ()
        bytes_0 = b'\x0f'
        bool_0 = False
        str_0 = ''
        set_0 = {str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, tuple_0)
        host_vars_0 = module_0.HostVars(bool_0, host_vars_vars_0, host_vars_vars_0)
        var_0 = host_vars_0.set_inventory(bytes_0)
        var_1 = host_vars_0.__len__()
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = -863.407453
        bool_0 = True
        str_0 = 'cli: %s'
        dict_0 = {}
        host_vars_vars_0 = module_0.HostVarsVars(str_0, dict_0)
        var_0 = host_vars_vars_0.__getitem__(bool_0)
        set_0 = set()
        int_0 = -212
        str_1 = 'B\nijU",WH+jBl\x0c'
        dict_1 = {int_0: float_0, str_1: int_0, str_1: str_1}
        host_vars_vars_1 = module_0.HostVarsVars(set_0, dict_1)
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_1, dict_1)
        var_1 = host_vars_0.__setstate__(dict_1)
        bytes_0 = b'\xa2\xc8\x04i\x19A\x98'
        str_2 = 'HsW'
        bytes_1 = b'\xef\xceI\xe0\xfe/\x9d\n\xe0\x96\xa29\xa8\xda'
        host_vars_vars_2 = module_0.HostVarsVars(str_2, bytes_1)
        host_vars_1 = module_0.HostVars(host_vars_vars_2, host_vars_vars_2, float_0)
        var_2 = host_vars_1.set_host_facts(bytes_0, int_0)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = -863.407453
        set_0 = set()
        int_0 = -212
        str_0 = 'B\nijU",WH+jBl\x0c'
        dict_0 = {int_0: float_0, str_0: int_0, str_0: str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, dict_0)
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_0, dict_0)
        var_0 = host_vars_0.__setstate__(host_vars_0)
    except BaseException:
        pass

def test_case_18():
    try:
        float_0 = -827.921937765947
        set_0 = set()
        int_0 = -204
        str_0 = 'B\nijU",WH+jBl\x0c'
        dict_0 = {int_0: float_0, str_0: int_0, str_0: str_0}
        host_vars_vars_0 = module_0.HostVarsVars(set_0, dict_0)
        dict_1 = None
        host_vars_vars_1 = module_0.HostVarsVars(float_0, dict_1)
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_1, dict_0)
        var_0 = host_vars_0.__setstate__(dict_0)
        bytes_0 = b'\xa2\xc8\x04i\rA\x98'
        var_1 = host_vars_0.set_inventory(int_0)
        str_1 = 'BWkL/N'
        bytes_1 = b'\xef\xceI\xe0\xfe/\x9d\n\xe0\x96\xa29\xa8\xda'
        host_vars_vars_2 = module_0.HostVarsVars(str_1, bytes_1)
        host_vars_1 = module_0.HostVars(host_vars_vars_2, host_vars_vars_2, float_0)
        var_2 = host_vars_1.set_host_facts(bytes_0, int_0)
    except BaseException:
        pass