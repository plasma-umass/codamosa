# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    try:
        float_0 = 0.1
        vars_module_0 = module_0.VarsModule()
        var_0 = vars_module_0.get_vars(float_0, float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        vars_module_0 = module_0.VarsModule()
        str_0 = 'hoIt1'
        host_0 = module_1.Host(str_0)
        str_1 = 'host2'
        host_1 = module_1.Host(str_1)
        str_2 = 'host3'
        set_0 = {vars_module_0}
        bool_0 = False
        bytes_0 = None
        var_0 = vars_module_0.get_vars(set_0, bool_0, host_1, bytes_0)
        host_2 = module_1.Host(str_2)
        var_1 = host_2.__repr__()
        str_3 = 'group1'
        group_0 = module_2.Group(str_3)
        str_4 = 'group2'
        str_5 = 'group3'
        group_1 = module_2.Group(str_5)
        var_2 = [host_0, host_1, host_2, group_0, group_1, group_1]
        str_6 = None
        str_7 = 'qm:?D9Xy{Ob.tTK*M'
        dict_0 = {str_1: str_4, str_6: group_1, str_6: host_1, str_7: var_2}
        str_8 = 'v\x0blp'
        var_3 = vars_module_0.get_vars(dict_0, str_8, str_5)
    except BaseException:
        pass