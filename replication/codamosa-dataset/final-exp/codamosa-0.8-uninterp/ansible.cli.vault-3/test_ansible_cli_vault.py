# Automatically generated by Pynguin.
import ansible.cli.vault as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Failed to remove service. rc: %s, out: %s, err: %s'
    vault_c_l_i_0 = module_0.VaultCLI(str_0)

def test_case_2():
    float_0 = 1.5
    list_0 = [float_0]
    str_0 = 'a'
    vault_c_l_i_0 = module_0.VaultCLI(str_0)
    var_0 = vault_c_l_i_0.init_parser()
    var_1 = vault_c_l_i_0.format_ciphertext_yaml(list_0)
    var_2 = vault_c_l_i_0.run()

def test_case_3():
    list_0 = None
    list_1 = [list_0, list_0, list_0]
    bool_0 = True
    vault_c_l_i_0 = module_0.VaultCLI(bool_0)
    var_0 = vault_c_l_i_0.format_ciphertext_yaml(list_1)