# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    pass

def test_case_1():
    version_0 = module_0.Version()

def test_case_2():
    str_0 = '2.7.2'
    strict_version_0 = module_0.StrictVersion(str_0)

def test_case_3():
    str_0 = '1.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 > strict_version_0

def test_case_4():
    str_0 = '2.7.2'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__str__()

def test_case_5():
    loose_version_0 = module_0.LooseVersion()

def test_case_6():
    str_0 = '8^M\x0bKR8Xk\\)'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_7():
    str_0 = '*/j,U|ND9a$HahcV)p\\'
    loose_version_0 = module_0.LooseVersion(str_0)
    var_0 = loose_version_0.__repr__()

def test_case_8():
    str_0 = "\\L0RR,J'E.Ey(\rFTY}MA"
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_9():
    str_0 = '27.2'
    str_1 = '*/j,U|ND9a$HahcV)p\\'
    loose_version_0 = module_0.LooseVersion(str_1)
    var_0 = loose_version_0.__repr__()
    strict_version_0 = module_0.StrictVersion(str_0)
    var_1 = strict_version_0.__str__()

def test_case_10():
    str_0 = '0.4'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__str__()
    str_1 = '0.4.0'
    strict_version_1 = module_0.StrictVersion(str_1)
    var_1 = strict_version_1.__str__()
    str_2 = '0.4.1'
    strict_version_2 = module_0.StrictVersion(str_2)
    var_2 = strict_version_2.__str__()
    str_3 = '0.5a1'
    strict_version_3 = module_0.StrictVersion(str_3)
    var_3 = strict_version_3.__str__()
    var_4 = strict_version_0.__str__()
    str_4 = '0.5'
    strict_version_4 = module_0.StrictVersion(str_4)
    var_5 = strict_version_4.__str__()
    str_5 = '0.9.6'
    strict_version_5 = module_0.StrictVersion(str_5)
    var_6 = strict_version_5.__str__()
    str_6 = '1.0'
    strict_version_6 = module_0.StrictVersion(str_6)
    var_7 = strict_version_6.__str__()

def test_case_11():
    str_0 = '1.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str_0 > strict_version_0

def test_case_12():
    str_0 = '1.0'
    str_1 = '1.0.0'
    loose_version_0 = module_0.LooseVersion()
    var_0 = loose_version_0.parse(str_1)
    var_1 = loose_version_0 > str_0

def test_case_13():
    str_0 = '10'
    str_1 = '1.0.0'
    loose_version_0 = module_0.LooseVersion()
    var_0 = loose_version_0.parse(str_1)
    var_1 = loose_version_0 > str_0
    str_2 = '5SdDXfEXIrdEh'
    var_2 = loose_version_0.parse(str_2)

def test_case_14():
    str_0 = '19.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    str_1 = '1.0.0'
    version_0 = module_0.Version()
    var_0 = strict_version_0.__str__()
    var_1 = str_1 > strict_version_0
    loose_version_0 = module_0.LooseVersion()
    loose_version_1 = module_0.LooseVersion()
    var_2 = loose_version_0.parse(str_1)
    var_3 = loose_version_0 > str_0
    loose_version_2 = module_0.LooseVersion()
    str_2 = '5SdDXfEXIrdEh'
    var_4 = loose_version_0.parse(str_2)