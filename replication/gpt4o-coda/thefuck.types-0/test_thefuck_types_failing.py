# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    try:
        list_0 = None
        int_0 = -1439
        bytes_0 = b''
        corrected_command_0 = module_0.CorrectedCommand(int_0, bytes_0, list_0)
        var_0 = corrected_command_0.run(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc1\x97o"\xda.2\x95{\xdaEy=\x06'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        list_0 = [set_0, bytes_0]
        list_1 = [bytes_0, bytes_0]
        command_0 = module_0.Command(list_0, list_1)
        str_0 = 'V^JG6?s\r\x0cWHQ@'
        tuple_0 = (str_0, command_0)
        corrected_command_0 = module_0.CorrectedCommand(tuple_0, command_0, command_0)
        var_0 = corrected_command_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        bool_0 = False
        int_0 = 4000
        float_0 = -1749.682
        list_0 = [dict_0, float_0]
        str_0 = '"UQ}'
        str_1 = 'TF_SHELL_ALIASES'
        dict_1 = {str_0: dict_0, str_0: float_0, str_1: bool_0}
        bool_1 = True
        bytes_0 = b'\xf6'
        str_2 = 'fatal: No such remote'
        rule_0 = module_0.Rule(list_0, dict_1, bool_1, bytes_0, str_2, dict_1, dict_0)
        bytes_1 = b'\x08\xe2j9 k&\xc0\xb4'
        corrected_command_0 = module_0.CorrectedCommand(rule_0, int_0, bytes_1)
        var_0 = corrected_command_0.run(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        bytes_0 = b'\tS\x05\x17v\xd54&\x9c+\xc2'
        set_0 = set()
        command_0 = module_0.Command(bytes_0, set_0)
        var_0 = command_0.__eq__(command_0)
        str_0 = 'z'
        command_1 = module_0.Command(str_0, set_0)
        tuple_0 = (int_0, command_0)
        list_0 = [tuple_0]
        command_2 = module_0.Command(tuple_0, list_0)
        bool_0 = True
        dict_0 = {}
        float_0 = 0.1
        corrected_command_0 = module_0.CorrectedCommand(dict_0, float_0, dict_0)
        str_1 = '6[>\x0b<j1F*~@+zwAQWi\x0c'
        corrected_command_1 = module_0.CorrectedCommand(command_0, str_1, tuple_0)
        tuple_1 = (command_2, bool_0, corrected_command_0, corrected_command_1)
        bool_1 = False
        command_3 = module_0.Command(tuple_1, bool_1)
        str_2 = 'Hx<\n01'
        int_1 = 10
        str_3 = '\x0bvfpZ!<$*<q/\x0bf'
        list_1 = [set_0, command_1]
        str_4 = '2)q`t%,vi\rz\t8'
        dict_1 = {}
        int_2 = 482
        command_4 = module_0.Command(corrected_command_0, int_2)
        rule_0 = module_0.Rule(list_1, command_3, str_3, str_4, tuple_0, dict_1, command_4)
        corrected_command_2 = module_0.CorrectedCommand(str_2, int_1, str_3)
        bytes_1 = b'\x00\x92F6\xd1$k'
        corrected_command_3 = module_0.CorrectedCommand(bool_1, bytes_1, bool_0)
        command_5 = module_0.Command(command_3, corrected_command_2)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'L\\:\x0c\x91'
        dict_0 = {bytes_0: bytes_0}
        bool_0 = False
        float_0 = None
        command_0 = module_0.Command(bytes_0, float_0)
        bytes_1 = None
        str_0 = '296cMqQ+-\\)Q^&R='
        command_1 = module_0.Command(bytes_1, str_0)
        float_1 = 2496.04
        int_0 = -1163
        list_0 = [bytes_0, float_1, int_0, bool_0]
        str_1 = 'WX\t[T'
        bytes_2 = b'J0\x1a'
        dict_1 = {str_1: str_1}
        float_2 = -183.633
        var_0 = command_0.__eq__(float_2)
        rule_0 = None
        var_1 = command_1.__eq__(rule_0)
        rule_1 = module_0.Rule(float_1, int_0, list_0, str_1, bytes_2, dict_1, bool_0)
        str_2 = 'k)8CCBM'
        var_2 = rule_1.__repr__()
        str_3 = "w-'jFm7"
        tuple_0 = None
        float_3 = 3838.9
        float_4 = -1637.49377
        bool_1 = False
        str_4 = 'dxH*VbhRC[(8<DEt'
        rule_2 = module_0.Rule(str_3, tuple_0, float_3, float_4, bool_1, dict_1, str_4)
        list_1 = []
        corrected_command_0 = module_0.CorrectedCommand(dict_1, list_1, command_0)
        set_0 = set()
        var_3 = rule_1.__repr__()
        rule_3 = module_0.Rule(str_2, dict_1, list_1, corrected_command_0, set_0, dict_0, corrected_command_0)
        var_4 = rule_1.is_match(command_0)
        float_5 = 1165.4
        list_2 = [float_5, corrected_command_0, str_0, list_1, bool_0]
        str_5 = '@fVM$P}]~fu'
        command_2 = module_0.Command(list_2, str_5)
        var_5 = corrected_command_0.__repr__()
        var_6 = rule_3.__repr__()
        str_6 = 't.6]#%"v7+9?'
        command_3 = module_0.Command(set_0, str_6)
        var_7 = corrected_command_0.run(corrected_command_0)
    except BaseException:
        pass