# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_unique_id()

def test_case_2():
    float_0 = 3633.0
    var_0 = module_0.load_extra_vars(float_0)

def test_case_3():
    str_0 = '1.0'
    var_0 = module_0.load_options_vars(str_0)

def test_case_4():
    bool_0 = True
    var_0 = module_0._isidentifier_PY3(bool_0)
    dict_0 = None
    var_1 = module_0.load_options_vars(dict_0)

def test_case_5():
    str_0 = 'merge'
    var_0 = module_0._isidentifier_PY3(str_0)

def test_case_6():
    float_0 = -1845.7
    var_0 = module_0._isidentifier_PY3(float_0)
    str_0 = '6C>dM6T4c81'
    var_1 = module_0._isidentifier_PY3(str_0)

def test_case_7():
    float_0 = -1845.7
    var_0 = module_0._isidentifier_PY3(float_0)

def test_case_8():
    bool_0 = False
    var_0 = module_0.load_options_vars(bool_0)
    str_0 = 'F'
    var_1 = module_0._isidentifier_PY3(str_0)
    dict_0 = {str_0: str_0}
    float_0 = -20.7776450570256
    str_1 = 'qI2>Ts'
    set_0 = set()
    var_2 = module_0.load_options_vars(set_0)
    var_3 = module_0._isidentifier_PY3(str_1)
    var_4 = module_0.combine_vars(dict_0, dict_0, float_0)

def test_case_9():
    var_0 = module_0.get_unique_id()
    int_0 = 156
    var_1 = module_0._isidentifier_PY3(int_0)
    var_2 = module_0.get_unique_id()
    str_0 = 'x'
    var_3 = module_0._isidentifier_PY3(str_0)
    int_1 = 86
    var_4 = module_0.load_options_vars(int_1)
    dict_0 = {str_0: str_0}
    float_0 = 2440.671
    var_5 = module_0.load_options_vars(dict_0)
    list_0 = [float_0, var_0, var_4]
    var_6 = module_0.load_extra_vars(list_0)
    bytes_0 = b'M\x1d\xc7\xf95ev\xc1\x99'
    var_7 = module_0.load_extra_vars(bytes_0)
    var_8 = module_0.load_extra_vars(int_1)
    str_1 = 'qI2>Ts'
    var_9 = module_0._isidentifier_PY3(str_1)
    var_10 = module_0.combine_vars(dict_0, dict_0)

def test_case_10():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = 'x'
    str_4 = 'y'
    str_5 = 'foo'
    str_6 = 'bar'
    str_7 = {str_5: str_6}
    str_8 = {str_0: str_1, str_1: str_7, str_2: str_3}
    str_9 = [str_4, str_8]
    str_10 = 'baz'
    str_11 = {str_5: str_10}
    str_12 = {str_0: str_9, str_1: str_11, str_2: str_4}
    bool_0 = False
    str_13 = 'replace'
    var_0 = module_0.merge_hash(str_8, str_12, bool_0, str_13)

def test_case_11():
    str_0 = 'a'
    str_1 = 'k'
    str_2 = 'l'
    str_3 = 'n'
    str_4 = 'b'
    str_5 = '1'
    str_6 = '2'
    str_7 = {str_4: str_5, str_6: str_6}
    str_8 = '3'
    var_0 = {}
    var_1 = {str_0: str_7, str_1: str_8, str_2: str_6, str_3: var_0}
    str_9 = 'd'
    str_10 = '4'
    str_11 = {str_4: str_6, str_9: str_10}
    str_12 = {str_0: str_11}
    var_2 = module_0.merge_hash(var_1, str_12)
    str_13 = {str_3: str_6}
    str_14 = {str_4: str_13}
    str_15 = {str_0: str_14}
    bool_0 = True
    var_3 = module_0.merge_hash(var_1, str_15, bool_0)

