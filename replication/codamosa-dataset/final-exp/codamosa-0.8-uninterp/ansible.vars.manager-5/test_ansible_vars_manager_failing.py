# Automatically generated by Pynguin.
import ansible.vars.manager as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        str_0 = '$yEkqRl([c_`oa\\_'
        var_0 = module_0.preprocess_vars(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = '9+Fn8~{f'
        bytes_0 = b'\x1c\x98\xd7\xdb'
        bool_0 = False
        tuple_0 = (str_0, bool_0)
        var_0 = variable_manager_0.set_host_variable(str_0, bytes_0, tuple_0)
        var_1 = variable_manager_0.__setstate__(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        int_0 = -1938
        list_0 = [int_0, vars_with_sources_0, int_0]
        bytes_0 = None
        float_0 = -1291.892957
        variable_manager_0 = module_0.VariableManager(float_0)
        var_0 = variable_manager_0.get_vars(vars_with_sources_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'L&$`Q=73svCwb[^vs;'
        vars_with_sources_0 = module_0.VarsWithSources()
        float_0 = 3457.5
        tuple_0 = (str_0, vars_with_sources_0, float_0)
        bool_0 = True
        var_0 = vars_with_sources_0.__iter__()
        variable_manager_0 = module_0.VariableManager()
        variable_manager_1 = module_0.VariableManager(bool_0, variable_manager_0)
        var_1 = variable_manager_1.clear_facts(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        variable_manager_0 = module_0.VariableManager()
        str_0 = "fpku|)J'(s{L"
        variable_manager_1 = module_0.VariableManager(variable_manager_0, str_0)
        variable_manager_2 = module_0.VariableManager()
        var_0 = variable_manager_2.set_host_variable(bool_0, variable_manager_1, str_0)
        variable_manager_3 = module_0.VariableManager()
        str_1 = 'b'
        int_0 = -14
        int_1 = {str_1: int_0}
        var_1 = variable_manager_3.set_host_facts(str_1, int_1)
        var_2 = variable_manager_3.set_host_facts(str_1, variable_manager_0)
    except BaseException:
        pass

def test_case_5():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_0 = {}
        host_0 = module_1.Host()
        vars_with_sources_1 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager(host_0, vars_with_sources_1)
        var_0 = variable_manager_0.set_nonpersistent_facts(vars_with_sources_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        str_0 = ''
        float_0 = None
        variable_manager_0 = module_0.VariableManager()
        var_1 = variable_manager_0.set_nonpersistent_facts(str_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x12t;]\xee\xdbL\xcb'
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        var_1 = module_0.preprocess_vars(bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        set_0 = set()
        var_0 = vars_with_sources_0.__delitem__(set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        variable_manager_0 = module_0.VariableManager()
        str_0 = "fpku|)J'(s{L"
        variable_manager_1 = module_0.VariableManager(variable_manager_0, str_0)
        variable_manager_2 = module_0.VariableManager()
        var_0 = variable_manager_2.set_host_variable(bool_0, variable_manager_1, str_0)
        variable_manager_3 = module_0.VariableManager()
        dict_0 = {str_0: variable_manager_2}
        list_0 = [dict_0]
        vars_with_sources_0 = module_0.VarsWithSources(*list_0)
        var_1 = variable_manager_1.set_host_facts(list_0, vars_with_sources_0)
    except BaseException:
        pass

def test_case_10():
    try:
        tuple_0 = None
        list_0 = [tuple_0, tuple_0]
        var_0 = module_0.preprocess_vars(list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.__iter__()
        variable_manager_0 = module_0.VariableManager()
        bool_0 = False
        var_1 = vars_with_sources_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '>Xu\t'
        float_0 = 1194.067
        str_1 = ':=LwXq{\\A.=r*<\n`}Ho1'
        str_2 = 'n\x0ca\t\\WK-O+xYY\x0b2BJ'
        dict_0 = {str_0: float_0, str_0: str_0, str_1: str_1, str_2: str_0}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        var_0 = vars_with_sources_0.copy()
        tuple_0 = None
        dict_1 = {tuple_0: tuple_0}
        variable_manager_0 = module_0.VariableManager()
        var_1 = variable_manager_0.__setstate__(dict_1)
        vars_with_sources_1 = module_0.VarsWithSources()
        var_2 = vars_with_sources_1.copy()
        var_3 = vars_with_sources_1.copy()
        variable_manager_1 = module_0.VariableManager(vars_with_sources_1)
        list_0 = [variable_manager_1]
        dict_2 = None
        vars_with_sources_2 = module_0.VarsWithSources(*list_0, **dict_2)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = "\n    reversible allows two way conversion of a camelized dict\n    such that snake_dict_to_camel_dict(camel_dict_to_snake_dict(x)) == x\n\n    This is achieved through mapping e.g. HTTPEndpoint to h_t_t_p_endpoint\n    where the default would be simply http_endpoint, which gets turned into\n    HttpEndpoint if recamelized.\n\n    ignore_list is used to avoid converting a sub-tree of a dict. This is\n    particularly important for tags, where keys are case-sensitive. We convert\n    the 'Tags' key but nothing below.\n    "
        dict_0 = {str_0: str_0}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        list_0 = [vars_with_sources_0]
        vars_with_sources_1 = module_0.VarsWithSources(*list_0)
        list_1 = [vars_with_sources_1, dict_0]
        vars_with_sources_2 = module_0.VarsWithSources(*list_1)
    except BaseException:
        pass