# Automatically generated by Pynguin.
import ansible.playbook.play as module_0

def test_case_0():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.load(play_0)
    except BaseException:
        pass

def test_case_1():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.load_data(play_0)
    except BaseException:
        pass

def test_case_2():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.get_vars()
        play_1 = module_0.Play()
        bool_0 = True
        var_1 = play_0.load(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'VZ\t5|\x0c]D%='
        play_0 = module_0.Play()
        var_0 = play_0.deserialize(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        play_0 = module_0.Play()
        var_0 = play_0.serialize()
        play_1 = module_0.Play()
        var_1 = play_1.get_roles()
        str_0 = "@($6'iY-s"
        var_2 = play_1.get_name()
        float_0 = -1207.505
        var_3 = play_1.get_tasks()
        set_0 = {float_0, str_0, play_1}
        float_1 = 1671.0
        var_4 = play_0.copy()
        var_5 = play_1.load(str_0, float_0, set_0, float_1)
    except BaseException:
        pass