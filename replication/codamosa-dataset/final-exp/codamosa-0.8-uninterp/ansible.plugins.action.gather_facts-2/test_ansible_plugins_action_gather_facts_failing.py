# Automatically generated by Pynguin.
import ansible.plugins.action.gather_facts as module_0

def test_case_0():
    try:
        str_0 = '\r3'
        str_1 = 'a,0C'
        str_2 = '>?/Z'
        str_3 = 'RznV~<\tzS,)'
        bool_0 = None
        dict_0 = {str_2: str_2, str_2: str_2, str_0: bool_0}
        str_4 = 'r'
        action_module_0 = module_0.ActionModule(str_2, str_3, dict_0, str_0, str_4, dict_0)
        var_0 = action_module_0.run(str_1)
    except BaseException:
        pass