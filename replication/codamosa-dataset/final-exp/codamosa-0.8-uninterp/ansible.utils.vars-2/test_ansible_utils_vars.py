# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_unique_id()

def test_case_2():
    str_0 = 'merge'
    str_1 = '4\rXG/o8U.GI\ro"d;'
    dict_0 = {str_0: str_1}
    dict_1 = {str_1: str_1}
    var_0 = module_0.merge_hash(dict_0, dict_1)

def test_case_3():
    bool_0 = True
    var_0 = module_0.load_extra_vars(bool_0)

def test_case_4():
    str_0 = 'Q!Hu?t "\t_l#'
    var_0 = module_0.load_options_vars(str_0)

def test_case_5():
    str_0 = "@h>=3)lYJ+6NG'fu@H"
    var_0 = module_0._isidentifier_PY3(str_0)

def test_case_6():
    tuple_0 = ()
    var_0 = module_0._isidentifier_PY3(tuple_0)

def test_case_7():
    str_0 = 'foo'
    str_1 = 'bar'
    str_2 = {str_0: str_1}
    str_3 = 'new_bar'
    str_4 = {str_0: str_3}
    var_0 = module_0.combine_vars(str_2, str_4)
    str_5 = 'baz'
    str_6 = {str_1: str_5}
    str_7 = {str_0: str_6}
    str_8 = {str_0: str_3}
    var_1 = module_0.combine_vars(str_7, str_8)
    str_9 = {str_0: str_1}
    str_10 = {str_1: str_5}
    str_11 = {str_0: str_10}
    var_2 = module_0.combine_vars(str_9, str_11)
    str_12 = {str_0: str_1}
    str_13 = {str_1: str_5}
    str_14 = {str_0: str_13}
    bool_0 = False
    var_3 = module_0.combine_vars(str_12, str_14, bool_0)

def test_case_8():
    str_0 = 'nmZ'
    str_1 = 'services'
    str_2 = 'keep'
    str_3 = 'bob'
    str_4 = 'vv'
    str_5 = [str_1, str_4]
    str_6 = 'ubuntu'
    str_7 = '14.04'
    str_8 = {str_0: str_6, str_7: str_7}
    str_9 = {str_0: str_3, str_1: str_5, str_2: str_8}
    str_10 = [str_9]
    str_11 = {str_0: str_5, str_1: str_10, str_2: str_1}
    var_0 = module_0.merge_hash(str_9, str_11)

def test_case_9():
    str_0 = 'abcd'
    var_0 = module_0._isidentifier_PY3(str_0)
    str_1 = 'ABCD'
    var_1 = module_0._isidentifier_PY3(str_1)
    str_2 = 'abc123'
    var_2 = module_0._isidentifier_PY3(str_2)
    str_3 = '_'
    var_3 = module_0._isidentifier_PY3(str_3)
    str_4 = '123'
    var_4 = module_0._isidentifier_PY3(str_4)
    str_5 = 'True'
    var_5 = module_0._isidentifier_PY3(str_5)
    str_6 = 'False'
    var_6 = module_0._isidentifier_PY3(str_6)
    var_7 = module_0._isidentifier_PY3(str_4)
    var_8 = module_0._isidentifier_PY3(str_3)
    str_7 = 'é'
    var_9 = module_0._isidentifier_PY3(str_7)

def test_case_10():
    str_0 = 'a'
    str_1 = {str_0: str_0}
    str_2 = 'b'
    str_3 = {str_0: str_2}
    bool_0 = False
    str_4 = 'replace'
    var_0 = module_0.merge_hash(str_1, str_3, bool_0, str_4)
    str_5 = {str_0: str_0}
    str_6 = {str_0: str_2}
    str_7 = 'keep'
    var_1 = module_0.merge_hash(str_5, str_6, bool_0, str_7)
    str_8 = [str_0, str_2]
    str_9 = {str_0: str_0, str_2: str_8}
    str_10 = {str_0: str_2}
    var_2 = module_0.merge_hash(str_9, str_10, bool_0, str_4)
    str_11 = [str_0, str_2]
    str_12 = {str_0: str_0, str_2: str_11}
    str_13 = {str_0: str_2}
    var_3 = module_0.merge_hash(str_12, str_13, bool_0, str_7)

def test_case_11():
    str_0 = 'nmZ'
    str_1 = 'services'
    str_2 = 'keep'
    str_3 = 'vv'
    str_4 = [str_1, str_3]
    str_5 = 'ubuntu'
    str_6 = '14.04'
    str_7 = {str_0: str_5, str_6: str_6}
    str_8 = {str_0: str_1, str_1: str_4, str_2: str_7}
    str_9 = [str_8]
    str_10 = '16.04'
    str_11 = {str_1: str_10}
    str_12 = {str_0: str_4, str_1: str_9, str_2: str_11}
    var_0 = module_0.merge_hash(str_8, str_12)