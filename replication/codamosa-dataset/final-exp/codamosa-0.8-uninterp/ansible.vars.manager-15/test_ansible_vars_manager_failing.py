# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    try:
        str_0 = None
        dict_0 = {str_0: str_0}
        float_0 = 2153.2373393016146
        str_1 = ']L. .f3]'
        vars_with_sources_0 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_host_facts(float_0, vars_with_sources_0)
        list_0 = []
        list_1 = [str_1, list_0, dict_0]
        var_1 = module_0.preprocess_vars(list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '0;35'
        variable_manager_0 = module_0.VariableManager()
        variable_manager_1 = module_0.VariableManager()
        var_0 = module_0.preprocess_vars(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        variable_manager_0 = module_0.VariableManager()
        list_0 = []
        bytes_0 = b'A\x81E~\x03\x17\x92[/S\xd2\xcbH'
        var_0 = variable_manager_0.__getstate__()
        str_0 = 'U=aVtKLrx\\\n2DH'
        var_1 = variable_manager_0.set_inventory(str_0)
        var_2 = variable_manager_0.set_nonpersistent_facts(list_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 1540
        dict_0 = {int_0: int_0, int_0: int_0}
        str_0 = 'yW'
        str_1 = "KlBTW0mS5'[H[FQ"
        dict_1 = {str_0: int_0, str_1: str_1, str_0: int_0, str_1: int_0}
        bytes_0 = b'\xa5l\xea%~\xf4H\xb0\xe9\x16pT\n`\xb8\x8a'
        variable_manager_0 = module_0.VariableManager(bytes_0)
        var_0 = variable_manager_0.__setstate__(dict_1)
        variable_manager_1 = module_0.VariableManager()
        var_1 = variable_manager_1.set_host_facts(dict_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x94\xcd\xed\xa7Qh'
        str_0 = '\\6auNyA\x0cxBC%>yFk-'
        str_1 = 'x'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_1: str_1}
        variable_manager_0 = module_0.VariableManager(dict_0)
        var_0 = variable_manager_0.get_vars(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '&^^'
        float_0 = -3937.603
        str_1 = 'h\tPB*%8&{E'
        str_2 = '~Y<-[g"J\r=>w6.'
        dict_0 = {str_0: str_0, str_1: str_1, str_1: str_0, str_2: float_0}
        set_0 = set()
        variable_manager_0 = module_0.VariableManager(dict_0, set_0)
        var_0 = variable_manager_0.__getstate__()
        str_3 = 'Rtf'
        variable_manager_1 = module_0.VariableManager(str_3)
        variable_manager_2 = module_0.VariableManager(float_0, variable_manager_1)
        bytes_0 = b'v\xac\xfam\xdf'
        var_1 = variable_manager_2.clear_facts(bytes_0)
        var_2 = variable_manager_2.__setstate__(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        bytes_0 = b'\x8d\x0b\x8ds\xf3\x97O\xc7EXNK'
        variable_manager_0 = module_0.VariableManager(bytes_0)
        variable_manager_1 = module_0.VariableManager(variable_manager_0)
        var_0 = variable_manager_1.set_host_facts(dict_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        dict_0 = {}
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_nonpersistent_facts(list_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -808
        dict_0 = None
        vars_with_sources_0 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager(vars_with_sources_0, vars_with_sources_0)
        var_0 = variable_manager_0.set_nonpersistent_facts(int_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'the downloaded file does not appear to be a valid tar archive.'
        float_0 = -3463.7507
        list_0 = [str_0, float_0]
        dict_0 = {str_0: str_0, str_0: list_0}
        set_0 = {str_0, float_0, str_0}
        str_1 = 'a|Ja\n\x0c9\x0cLqPKm%^o7'
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_host_variable(dict_0, set_0, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        int_0 = -1122
        var_0 = vars_with_sources_0.get_source(int_0)
        float_0 = -3311.6
        variable_manager_0 = module_0.VariableManager(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = None
        variable_manager_0 = module_0.VariableManager(str_0)
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_0 = {str_0: str_0, str_0: vars_with_sources_0}
        var_0 = module_0.preprocess_vars(dict_0)
        vars_with_sources_1 = module_0.VarsWithSources()
        var_1 = vars_with_sources_1.__iter__()
        str_1 = 'A|U\x0cTqiq*7umnB(O'
        variable_manager_1 = module_0.VariableManager(str_1)
        vars_with_sources_2 = module_0.VarsWithSources()
        var_2 = vars_with_sources_0.__getitem__(vars_with_sources_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = None
        dict_0 = {str_0: str_0}
        float_0 = 2150.328
        str_1 = '&U.{)'
        variable_manager_0 = module_0.VariableManager(str_1)
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_1 = {str_1: str_1, str_0: vars_with_sources_0}
        var_0 = module_0.preprocess_vars(dict_1)
        vars_with_sources_1 = module_0.VarsWithSources()
        var_1 = vars_with_sources_1.__iter__()
        var_2 = vars_with_sources_1.copy()
        var_3 = vars_with_sources_1.__setitem__(dict_0, float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_0 = {}
        var_0 = vars_with_sources_0.__delitem__(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = 2.0
        str_0 = 'QU_;"a>"5/ Lt9Dh'
        vars_with_sources_0 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager()
        str_1 = '7Z0@hq9+\\7AI8(OZ|sN'
        set_0 = set()
        var_0 = variable_manager_0.set_host_variable(float_0, str_1, set_0)
        var_1 = variable_manager_0.set_host_facts(float_0, vars_with_sources_0)
        int_0 = -1782
        var_2 = vars_with_sources_0.__len__()
        variable_manager_1 = module_0.VariableManager(str_0)
        var_3 = variable_manager_1.set_nonpersistent_facts(int_0, set_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = 2.0
        str_0 = 'QU_;"a>"5/ Lt9Dh'
        str_1 = ']l. .B3]'
        vars_with_sources_0 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager()
        list_0 = [str_1, variable_manager_0]
        str_2 = '7Z0@hq9+\\7AI8(OZ|sN'
        var_0 = vars_with_sources_0.__contains__(str_0)
        set_0 = set()
        var_1 = variable_manager_0.set_host_variable(float_0, str_2, set_0)
        var_2 = variable_manager_0.set_inventory(list_0)
        var_3 = variable_manager_0.set_host_facts(float_0, vars_with_sources_0)
        int_0 = -1782
        set_1 = {float_0, int_0, str_1}
        var_4 = vars_with_sources_0.__len__()
        bool_0 = False
        str_3 = '$tvi\x0bdP:%FfYS:'
        var_5 = variable_manager_0.set_host_variable(bool_0, str_1, str_3)
        variable_manager_1 = module_0.VariableManager(str_0)
        var_6 = variable_manager_1.set_nonpersistent_facts(int_0, set_1)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b''
        str_0 = '_V;-X#&1'
        list_0 = None
        dict_0 = {str_0: str_0, str_0: str_0, str_0: list_0, str_0: bytes_0}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        var_0 = vars_with_sources_0.copy()
        variable_manager_0 = module_0.VariableManager()
        var_1 = variable_manager_0.set_host_facts(dict_0, dict_0)
    except BaseException:
        pass