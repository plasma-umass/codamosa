# Automatically generated by Pynguin.
import ansible.playbook.play_context as module_0

def test_case_0():
    pass

def test_case_1():
    play_context_0 = module_0.PlayContext()

def test_case_2():
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.set_attributes_from_cli()

def test_case_3():
    int_0 = 1203
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.set_become_plugin(int_0)

def test_case_4():
    str_0 = "p$()t3VX(b'^&@\r/#paD"
    dict_0 = {str_0: str_0}
    play_context_0 = module_0.PlayContext()
    var_0 = play_context_0.update_vars(dict_0)