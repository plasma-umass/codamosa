# Automatically generated by Pynguin.
import ansible.playbook.play as module_0
import ansible.playbook.role as module_1

def test_case_0():
    pass

def test_case_1():
    play_0 = module_0.Play()

def test_case_2():
    play_0 = module_0.Play()
    var_0 = play_0.__repr__()

def test_case_3():
    play_0 = module_0.Play()
    var_0 = play_0.compile()

def test_case_4():
    play_0 = module_0.Play()
    var_0 = play_0.compile_roles_handlers()

def test_case_5():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars()

def test_case_6():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars_files()

def test_case_7():
    play_0 = module_0.Play()
    var_0 = play_0.get_handlers()
    play_1 = module_0.Play()
    var_1 = play_1.get_handlers()

def test_case_8():
    play_0 = module_0.Play()
    var_0 = play_0.serialize()

def test_case_9():
    play_0 = module_0.Play()
    var_0 = play_0.get_tasks()

def test_case_10():
    var_0 = {}
    play_0 = module_0.Play()
    var_1 = play_0.deserialize(var_0)

def test_case_11():
    play_0 = module_0.Play()
    var_0 = play_0.get_vars()
    var_1 = play_0.copy()
    play_1 = module_0.Play()
    play_2 = module_0.Play()
    var_2 = play_0.compile_roles_handlers()

def test_case_12():
    play_0 = module_0.Play()
    str_0 = 'user'
    str_1 = {str_0: str_0}
    var_0 = play_0.preprocess_data(str_1)

def test_case_13():
    play_0 = module_0.Play()
    var_0 = play_0.serialize()
    play_1 = module_0.Play()
    str_0 = 'uer'
    str_1 = 'root'
    str_2 = {str_0: str_1}
    var_1 = play_1.preprocess_data(str_2)

def test_case_14():
    play_0 = module_0.Play()
    str_0 = 'name'
    str_1 = 'hosts'
    str_2 = 'test-play'
    str_3 = 'test-hosts'
    str_4 = {str_0: str_2, str_1: str_3}
    var_0 = play_0.load_data(str_4)

def test_case_15():
    str_0 = 'name'
    str_1 = 'roles'
    str_2 = 'vars'
    str_3 = 'testPlay'
    var_0 = []
    str_4 = 'key'
    str_5 = 'value'
    str_6 = {str_4: str_5}
    var_1 = {str_0: str_3, str_1: var_0, str_2: str_6}
    play_0 = module_0.Play()
    var_2 = play_0.deserialize(var_1)
    var_3 = None
    str_7 = {str_4: str_5}
    str_8 = {var_3: str_3, str_2: str_7}
    play_1 = module_0.Play()
    var_4 = play_1.deserialize(str_8)

def test_case_16():
    play_0 = module_0.Play()
    role_0 = module_1.Role()
    str_0 = 'role_name'
    str_1 = 'role_path'
    str_2 = 'role1'
    str_3 = '/foo/bar'
    str_4 = {str_0: str_2, str_1: str_3}
    var_0 = role_0.deserialize(str_4)
    str_5 = 'hosts'
    str_6 = 'roles'
    str_7 = 'name'
    str_8 = 'connection'
    str_9 = 'host1'
    var_1 = role_0.serialize()
    var_2 = [var_1]
    str_10 = 'local'
    var_3 = {str_5: str_9, str_6: var_2, str_7: str_2, str_8: str_10}
    var_4 = play_0.deserialize(var_3)
    var_5 = play_0.roles
    var_6 = len(var_5)

def test_case_17():
    play_0 = module_0.Play()
    str_0 = 'hosts'
    str_1 = 'test-play'
    str_2 = 'test-hosts'
    str_3 = {str_0: str_1, str_0: str_2}
    var_0 = play_0.get_roles()
    var_1 = play_0.load_data(str_3)
    var_2 = play_0.get_name()
    var_3 = play_0.get_tasks()