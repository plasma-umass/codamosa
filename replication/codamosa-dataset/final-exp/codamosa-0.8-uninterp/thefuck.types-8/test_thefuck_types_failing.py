# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    try:
        int_0 = 10
        list_0 = []
        corrected_command_0 = module_0.CorrectedCommand(list_0, list_0, list_0)
        var_0 = corrected_command_0.__repr__()
        var_1 = corrected_command_0.run(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        set_0 = set()
        bytes_0 = b';\xa45\xba]\x80\x81\x91\xacN\x95'
        corrected_command_0 = module_0.CorrectedCommand(bool_0, set_0, bytes_0)
        float_0 = -2982.1
        var_0 = corrected_command_0.__eq__(float_0)
        tuple_0 = ()
        var_1 = corrected_command_0.run(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x14^K\x7f\xb6j\x83\x8d$ak'
        list_0 = [bytes_0, bytes_0, bytes_0]
        list_1 = [bytes_0, bytes_0, bytes_0, list_0]
        str_0 = '>9:p,#'
        corrected_command_0 = module_0.CorrectedCommand(list_1, str_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        str_0 = 'l?)'
        dict_0 = {str_0: list_0, str_0: str_0}
        float_0 = -508.77484
        corrected_command_0 = module_0.CorrectedCommand(list_0, dict_0, float_0)
        var_0 = corrected_command_0.__repr__()
        bool_0 = True
        set_0 = {bool_0}
        bytes_0 = b';\xa45\xba]\x80\x81\x91\xacN\x95'
        corrected_command_1 = module_0.CorrectedCommand(bool_0, set_0, bytes_0)
        tuple_0 = ()
        var_1 = corrected_command_1.run(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        bytes_0 = b'\x94\xcd\xd6\xad'
        bytes_1 = b'\xf1\xb8\t\xcd\x03[\x93\xf4v|\xd5M\xc09\xff9\xe5\xa9\x0c\xca'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_1}
        float_0 = 0.5
        set_0 = set()
        command_0 = module_0.Command(float_0, set_0)
        int_0 = -206
        str_0 = 'sLtBwo'
        corrected_command_0 = module_0.CorrectedCommand(int_0, str_0, dict_0)
        var_0 = command_0.__eq__(command_0)
        str_1 = ';'
        tuple_0 = (list_0, str_1, dict_0, dict_0)
        var_1 = corrected_command_0.run(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 3250.2926
        bytes_0 = b'\xe7\xa6C\x12&\xd9\xbd\x83_'
        float_1 = -5144.178
        dict_0 = {}
        list_0 = [dict_0]
        bytes_1 = b'\xc9C\x8dl\x12-\xda\xffx-\x13z\x9c\xd0\x1f\x9bq\xcf'
        str_0 = 'XH 6[i`s7g@ii)=1TYRu'
        float_2 = -2179.027
        list_1 = [float_1, float_0, float_2]
        list_2 = [bytes_1]
        corrected_command_0 = module_0.CorrectedCommand(list_1, str_0, list_2)
        bool_0 = False
        set_0 = {bool_0}
        corrected_command_1 = module_0.CorrectedCommand(bool_0, list_0, set_0)
        var_0 = corrected_command_1.__eq__(corrected_command_0)
        bytes_2 = b'\xcfi\x88-\xf0\xc6\xb1\xb0R\xa8\xb9\xd1\xfd\x1a\x0b\x1e!\x15\xd7\x94'
        rule_0 = module_0.Rule(float_0, list_0, bytes_1, bytes_0, str_0, bytes_0, bytes_2)
        var_1 = rule_0.__repr__()
        int_0 = -447
        dict_1 = {int_0: dict_0}
        bool_1 = False
        str_1 = '~'
        dict_2 = {str_1: dict_1}
        command_0 = module_0.Command(bool_1, dict_2)
        str_2 = 'R?s_@Sz\x0bK5 '
        str_3 = '--alias'
        corrected_command_2 = module_0.CorrectedCommand(str_3, bytes_0, dict_1)
        set_1 = {str_2}
        list_3 = [command_0, dict_2]
        bytes_3 = b'eN\x96\x15F\xf5&\xbe!a\x197\x83Zs\x85m'
        float_3 = -1642.4
        rule_1 = module_0.Rule(str_2, corrected_command_2, set_1, list_3, bytes_3, float_3, dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    Test that the is_match method of class Rule works properly.\n    '
        bool_0 = True
        var_0 = lambda cmd: bool_0
        int_0 = 95
        rule_0 = module_0.Rule(str_0, var_0, str_0, bool_0, bool_0, int_0, bool_0)
        str_1 = 'test_script'
        list_0 = [str_1, int_0]
        var_1 = rule_0.__eq__(rule_0)
        dict_0 = {}
        list_1 = [var_1, list_0]
        tuple_0 = (list_1,)
        command_0 = module_0.Command(dict_0, tuple_0)
        str_2 = 'D_,n(M#|z"ndrqs{y*'
        var_2 = rule_0.is_match(str_2)
    except BaseException:
        pass