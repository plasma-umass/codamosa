# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0

def test_case_0():
    pass

def test_case_1():
    role_definition_0 = module_0.RoleDefinition()

def test_case_2():
    str_0 = 'Could not detect a supported package manager from the following list: %s, or the required Python library is not installed. Check warnings for details.'
    list_0 = []
    tuple_0 = ()
    role_definition_0 = module_0.RoleDefinition(str_0, list_0, tuple_0)
    var_0 = role_definition_0.get_role_params()

def test_case_3():
    dict_0 = {}
    int_0 = 745
    role_definition_0 = module_0.RoleDefinition(dict_0, int_0)
    var_0 = role_definition_0.get_role_path()

def test_case_4():
    role_definition_0 = module_0.RoleDefinition()
    var_0 = role_definition_0.get_name(role_definition_0)