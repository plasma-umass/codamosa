# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()

def test_case_2():
    str_0 = '__ansible_vault'
    str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_1)

def test_case_3():
    str_0 = '^R>i8AA'
    str_1 = '[p`G}'
    dict_0 = {str_0: str_0, str_1: str_0, str_1: str_0, str_0: str_0}
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)