# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    pass

def test_case_1():
    version_0 = module_0.Version()

def test_case_2():
    str_0 = '1.0a81'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == str_0

def test_case_3():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 <= strict_version_0

def test_case_4():
    str_0 = '1.0a2'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == strict_version_0
    var_1 = strict_version_0.__str__()
    loose_version_0 = module_0.LooseVersion()
    var_2 = loose_version_0.parse(str_0)

def test_case_5():
    str_0 = '4"C"{uNRMg'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_6():
    str_0 = '1.0a1'
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__str__()
    var_1 = strict_version_0 == var_0
    loose_version_0 = module_0.LooseVersion(str_0)
    var_2 = loose_version_0.__repr__()

def test_case_7():
    str_0 = '1.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    str_1 = '1.0a2'
    strict_version_1 = module_0.StrictVersion(str_1)
    var_0 = strict_version_0 == strict_version_1

def test_case_8():
    str_0 = '1.0a1'
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == strict_version_1
    str_1 = '1.0a2'
    strict_version_2 = module_0.StrictVersion(str_1)
    var_1 = strict_version_0 == strict_version_2

def test_case_9():
    str_0 = '1.0a81'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == strict_version_0

def test_case_10():
    str_0 = '1.0a1'
    strict_version_0 = module_0.StrictVersion(str_0)
    str_1 = '1.0'
    strict_version_1 = module_0.StrictVersion(str_1)
    var_0 = strict_version_0 == strict_version_1
    var_1 = strict_version_0 == strict_version_1

def test_case_11():
    str_0 = '1.01'
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    str_1 = '1.0a2'
    strict_version_2 = module_0.StrictVersion(str_1)
    version_0 = module_0.Version()
    var_0 = strict_version_0 == strict_version_2
    version_1 = module_0.Version()
    version_2 = module_0.Version()
    var_1 = strict_version_1.__str__()
    str_2 = 'Y[%M^h\r_#\tH F'
    loose_version_0 = module_0.LooseVersion(str_2)
    strict_version_3 = module_0.StrictVersion()
    str_3 = "haz(+Ct'#zZW"
    var_2 = loose_version_0.parse(str_3)

def test_case_12():
    str_0 = '1.0a1'
    str_1 = '1.0a2'
    strict_version_0 = module_0.StrictVersion(str_1)
    var_0 = str_0 == strict_version_0
    loose_version_0 = module_0.LooseVersion()
    var_1 = loose_version_0.parse(str_0)