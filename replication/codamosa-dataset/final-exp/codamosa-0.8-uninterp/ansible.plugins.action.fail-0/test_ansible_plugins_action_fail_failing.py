# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        dict_0 = {}
        str_0 = '\'refW!Df#Q!Z>("k ]l*'
        str_1 = '\r6n(HQ\\@Gt<<x'
        bytes_0 = b'\x01'
        list_0 = []
        action_module_0 = module_0.ActionModule(dict_0, dict_0, str_0, str_1, bytes_0, list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 4596
        dict_0 = {int_0: int_0}
        str_0 = '^*Ln\n\r,2bNc#6|Ue\x0c'
        list_0 = [int_0, dict_0]
        bytes_0 = b'\xbeo'
        bytes_1 = b"\xa4\xd4t\xbd\n\xe6'\xado\xc9\xea\t:G "
        str_1 = ''
        bool_0 = False
        bytes_2 = b'\x18R\xb0\x8a\x08&\x06\xce\xb0V\x9b\xbc\x7f\x94\xe2\x0f'
        float_0 = -204.006
        action_module_0 = module_0.ActionModule(dict_0, str_1, bool_0, dict_0, bytes_2, float_0)
        set_0 = {bool_0, bytes_0, int_0, bytes_1}
        bytes_3 = b'\xfeL\xf8\x02\x01\xd2.*%U\xbb\xa1\xe03R\xcc\x8cR"'
        action_module_1 = module_0.ActionModule(bytes_0, bytes_1, action_module_0, set_0, dict_0, bytes_3)
        var_0 = action_module_1.run(str_0, list_0)
    except BaseException:
        pass