# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0
import json as module_1

def test_case_0():
    try:
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        list_0 = []
        ansible_j_s_o_n_decoder_1 = module_0.AnsibleJSONDecoder(*list_0)
        var_0 = ansible_j_s_o_n_decoder_1.object_hook(ansible_j_s_o_n_decoder_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        bytes_0 = b''
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(bytes_0)
        str_0 = '__ansible_vault'
        str_1 = '$ANSIBLE_VAULT;1.1;ABCDEF\nblablabla\nblablabla\nblablabla'
        str_2 = {str_0: str_1}
        var_1 = ansible_j_s_o_n_decoder_0.object_hook(str_2)
        tuple_0 = ()
        var_2 = module_1.loads(tuple_0)
    except BaseException:
        pass