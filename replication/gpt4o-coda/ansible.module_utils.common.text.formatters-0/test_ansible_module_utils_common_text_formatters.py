# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    bytes_0 = b'\xb03>\x05U4\x91\x12'
    var_0 = module_0.lenient_lowercase(bytes_0)

def test_case_1():
    int_0 = 1007
    var_0 = module_0.human_to_bytes(int_0)

def test_case_2():
    str_0 = '10K'
    var_0 = module_0.human_to_bytes(str_0)

def test_case_3():
    int_0 = 1024
    var_0 = module_0.bytes_to_human(int_0)

def test_case_4():
    int_0 = 995
    var_0 = module_0.bytes_to_human(int_0)

def test_case_5():
    int_0 = -197
    var_0 = module_0.bytes_to_human(int_0)