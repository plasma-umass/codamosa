# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        var_1 = vars_with_sources_0.copy()
        int_0 = 2087
        var_2 = module_0.preprocess_vars(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1.5
        str_0 = '\\*.dJ'
        list_0 = [str_0]
        variable_manager_0 = module_0.VariableManager()
        variable_manager_1 = module_0.VariableManager(list_0, variable_manager_0)
        variable_manager_2 = module_0.VariableManager(variable_manager_1)
        var_0 = variable_manager_2.get_vars(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        variable_manager_0 = module_0.VariableManager(dict_0)
        bool_0 = False
        var_0 = variable_manager_0.set_host_facts(variable_manager_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'display_failed_stderr'
        bytes_0 = b"\x9d_\x0e\x9a\x0f\x84\x01\xfe&A'S\xfb\xe7q\xaa\x89@\xd5\xdd"
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_nonpersistent_facts(str_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        variable_manager_0 = module_0.VariableManager(list_0)
        var_0 = variable_manager_0.__getstate__()
        str_0 = '`|\'/Q#\'y)vlZRS}w"'
        str_1 = 'j+NCzu$1'
        str_2 = 'repo'
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1}
        float_0 = -515.9
        var_1 = variable_manager_0.set_inventory(float_0)
        str_3 = 'gVz5#'
        str_4 = 'emerg'
        dict_1 = {str_3: str_3, str_3: str_3, str_3: str_4}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_1)
        var_2 = vars_with_sources_0.get_source(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = None
        str_0 = "Don't download collection(s) listed as dependencies."
        list_1 = []
        vars_with_sources_0 = module_0.VarsWithSources(*list_1)
        var_0 = vars_with_sources_0.__setitem__(list_0, str_0)
        str_1 = ']o<'
        str_2 = None
        dict_0 = {str_1: str_1, str_1: str_1, str_2: str_2}
        tuple_0 = (list_0,)
        variable_manager_0 = module_0.VariableManager(tuple_0)
        variable_manager_1 = module_0.VariableManager()
        var_1 = variable_manager_1.set_nonpersistent_facts(dict_0, variable_manager_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        vars_with_sources_0 = module_0.VarsWithSources(*list_0)
        var_0 = vars_with_sources_0.copy()
        bytes_0 = b'\xe2\x00\x9dH,\xd5\x80CZ\xba\x9d'
        variable_manager_0 = module_0.VariableManager(bytes_0)
        bytes_1 = None
        var_1 = variable_manager_0.set_host_variable(bytes_0, variable_manager_0, bytes_1)
        str_0 = 'suffix'
        str_1 = 'this loader can only load collections namespace packages, not {0}'
        dict_0 = {str_1: bytes_0}
        dict_1 = {str_0: dict_0}
        var_2 = variable_manager_0.set_inventory(dict_1)
        bool_0 = True
        var_3 = vars_with_sources_0.__delitem__(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\n    Data about an individual task.\n    '
        str_1 = ';BQ*.2k'
        dict_0 = {str_1: str_1}
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.__iter__()
        variable_manager_0 = module_0.VariableManager(dict_0)
        list_0 = [variable_manager_0]
        str_2 = 'armv3l'
        dict_1 = {str_0: list_0, str_0: str_0, str_2: dict_0}
        var_1 = variable_manager_0.set_nonpersistent_facts(dict_1, vars_with_sources_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xfe\xd4\xfe\x0f\x1d\xc4.4\xc3-9I\xe8d'
        bytes_1 = b'\xe2\x00\x9dH,\xd5\x80CZ\xba\x9d'
        list_0 = []
        vars_with_sources_0 = module_0.VarsWithSources(*list_0)
        var_0 = vars_with_sources_0.__len__()
        variable_manager_0 = module_0.VariableManager(bytes_1)
        bytes_2 = None
        var_1 = variable_manager_0.set_host_variable(bytes_0, variable_manager_0, bytes_2)
        str_0 = 'E]1\x0b"zRWx'
        var_2 = module_0.preprocess_vars(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        int_0 = 2087
        bool_0 = False
        var_1 = vars_with_sources_0.__contains__(bool_0)
        var_2 = module_0.preprocess_vars(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'l5'
        str_1 = 'S'
        str_2 = None
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_2}
        list_0 = []
        variable_manager_0 = module_0.VariableManager(list_0)
        var_0 = variable_manager_0.set_host_facts(dict_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        dict_0 = None
        var_1 = module_0.preprocess_vars(dict_0)
        bool_0 = True
        set_0 = None
        variable_manager_0 = module_0.VariableManager(bool_0, set_0)
        float_0 = -2109.8
        bool_1 = True
        var_2 = variable_manager_0.set_host_variable(vars_with_sources_0, float_0, bool_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '1{?S{'
        str_1 = '\\"\n&8>\rm \n]s(2n'
        dict_0 = {str_0: str_0, str_1: str_1, str_1: str_0}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        vars_with_sources_1 = None
        list_0 = [str_1, str_1, vars_with_sources_0, vars_with_sources_1]
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_nonpersistent_facts(list_0, dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'testhost'
        str_1 = 'new_variable'
        str_2 = 'new_value'
        var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
        str_3 = 'existing_variable'
        str_4 = 'old_value'
        var_1 = variable_manager_0.set_host_variable(str_0, str_3, str_4)
        str_5 = 'updated_value'
        var_2 = variable_manager_0.set_host_variable(str_0, str_3, str_5)
        str_6 = 'dict_variable'
        var_3 = variable_manager_0.set_host_variable(str_0, str_6, str_2)
        var_4 = variable_manager_0.set
    except BaseException:
        pass

def test_case_14():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'test_host'
        str_1 = 'simple_var'
        str_2 = 'CK2.'
        str_3 = '6Ec\x0bFIrdR~O'
        set_0 = {str_3, variable_manager_0}
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.__setitem__(str_3, set_0)
        var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
        str_4 = 'dict_var'
        str_5 = 'key1'
        str_6 = 'value1'
        str_7 = {str_5: str_6}
        list_0 = [str_6, str_7]
        var_2 = variable_manager_0.set_host_variable(str_0, str_4, str_7)
        float_0 = 100.0
        vars_with_sources_1 = module_0.VarsWithSources()
        var_3 = vars_with_sources_1.get_source(float_0)
        var_4 = variable_manager_0.set_host_variable(str_0, str_4, str_6)
        var_5 = variable_manager_0.set_host_facts(list_0, str_7)
    except BaseException:
        pass