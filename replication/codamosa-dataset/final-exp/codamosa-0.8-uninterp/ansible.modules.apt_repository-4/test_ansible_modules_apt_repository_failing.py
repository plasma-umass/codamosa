# Automatically generated by Pynguin.
import ansible.modules.apt_repository as module_0

def test_case_0():
    try:
        list_0 = []
        float_0 = 0.5
        var_0 = module_0.install_python_apt(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'H'
        sources_list_0 = module_0.SourcesList(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'failed to parse body as form_urlencoded: %s'
        str_1 = '-JS:'
        list_0 = [str_1]
        str_2 = '6b5<'
        dict_0 = {str_1: str_0, str_0: list_0, str_0: list_0, str_2: str_0}
        ubuntu_sources_list_0 = module_0.UbuntuSourcesList(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = None
        var_0 = module_0.get_add_ppa_signing_key_callback(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        invalid_source_0 = module_0.InvalidSource()
        str_0 = '9Hp'
        float_0 = -1184.1
        list_0 = []
        var_0 = module_0.revert_sources_list(float_0, str_0, list_0)
    except BaseException:
        pass