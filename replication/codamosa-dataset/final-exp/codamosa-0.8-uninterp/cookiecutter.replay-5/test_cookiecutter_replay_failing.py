# Automatically generated by Pynguin.
import cookiecutter.replay as module_0

def test_case_0():
    try:
        str_0 = 'cookiecuttertj%on'
        var_0 = module_0.load(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '"W'
        float_0 = None
        var_0 = module_0.dump(str_0, str_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'tests/test-load/'
        str_1 = 'test_load'
        str_2 = 'cookiecutter'
        str_3 = {str_2: str_1}
        var_0 = module_0.dump(str_0, str_1, str_3)
        var_1 = module_0.load(str_0, str_1)
        str_4 = '\n    Locate the repository directory from a template reference.\n\n    Applies repository abbreviations to the template reference.\n    If the template refers to a repository URL, clone it.\n    If the template is a path to a local repository, use it.\n\n    :param template: A directory containing a project template directory,\n        or a URL to a git repository.\n    :param abbreviations: A dictionary of repository abbreviation\n        definitions.\n    :param clone_to_dir: The directory to clone the repository into.\n    :param checkout: The branch, tag or commit ID to checkout after clone.\n    :param no_input: Prompt the user at command line for manual configuration?\n    :param password: The password to use when extracting the repository.\n    :param directory: Directory within repo where cookiecutter.json lives.\n    :return: A tuple containing the cookiecutter template directory, and\n        a boolean descriving whether that directory should be cleaned up\n        after the template has been instantiated.\n    :raises: `RepositoryNotFound` if a repository directory could not be found.\n    '
        float_0 = -344.24
        float_1 = 616.3
        var_2 = module_0.dump(str_4, float_0, float_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xef\xcdo\x86\x85\xf3\xc3'
        set_0 = None
        str_0 = 'z\\Re|\x0cEqi'
        var_0 = module_0.dump(bytes_0, set_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        var_0 = module_0.load(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'cookiecutter.json'
        var_0 = module_0.load(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'cookiecuttr'
        str_1 = {str_0: str_0}
        var_0 = module_0.dump(str_0, str_0, str_1)
    except BaseException:
        pass