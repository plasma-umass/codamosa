# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    bool_0 = True
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(bool_0, bool_0)

def test_case_1():
    bool_0 = False
    float_0 = -6114.6
    str_0 = '2Mt,S'
    dict_0 = {str_0: str_0, str_0: bool_0, str_0: bool_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, float_0, dict_0)

def test_case_2():
    float_0 = -1635.37
    str_0 = '/ 6H-Zdc8_c'
    bool_0 = False
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, bool_0, str_0)
    bool_1 = False
    dict_0 = {str_0: bool_1, str_0: float_0, str_0: str_0}
    var_0 = ansible_j2_vars_0.add_locals(dict_0)

def test_case_3():
    bool_0 = False
    float_0 = -1072.0
    str_0 = '密碼'
    dict_0 = {str_0: str_0, str_0: bool_0, str_0: bool_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, float_0, dict_0)
    var_0 = ansible_j2_vars_0.__getitem__(str_0)