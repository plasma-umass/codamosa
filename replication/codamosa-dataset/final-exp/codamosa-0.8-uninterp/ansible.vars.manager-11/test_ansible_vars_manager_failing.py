# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    try:
        float_0 = None
        list_0 = [float_0]
        var_0 = module_0.preprocess_vars(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = module_0.preprocess_vars(vars_with_sources_0)
        dict_0 = None
        var_1 = vars_with_sources_0.get_source(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        variable_manager_0 = module_0.VariableManager()
        float_0 = -3128.884103
        tuple_0 = (float_0,)
        var_0 = module_0.preprocess_vars(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'Cmc'
        var_0 = variable_manager_0.__setstate__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        list_1 = [list_0]
        variable_manager_0 = module_0.VariableManager()
        dict_0 = {}
        var_0 = variable_manager_0.set_inventory(dict_0)
        var_1 = variable_manager_0.__setstate__(list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        variable_manager_0 = module_0.VariableManager()
        float_0 = -1442.89398
        list_0 = []
        str_0 = 'I~3\n910AThpa'
        str_1 = 'NpwC+8-xPK3_VC .,)ds'
        str_2 = '\x0c8`/IB+`3C/ ^'
        str_3 = '(required)'
        dict_0 = {str_0: variable_manager_0, str_1: list_0, str_2: list_0, str_3: str_0}
        vars_with_sources_0 = module_0.VarsWithSources(*list_0, **dict_0)
        var_0 = vars_with_sources_0.get_source(float_0)
        bool_0 = False
        float_1 = None
        set_0 = None
        tuple_0 = ()
        var_1 = variable_manager_0.clear_facts(tuple_0)
        var_2 = variable_manager_0.get_vars(bool_0, float_1, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 60.0
        str_0 = 'Qe'
        set_0 = {str_0}
        str_1 = 'wADThZSZ'
        float_1 = 3198.759
        variable_manager_0 = module_0.VariableManager(str_1, str_1, float_1)
        var_0 = variable_manager_0.set_host_variable(float_0, str_0, set_0)
        str_2 = '\x0c}'
        str_3 = '(?P<service>.*?)\\s+(?P<rl0>on|off)'
        dict_0 = {str_2: float_1, str_2: str_0, str_3: float_1}
        var_1 = variable_manager_0.clear_facts(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        variable_manager_0 = module_0.VariableManager()
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        var_0 = variable_manager_0.set_nonpersistent_facts(tuple_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        str_0 = '`4|Gu@b6e%R\nM'
        var_0 = vars_with_sources_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '^'
        bytes_0 = b'\xc5+7x\x11\xd6\xd6'
        str_1 = '!-8t\\im$?\r].W!"_R%'
        dict_0 = {str_0: str_0, str_0: bytes_0, str_1: bytes_0}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        var_0 = vars_with_sources_0.__getitem__(str_0)
        list_0 = [str_0, str_0, str_0]
        list_1 = [str_0]
        variable_manager_0 = module_0.VariableManager(list_1)
        var_1 = variable_manager_0.__setstate__(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        str_0 = '/GW^xX+6&?t%C=`gY|]'
        var_0 = vars_with_sources_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        str_0 = None
        str_1 = None
        variable_manager_0 = module_0.VariableManager(str_1)
        bool_1 = True
        list_0 = [bool_0, str_1]
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.__contains__(bool_1)
        var_1 = variable_manager_0.set_host_variable(str_1, bool_1, list_0)
        var_2 = variable_manager_0.__setstate__(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 3398
        set_0 = {int_0, int_0, int_0, int_0}
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_host_facts(int_0, set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 219
        int_1 = -1794
        variable_manager_0 = module_0.VariableManager(int_1)
        bool_0 = True
        str_0 = 'VX_@Rdl`opFO'
        tuple_0 = None
        str_1 = "[:!B\x0cq!'6@*"
        dict_0 = {str_0: int_0, str_0: int_1, str_0: tuple_0, str_1: tuple_0}
        list_0 = [bool_0, bool_0, dict_0]
        var_0 = variable_manager_0.set_host_facts(list_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        variable_manager_0 = module_0.VariableManager()
        int_0 = 1179
        bytes_0 = b'\xc4:\\\x8c7\xf8A\x03'
        float_0 = None
        dict_0 = {}
        var_0 = variable_manager_0.set_host_facts(float_0, dict_0)
        var_1 = variable_manager_0.__getstate__()
        dict_1 = {}
        var_2 = variable_manager_0.set_host_variable(int_0, bytes_0, dict_1)
        list_0 = [var_2, bytes_0]
        tuple_0 = (dict_1, list_0)
        var_3 = variable_manager_0.set_inventory(tuple_0)
        dict_2 = {}
        vars_with_sources_0 = module_0.VarsWithSources(*list_0, **dict_2)
    except BaseException:
        pass

def test_case_15():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'some_var'
        str_1 = 'some_value'
        str_2 = {str_0: str_1}
        var_0 = variable_manager_0.set_nonpersistent_facts(str_2, str_2)
    except BaseException:
        pass