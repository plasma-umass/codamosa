# Automatically generated by Pynguin.
import ansible.utils.version as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '0.0.3-alpha.1.0'
    semantic_version_0 = module_0.SemanticVersion(str_0)

def test_case_2():
    semantic_version_0 = module_0.SemanticVersion()
    str_0 = ' '
    alpha_0 = module_0._Alpha(str_0)
    bool_0 = False
    var_0 = alpha_0.__eq__(bool_0)
    var_1 = alpha_0.__ge__(str_0)
    var_2 = alpha_0.__repr__()

def test_case_3():
    str_0 = ''
    semantic_version_0 = module_0.SemanticVersion()
    alpha_0 = module_0._Alpha(semantic_version_0)
    var_0 = alpha_0.__ne__(str_0)

def test_case_4():
    semantic_version_0 = module_0.SemanticVersion()
    alpha_0 = module_0._Alpha(semantic_version_0)
    bool_0 = True
    var_0 = alpha_0.__eq__(bool_0)

def test_case_5():
    semantic_version_0 = module_0.SemanticVersion()
    alpha_0 = module_0._Alpha(semantic_version_0)
    int_0 = -459
    numeric_0 = module_0._Numeric(int_0)
    var_0 = numeric_0.__repr__()
    set_0 = None
    var_1 = numeric_0.__ne__(set_0)

def test_case_6():
    str_0 = 'q>/XA`&C_)KA^2%$C'
    set_0 = {str_0, str_0, str_0}
    float_0 = -3095.47
    numeric_0 = module_0._Numeric(float_0)
    var_0 = numeric_0.__ne__(set_0)
    bool_0 = False
    var_1 = numeric_0.__le__(bool_0)
    list_0 = None
    alpha_0 = module_0._Alpha(list_0)
    semantic_version_0 = module_0.SemanticVersion()
    var_2 = semantic_version_0.__repr__()

def test_case_7():
    semantic_version_0 = module_0.SemanticVersion()

def test_case_8():
    semantic_version_0 = module_0.SemanticVersion()
    var_0 = semantic_version_0.__le__(semantic_version_0)

def test_case_9():
    bool_0 = True
    alpha_0 = module_0._Alpha(bool_0)
    int_0 = 1919
    alpha_1 = module_0._Alpha(int_0)
    var_0 = alpha_1.__le__(alpha_0)

def test_case_10():
    int_0 = -1345
    numeric_0 = module_0._Numeric(int_0)
    var_0 = numeric_0.__repr__()
    float_0 = 1.2285802456324553
    numeric_1 = module_0._Numeric(float_0)
    bool_0 = False
    var_1 = numeric_1.__ne__(bool_0)
    semantic_version_0 = module_0.SemanticVersion()
    var_2 = semantic_version_0.__repr__()

def test_case_11():
    str_0 = '1.2.3-alpha.1'
    semantic_version_0 = module_0.SemanticVersion(str_0)
    var_0 = semantic_version_0.core
    semantic_version_1 = module_0.SemanticVersion(str_0)
    var_1 = semantic_version_1.prerelease
    str_1 = 'alpha'
    alpha_0 = module_0._Alpha(str_1)
    str_2 = '1'
    numeric_0 = module_0._Numeric(str_2)
    var_2 = semantic_version_1.buildmetadata
    str_3 = '1.2.3+build.1'
    semantic_version_2 = module_0.SemanticVersion(str_3)
    var_3 = semantic_version_2.core
    semantic_version_3 = module_0.SemanticVersion(str_3)
    var_4 = semantic_version_3.prerelease

def test_case_12():
    str_0 = '1.0.0'
    semantic_version_0 = module_0.SemanticVersion(str_0)
    str_1 = '0.0.3-alpha.1.0'
    semantic_version_1 = module_0.SemanticVersion(str_1)