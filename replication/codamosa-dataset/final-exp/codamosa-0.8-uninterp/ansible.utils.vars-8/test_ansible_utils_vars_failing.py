# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    try:
        tuple_0 = ()
        bytes_0 = b'0mE\xef\x8a\xc2\x7f\xa6\xab+\xeb\x8b*\x9e\xf9\xe5\x97V'
        var_0 = module_0.combine_vars(tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        str_0 = 'b6!~d'
        bool_0 = False
        tuple_0 = (bool_0,)
        var_0 = module_0.combine_vars(list_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1831
        bytes_0 = b'\x91\xe4\x87\xd3I\xf0{\xe7$\x96\xe0l'
        var_0 = module_0.merge_hash(int_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xf3\xc0I\xc1\xad\xb1\xd6\xdbD\xaf'
        tuple_0 = ()
        dict_0 = {bytes_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, bytes_0: bytes_0}
        str_0 = None
        var_0 = module_0.merge_hash(tuple_0, dict_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ' '
        bool_0 = True
        dict_0 = {str_0: str_0, bool_0: bool_0}
        str_1 = 'V^J_]wRXOP%s\x0c,'
        str_2 = '\'6RZ"Lc'
        var_0 = module_0.merge_hash(dict_0, str_1, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'nsoch_int'
        bool_0 = True
        var_0 = module_0._isidentifier_PY3(bool_0)
        var_1 = module_0.get_unique_id()
        int_0 = -1623
        var_2 = module_0._isidentifier_PY3(str_0)
        str_1 = 'a{TnD\n*4}P'
        dict_0 = {str_0: str_0, int_0: int_0, str_1: var_2}
        dict_1 = {str_1: str_0, str_0: bool_0, str_0: dict_0, var_2: var_1}
        var_3 = module_0.merge_hash(dict_1, dict_0)
        var_4 = module_0._isidentifier_PY3(int_0)
        str_2 = '3fbtU"O(4oR]%"5k'
        var_5 = module_0.load_extra_vars(str_2)
        var_6 = module_0.load_options_vars(str_0)
        bytes_0 = b'\xfe6$\xeal\x9c\xd7\xa3j\xb1gzc\xacB\x94\xb1n\x12\xac'
        tuple_0 = (bool_0, bytes_0)
        dict_2 = {bytes_0: bytes_0, int_0: bool_0, str_0: bytes_0}
        var_7 = module_0.get_unique_id()
        var_8 = module_0.combine_vars(dict_2, var_6, dict_2)
        var_9 = module_0.load_options_vars(tuple_0)
        bytes_1 = b'\x1e\xd3B\xa6\xedd\xde\x9ew'
        var_10 = module_0._isidentifier_PY3(bool_0)
        var_11 = module_0.combine_vars(bytes_1, int_0)
    except BaseException:
        pass