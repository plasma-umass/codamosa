# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.block as module_1
import ansible.playbook.role as module_2

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    include_role_0 = module_0.IncludeRole(bool_0)

def test_case_2():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.get_name()

def test_case_3():
    int_0 = -3939
    tuple_0 = (int_0,)
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.copy()
    set_0 = {int_0, tuple_0, int_0, tuple_0}
    list_0 = [tuple_0, set_0, int_0]
    include_role_1 = module_0.IncludeRole(list_0, int_0)
    include_role_2 = module_0.IncludeRole()
    var_1 = include_role_2.get_include_params()
    var_2 = include_role_1.get_name()

def test_case_4():
    bool_0 = False
    include_role_0 = module_0.IncludeRole(bool_0)
    var_0 = include_role_0.get_include_params()

def test_case_5():
    block_0 = module_1.Block()
    role_0 = module_2.Role()
    include_role_0 = module_0.IncludeRole(block_0, role_0)
    var_0 = block_0.get_include_params()
    var_1 = include_role_0.get_name()
    role_1 = module_2.Role(include_role_0)
    var_2 = include_role_0.get_include_params()