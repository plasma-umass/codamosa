# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        float_0 = None
        list_0 = [float_0]
        tuple_0 = ()
        int_0 = 1173
        role_definition_0 = module_0.RoleDefinition(int_0)
        var_0 = role_definition_0.load(list_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.preprocess_data(role_definition_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_definition_0 = module_0.RoleDefinition()
        int_0 = 889
        var_0 = role_definition_0.preprocess_data(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_definition_0 = module_0.RoleDefinition()
        int_0 = 895
        var_0 = role_definition_0.get_name()
        dict_0 = {var_0: int_0, int_0: var_0}
        var_1 = role_definition_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xc1'
        set_0 = {bytes_0}
        list_0 = [bytes_0, bytes_0]
        role_definition_0 = module_0.RoleDefinition(bytes_0, set_0, list_0)
        bool_0 = True
        bytes_1 = b'\x98\x85\x10\xf7\xd0\x05'
        float_0 = -784.96109
        role_definition_1 = module_0.RoleDefinition(bool_0, bytes_1, float_0)
        str_0 = 'M%cJJjK'
        var_0 = role_definition_1.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'tests/unit/test_collections/ansible_collections/test_ns/test_coll/roles'
        role_definition_0 = module_0.RoleDefinition(str_0)
        var_0 = dict(role=str_0)
        var_1 = role_definition_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ke_A'
        set_0 = {str_0, str_0, str_0}
        role_definition_0 = module_0.RoleDefinition(str_0, set_0)
        var_0 = role_definition_0.get_role_params()
        str_1 = 'tests/unit/test_collections/ansible_collections/test_ns/test_coll/roles'
        role_definition_1 = module_0.RoleDefinition(str_1)
        var_1 = role_definition_1.get_name()
        var_2 = dict(role=role_definition_0)
        var_3 = role_definition_1.preprocess_data(var_2)
    except BaseException:
        pass

def test_case_7():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_role_params()
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject()
        var_1 = role_definition_0.get_role_params()
        var_2 = role_definition_0.preprocess_data(ansible_base_y_a_m_l_object_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'key_id'
        set_0 = {str_0, str_0, str_0}
        role_definition_0 = module_0.RoleDefinition(str_0, set_0)
        var_0 = role_definition_0.get_role_params()
        str_1 = 'tests/nit/test_collections/ansible_collections/test_ns/test_collroles'
        role_definition_1 = module_0.RoleDefinition(var_0, str_1, set_0)
        str_2 = 'test_role'
        var_1 = role_definition_1.get_name()
        var_2 = dict(role=str_2)
        var_3 = role_definition_1.preprocess_data(var_2)
    except BaseException:
        pass