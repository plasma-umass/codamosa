# Automatically generated by Pynguin.
import ansible.plugins.filter.encryption as module_0
import ansible.parsing.vault as module_1
import ansible.parsing.yaml.objects as module_2

def test_case_0():
    try:
        str_0 = 'my_secret'
        var_0 = module_0.do_vault(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        list_0 = [dict_0, bool_0]
        tuple_0 = (list_0,)
        bool_1 = None
        var_0 = module_0.do_vault(tuple_0, bool_1)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        bytes_0 = b'\r\xfd\xbd\x9c\xcfa\xdd\xfe\x13v\x1a\xe1N[\xb1\x8b*.\x8c'
        var_0 = module_0.do_vault(filter_module_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'C,b~h1'
        list_0 = [str_0, str_0]
        int_0 = -1635
        var_0 = module_0.do_unvault(int_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'C,b~h1'
        dict_0 = None
        list_0 = [dict_0, str_0]
        dict_1 = {str_0: str_0, str_0: str_0, dict_0: list_0}
        bytes_0 = b'5\x11\xad\xe3b4Brl\xf6\xeb\xfdl'
        var_0 = module_0.do_unvault(dict_1, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        str_0 = '$ANSIBLE_VAULT;1.2;AES256;ansible_default\n3463336330653934666533303338353835633461393362323762626238396166366564356333663b0a373662623161343963323162303861333930323636363066643533666434366638\n396466626235613337336435626465633930653633633262613965393464356264643330383964653534643034656433393461396162373262393530313938313433666538666363656430\n'
        var_1 = module_0.do_unvault(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '$ANSIBLE_VAULT;1.2;AES256;ansible_default\n3463336330653934666533303338353835633461393362323762626238396166366564356333663b0a373662623161343963323162303861333930323636363066643533666434366638\n396466626235613337336435626465633930653633633262613965393464356264643330383964653534643034656433393461396162373262393530313938313433666538666363656430\n'
        var_0 = module_0.do_unvault(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\xad\x9cc\xc8\xdau'
        vault_secret_0 = module_1.VaultSecret()
        ansible_vault_encrypted_unicode_0 = module_2.AnsibleVaultEncryptedUnicode(vault_secret_0)
        list_0 = [ansible_vault_encrypted_unicode_0]
        var_0 = module_0.do_unvault(ansible_vault_encrypted_unicode_0, bytes_0, list_0)
    except BaseException:
        pass