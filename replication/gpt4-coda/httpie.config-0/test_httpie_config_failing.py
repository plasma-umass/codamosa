# Automatically generated by Pynguin.
import httpie.config as module_0
import pathlib as module_1

def test_case_0():
    try:
        path_0 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_0.get_default_config_dir()
        var_0 = path_0.is_file()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_1 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_2():
    try:
        path_0 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.save()
    except BaseException:
        pass

def test_case_3():
    try:
        path_0 = module_1.Path()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.save(path_0)
        var_1 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_4():
    try:
        path_0 = None
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        config_file_error_0 = module_0.ConfigFileError()
        base_config_dict_1 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_1.save()
    except BaseException:
        pass

def test_case_5():
    try:
        path_0 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.delete()
        path_1 = module_1.Path()
        base_config_dict_1 = module_0.BaseConfigDict(path_1)
        var_1 = base_config_dict_1.save()
    except BaseException:
        pass

def test_case_6():
    try:
        path_0 = module_0.get_default_config_dir()
        path_1 = None
        base_config_dict_0 = module_0.BaseConfigDict(path_1)
        config_0 = module_0.Config()
        config_1 = module_0.Config()
        var_0 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_7():
    try:
        path_0 = module_0.get_default_config_dir()
        str_0 = 'z'
        list_0 = [path_0, str_0, str_0]
        path_1 = module_1.Path(*list_0)
        dict_0 = {str_0: str_0, str_0: str_0, str_0: path_1, str_0: list_0}
        path_2 = module_1.Path(**dict_0)
        base_config_dict_0 = module_0.BaseConfigDict(path_1)
        var_0 = base_config_dict_0.save()
    except BaseException:
        pass