# Automatically generated by Pynguin.
import ansible.parsing.yaml.dumper as module_0
import ansible.parsing.yaml.objects as module_1
import yaml as module_2
import ansible.vars.hostvars as module_3
import ansible.template as module_4
import ansible.utils.unsafe_proxy as module_5

def test_case_0():
    try:
        bool_0 = False
        ansible_dumper_0 = module_0.AnsibleDumper(bool_0)
        bytes_0 = b'AES256$p4$4$7IwWmZWTk7BjK2S0rxEgIw==$GTc0YTQ3ODUzZjU3ZjU1MGM0MGZkNzNhNDkwZmMzYzY='
        ansible_vault_encrypted_unicode_0 = module_1.AnsibleVaultEncryptedUnicode(bytes_0)
        var_0 = ansible_dumper_0.represent_data(ansible_vault_encrypted_unicode_0)
        var_1 = module_2.load(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        ansible_dumper_0 = module_0.AnsibleDumper(bool_0)
        str_0 = 'oZX_4wT;;\n)H<&7'
        int_0 = None
        host_vars_vars_0 = module_3.HostVarsVars(str_0, int_0)
        var_0 = ansible_dumper_0.represent_data(host_vars_vars_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        ansible_dumper_0 = module_0.AnsibleDumper(bool_0)
        int_0 = 512
        ansible_undefined_0 = module_4.AnsibleUndefined()
        ansible_unsafe_text_0 = module_5.AnsibleUnsafeText()
        int_1 = 927
        str_0 = 'ansible.plugins.terminal'
        dict_0 = {str_0: ansible_undefined_0, str_0: ansible_dumper_0, str_0: ansible_dumper_0, str_0: str_0}
        tuple_0 = (ansible_undefined_0, ansible_unsafe_text_0, int_1, dict_0)
        ansible_undefined_1 = module_4.AnsibleUndefined(tuple_0)
        async_iterator_0 = ansible_undefined_1.__aiter__()
        int_2 = 23
        host_vars_vars_0 = module_3.HostVarsVars(async_iterator_0, int_2)
        ansible_unicode_0 = module_1.AnsibleUnicode()
        var_0 = ansible_dumper_0.represent_data(ansible_unicode_0)
        list_0 = [ansible_dumper_0, int_0, ansible_unsafe_text_0]
        ansible_sequence_0 = module_1.AnsibleSequence(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        ansible_dumper_0 = module_0.AnsibleDumper(bool_0)
        bytes_0 = b'AES256$p4$4$7IwWmZWTk7BjK2S0rxEgIw==$GTc0YTQ3ODUzZjU3ZjU1MGM0MGZkNzNhNDkwZmMzYzY='
        int_0 = 512
        str_0 = 'oZX_4wT;;\n)H<&7'
        dict_0 = {ansible_dumper_0: int_0, bytes_0: bool_0, str_0: bytes_0}
        int_1 = 520
        host_vars_vars_0 = module_3.HostVarsVars(dict_0, int_1)
        dict_1 = {}
        ansible_unsafe_bytes_0 = module_5.AnsibleUnsafeBytes(**dict_1)
        var_0 = ansible_dumper_0.represent_data(ansible_unsafe_bytes_0)
        bytes_1 = b''
        var_1 = module_0.represent_undefined(bytes_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        ansible_dumper_0 = module_0.AnsibleDumper(bool_0)
        str_0 = 'oZX_4wT;;\n)H<&7'
        ansible_undefined_0 = module_4.AnsibleUndefined(str_0)
        var_0 = ansible_dumper_0.represent_data(ansible_undefined_0)
    except BaseException:
        pass