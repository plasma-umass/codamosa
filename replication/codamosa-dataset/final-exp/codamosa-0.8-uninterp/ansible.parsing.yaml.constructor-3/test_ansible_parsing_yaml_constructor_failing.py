# Automatically generated by Pynguin.
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1

def test_case_0():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        float_0 = 518.1454551699917
        var_0 = ansible_constructor_0.construct_mapping(float_0, ansible_constructor_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x95Y\xa1U\xae'
        ansible_constructor_0 = module_0.AnsibleConstructor()
        dict_0 = {ansible_constructor_0: ansible_constructor_0}
        ansible_constructor_1 = module_0.AnsibleConstructor(dict_0)
        var_0 = ansible_constructor_1.construct_yaml_str(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 535000
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_seq(int_0)
        ansible_constructor_1 = module_0.AnsibleConstructor()
        var_1 = ansible_constructor_1.construct_yaml_map(ansible_constructor_1)
        str_0 = 'N'
        var_2 = ansible_constructor_1.construct_vault_encrypted_unicode(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        str_0 = 'x691/8E(jo!0!e'
        var_0 = ansible_constructor_0.construct_yaml_unsafe(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -67
        ansible_constructor_0 = module_0.AnsibleConstructor(int_0)
        dict_0 = {int_0: int_0, ansible_constructor_0: ansible_constructor_0}
        mapping_node_0 = module_1.MappingNode(dict_0, int_0)
        var_0 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = None
        dict_0 = {}
        mapping_node_0 = module_1.MappingNode(tuple_0, dict_0, tuple_0, dict_0)
        set_0 = None
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_mapping(mapping_node_0, set_0)
    except BaseException:
        pass