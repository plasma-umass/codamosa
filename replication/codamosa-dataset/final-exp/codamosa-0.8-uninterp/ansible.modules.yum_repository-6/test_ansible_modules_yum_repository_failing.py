# Automatically generated by Pynguin.
import ansible.modules.yum_repository as module_0

def test_case_0():
    try:
        int_0 = 519
        yum_repo_0 = module_0.YumRepo(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ModuleTest'
        var_0 = ()
        str_1 = 'params'
        str_2 = 'repoid'
        str_3 = [str_2]
        str_4 = {str_2: str_3}
        str_5 = {str_1: str_4}
        var_1 = type(str_0, var_0, str_5)
        yum_repo_0 = module_0.YumRepo(var_1)
    except BaseException:
        pass