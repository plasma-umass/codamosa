# Automatically generated by Pynguin.
import ansible.playbook.play as module_0

def test_case_0():
    pass

def test_case_1():
    play_0 = module_0.Play()

def test_case_2():
    play_0 = module_0.Play()
    var_0 = play_0.__repr__()

def test_case_3():
    dict_0 = {}
    play_0 = module_0.Play()
    var_0 = play_0.load(dict_0)

def test_case_4():
    play_0 = module_0.Play()
    var_0 = play_0.compile()

def test_case_5():
    play_0 = module_0.Play()
    var_0 = play_0.compile_roles_handlers()

def test_case_6():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars()

def test_case_7():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars_files()

def test_case_8():
    play_0 = module_0.Play()
    var_0 = play_0.serialize()
    play_1 = module_0.Play()
    var_1 = play_1.get_tasks()
    var_2 = play_1.get_handlers()
    var_3 = play_1.get_roles()

def test_case_9():
    play_0 = module_0.Play()
    var_0 = play_0.serialize()

def test_case_10():
    play_0 = module_0.Play()
    var_0 = play_0.get_tasks()

def test_case_11():
    play_0 = module_0.Play()
    var_0 = play_0.compile_roles_handlers()
    play_1 = module_0.Play()
    var_1 = play_1.get_tasks()
    var_2 = play_1.get_tasks()
    play_2 = module_0.Play()
    var_3 = play_2.copy()
    var_4 = play_1.get_name()

def test_case_12():
    play_0 = module_0.Play()
    str_0 = 'user'
    str_1 = {str_0: str_0}
    var_0 = play_0.preprocess_data(str_1)

def test_case_13():
    play_0 = module_0.Play()
    str_0 = 'roles'
    str_1 = 'name'
    str_2 = 'default_vars'
    str_3 = 'test_role'
    str_4 = 'a'
    str_5 = 'b'
    str_6 = {str_4: str_5}
    str_7 = {str_1: str_3, str_2: str_6}
    str_8 = 'test_role2'
    str_9 = {str_4: str_5}
    str_10 = {str_1: str_8, str_2: str_9}
    str_11 = [str_7, str_10]
    str_12 = {str_0: str_11}
    var_0 = play_0.deserialize(str_12)
    var_1 = play_0.roles
    int_0 = 0
    var_2 = play_0.roles[int_0]
    int_1 = 1
    var_3 = play_0.roles[int_1]

def test_case_14():
    str_0 = 'hosts'
    str_1 = 'user'
    str_2 = 'tasks'
    str_3 = 'all'
    str_4 = 'foo'
    str_5 = 'action'
    str_6 = 'module'
    str_7 = 'args'
    str_8 = 'shell'
    str_9 = 'echo 1'
    str_10 = 'bar'
    str_11 = {str_6: str_8, str_7: str_9, str_1: str_10}
    str_12 = {str_5: str_11}
    str_13 = [str_12]
    str_14 = {str_0: str_3, str_1: str_4, str_2: str_13}
    play_0 = module_0.Play()
    var_0 = play_0.load(str_14)