def test_case_12():
    var_0 = {}
    str_0 = 'a'
    int_0 = 1
    int_1 = {str_0: int_0}
    var_1 = module_0.merge_hash(var_0, int_1)
    int_2 = {str_0: int_0}
    var_2 = {}
    var_3 = module_0.merge_hash(int_2, var_2)
    int_3 = {str_0: int_0}
    int_4 = {str_0: int_0}
    var_4 = module_0.merge_hash(int_3, int_4)
    str_1 = 'c'
    int_5 = {str_1: int_0}
    int_6 = {str_0: int_0, str_0: int_5}
    int_7 = {str_1: int_0}
    int_8 = {str_0: int_0, str_1: int_7}
    var_5 = module_0.merge_hash(int_6, int_8)
    var_6 = module_0.load_extra_vars(int_3)
    var_7 = module_0._isidentifier_PY3(int_2)

def test_case_13():
    str_0 = 'valid'
    var_0 = module_0._isidentifier_PY3(str_0)
    str_1 = '__valid'
    var_1 = module_0._isidentifier_PY3(str_1)
    str_2 = '__válid'
    var_2 = module_0._isidentifier_PY3(str_2)
    str_3 = '_válid'
    var_3 = module_0._isidentifier_PY3(str_3)
    str_4 = '_válid_'
    var_4 = module_0._isidentifier_PY3(str_4)
    str_5 = '1valid'
    var_5 = module_0._isidentifier_PY3(str_5)
    str_6 = 'if'
    var_6 = module_0._isidentifier_PY3(str_6)
    str_7 = 'while'
    var_7 = module_0._isidentifier_PY3(str_7)

def test_case_14():
    var_0 = {}
    var_1 = {}
    bool_0 = True
    str_0 = 'replace'
    var_2 = module_0.merge_hash(var_0, var_1, bool_0, str_0)
    str_1 = 'a'
    str_2 = 'b'
    str_3 = '1'
    str_4 = '2'
    str_5 = {str_1: str_3, str_2: str_4}
    str_6 = 'c'
    str_7 = '3'
    str_8 = '4'
    str_9 = {str_2: str_7, str_6: str_8}
    var_3 = module_0.merge_hash(str_5, str_9, bool_0, str_0)
    str_10 = [str_3, str_4]
    str_11 = {str_1: str_10}
    str_12 = [str_7, str_8]
    str_13 = {str_1: str_12}
    var_4 = module_0.merge_hash(str_11, str_13, bool_0, str_0)
    str_14 = [str_3, str_4]
    str_15 = {str_1: str_14}
    str_16 = [str_7, str_8]
    str_17 = {str_1: str_16}
    str_18 = 'keep'
    var_5 = module_0.merge_hash(str_15, str_17, bool_0, str_18)

def test_case_15():
    var_0 = {}
    var_1 = {}
    bool_0 = False
    str_0 = 'replace'
    var_2 = module_0.merge_hash(var_0, var_1, bool_0, str_0)
    var_3 = {}
    str_1 = 'foo'
    int_0 = 42
    int_1 = {str_1: int_0}
    var_4 = module_0.merge_hash(var_3, int_1, bool_0, str_0)
    int_2 = {str_1: int_0}
    var_5 = {}
    var_6 = module_0.merge_hash(int_2, var_5, bool_0, str_0)
    var_7 = {}
    var_8 = {}
    str_2 = 'keep'
    var_9 = module_0.merge_hash(var_7, var_8, bool_0, str_2)
    var_10 = {}
    int_3 = {str_1: int_0}
    var_11 = module_0.merge_hash(var_10, int_3, bool_0, str_2)
    int_4 = {str_1: int_0}
    var_12 = {}
    var_13 = module_0.merge_hash(int_4, var_12, bool_0, str_2)
    var_14 = {}
    var_15 = {}
    str_3 = 'append'
    var_16 = module_0.merge_hash(var_14, var_15, bool_0, str_3)
    var_17 = {}
    int_5 = {str_1: int_0}
    var_18 = module_0.merge_hash(var_17, int_5, bool_0, str_3)