# Automatically generated by Pynguin.
import ansible.utils.context_objects as module_0

def test_case_0():
    try:
        bool_0 = True
        global_c_l_i_args_0 = module_0.GlobalCLIArgs(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xd7k\x92Eb\x07@\x1ch'
        bool_0 = True
        float_0 = 1955.4783846579617
        list_0 = [float_0, bytes_0, bool_0]
        bool_1 = False
        dict_0 = {bool_0: bytes_0, bool_1: list_0, float_0: bool_0, bool_0: list_0}
        c_l_i_args_0 = module_0.CLIArgs(dict_0)
        set_0 = set()
        c_l_i_args_1 = module_0.CLIArgs(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'key1'
        str_1 = 'key2'
        str_2 = 'key5'
        int_0 = 1
        str_3 = 'key4'
        int_1 = 2
        int_2 = 3
        int_3 = 4
        int_4 = [int_2, int_3]
        int_5 = [int_0, int_1, int_4]
        int_6 = {str_1: int_1, str_3: int_5}
        str_4 = 'set1'
        str_5 = "~nmFuhx:1'pRIRjn/]"
        int_7 = {int_0, int_1, int_2}
        int_8 = 5
        int_9 = 6
        int_10 = {int_3, int_8, int_9, str_1, int_0}
        int_11 = {str_4: int_7, str_5: int_10}
        int_12 = {str_0: int_0, str_1: int_6, str_2: int_11}
        c_l_i_args_0 = module_0.CLIArgs(int_12)
        var_0 = c_l_i_args_0[int_0]
    except BaseException:
        pass