# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '2.1.1'
    int_0 = 1
    str_1 = 'alpha'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_2():
    str_0 = '2.0.0'
    int_0 = 1
    str_1 = 'beta'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_3():
    str_0 = '2.0.0'
    int_0 = -1
    str_1 = 'beta'
    str_2 = module_0.bump_version(str_0, int_0, str_1)
    str_3 = module_0.bump_version(str_2)

def test_case_4():
    str_0 = '2.0.0'
    str_1 = module_0.bump_version(str_0)

def test_case_5():
    str_0 = '2.1.1'
    int_0 = 1
    str_1 = module_0.bump_version(str_0, int_0)
    str_2 = 'alpha'
    str_3 = module_0.bump_version(str_1, int_0, str_2)

def test_case_6():
    str_0 = '2.0.0'
    str_1 = module_0.bump_version(str_0)
    int_0 = 1
    str_2 = module_0.bump_version(str_0, int_0)
    str_3 = 'alpha'
    str_4 = module_0.bump_version(str_0, int_0, str_3)
    str_5 = 'beta'
    str_6 = module_0.bump_version(str_0, int_0, str_5)
    int_1 = 0
    str_7 = module_0.bump_version(str_4, int_1)

def test_case_7():
    str_0 = '2.0.0'
    int_0 = -1
    str_1 = 'beta'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_8():
    str_0 = '2.0.0'
    str_1 = module_0.bump_version(str_0)
    int_0 = 1
    str_2 = 'alpha'
    str_3 = module_0.bump_version(str_0, int_0, str_2)
    str_4 = 'beta'
    str_5 = module_0.bump_version(str_0, int_0, str_4)
    str_6 = module_0.bump_version(str_5, int_0)

def test_case_9():
    str_0 = '2.1.1'
    int_0 = 1
    str_1 = module_0.bump_version(str_0, int_0)
    str_2 = 'alpha'
    str_3 = module_0.bump_version(str_1, int_0, str_2)
    str_4 = module_0.bump_version(str_3)

def test_case_10():
    str_0 = '2.0.0'
    str_1 = module_0.bump_version(str_0)
    str_2 = '2.1.1'
    int_0 = 1
    str_3 = module_0.bump_version(str_0, int_0)
    str_4 = 'alpha'
    str_5 = module_0.bump_version(str_0, int_0, str_4)
    str_6 = 'beta'
    str_7 = module_0.bump_version(str_2)
    str_8 = module_0.bump_version(str_5, int_0, str_6)

def test_case_11():
    str_0 = '2.0.0'
    str_1 = module_0.bump_version(str_0)
    int_0 = 2
    str_2 = 'alpha'
    str_3 = module_0.bump_version(str_0, int_0, str_2)
    str_4 = 'beta'
    str_5 = module_0.bump_version(str_0, int_0, str_4)

def test_case_12():
    str_0 = '2.1.1'
    str_1 = module_0.bump_version(str_0)
    str_2 = module_0.bump_version(str_1)
    int_0 = 2
    str_3 = module_0.bump_version(str_0, int_0)
    str_4 = 'alpha'
    str_5 = module_0.bump_version(str_1, int_0, str_4)
    str_6 = 'beta'
    str_7 = module_0.bump_version(str_5, int_0, str_6)

def test_case_13():
    str_0 = '2.1.1'
    int_0 = 1
    str_1 = module_0.bump_version(str_0, int_0)
    str_2 = 'alpha'
    str_3 = module_0.bump_version(str_1, int_0, str_2)
    str_4 = 'beta'
    str_5 = module_0.bump_version(str_0, int_0, str_4)
    str_6 = module_0.bump_version(str_5)
    str_7 = module_0.bump_version(str_5, int_0, str_4)

def test_case_14():
    str_0 = '2.0.0'
    int_0 = -1
    str_1 = 'beta'
    str_2 = module_0.bump_version(str_0, int_0, str_1)
    str_3 = module_0.bump_version(str_2, int_0, str_1)