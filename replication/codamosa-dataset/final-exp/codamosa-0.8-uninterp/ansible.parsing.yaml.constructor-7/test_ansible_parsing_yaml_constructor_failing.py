# Automatically generated by Pynguin.
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1

def test_case_0():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_mapping(ansible_constructor_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc0\xeax\xd3<\x06\xed\x93E]\xc4\xc7%\x890>G\r'
        ansible_constructor_0 = module_0.AnsibleConstructor(bytes_0)
        float_0 = 2052.04
        set_0 = {float_0, float_0, float_0, float_0}
        ansible_constructor_1 = module_0.AnsibleConstructor(set_0)
        var_0 = ansible_constructor_1.construct_yaml_str(ansible_constructor_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_vault_encrypted_unicode(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 3223.855
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_unsafe(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        int_0 = 345
        bool_0 = True
        str_0 = 'File does not exist, used empty file: %s'
        ansible_constructor_1 = module_0.AnsibleConstructor()
        ansible_constructor_2 = module_0.AnsibleConstructor(bool_0, ansible_constructor_1)
        var_0 = ansible_constructor_2.construct_yaml_map(str_0)
        ansible_constructor_3 = module_0.AnsibleConstructor(int_0, bool_0)
        var_1 = ansible_constructor_3.construct_yaml_map(ansible_constructor_0)
        ansible_constructor_4 = module_0.AnsibleConstructor()
        var_2 = ansible_constructor_4.construct_yaml_str(ansible_constructor_3)
    except BaseException:
        pass

def test_case_5():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        int_0 = 3335
        bool_0 = True
        str_0 = 'JOT~'
        mapping_node_0 = module_1.MappingNode(int_0, bool_0, str_0)
        var_0 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/tmp/test'
        ansible_constructor_0 = module_0.AnsibleConstructor(str_0)
        str_1 = '1'
        bytes_0 = b''
        dict_0 = {str_1: bytes_0}
        list_0 = [str_1]
        mapping_node_0 = module_1.MappingNode(ansible_constructor_0, bytes_0, dict_0, list_0)
        tuple_0 = ()
        var_0 = ansible_constructor_0.construct_mapping(mapping_node_0, tuple_0)
    except BaseException:
        pass