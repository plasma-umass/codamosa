# Automatically generated by Pynguin.
import cookiecutter.repository as module_0

def test_case_0():
    try:
        list_0 = None
        var_0 = module_0.is_repo_url(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = {}
        str_0 = ''
        bool_0 = False
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, str_0, bool_0, str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        set_0 = {bool_0}
        var_0 = module_0.expand_abbreviations(bool_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        str_0 = 'List curently istalled templates.'
        bool_0 = None
        tuple_0 = (str_0, str_0, bool_0, dict_0)
        str_1 = '^L^YE1.LAGP\t\\]'
        float_0 = 640.3074
        str_2 = 'j"n`:Xjer*HFLQ\t+$'
        str_3 = '}a=$dj2yp\ti.zip'
        var_0 = module_0.determine_repo_dir(str_3, str_1, str_1, float_0, str_2, tuple_0, str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = {}
        str_0 = 'oI'
        bool_0 = False
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, str_0, bool_0, str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = {}
        str_0 = '.'
        bool_0 = False
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, str_0, bool_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'gh'
        str_1 = 'bb'
        str_2 = 'https://github.com/{}.git'
        str_3 = 'https://bitbucket.org/{}.git'
        str_4 = {str_0: str_2, str_1: str_3}
        str_5 = 'gh:audreyr/cookiecutter-pypackage'
        str_6 = '/some/dir'
        var_0 = None
        bool_0 = False
        var_1 = module_0.determine_repo_dir(str_5, str_4, str_6, var_0, bool_0)
    except BaseException:
        pass