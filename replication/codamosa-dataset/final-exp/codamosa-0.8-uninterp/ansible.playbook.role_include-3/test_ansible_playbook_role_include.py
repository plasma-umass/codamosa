# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.block as module_1

def test_case_0():
    pass

def test_case_1():
    include_role_0 = module_0.IncludeRole()

def test_case_2():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.get_name()

def test_case_3():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.copy()
    var_1 = include_role_0.copy()
    var_2 = include_role_0.get_include_params()
    list_0 = []
    include_role_1 = module_0.IncludeRole(list_0)

def test_case_4():
    str_0 = 'include_role'
    var_0 = dict(name=str_0)
    var_1 = dict(module=str_0, args=var_0)
    var_2 = dict(action=var_1)
    block_0 = module_1.Block(var_0, var_2)
    include_role_0 = module_0.IncludeRole(block_0, str_0)
    var_3 = include_role_0.load(var_2, block_0, include_role_0)