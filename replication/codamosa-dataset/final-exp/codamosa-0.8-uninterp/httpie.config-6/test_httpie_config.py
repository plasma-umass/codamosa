# Automatically generated by Pynguin.
import httpie.config as module_0

def test_case_0():
    pass

def test_case_1():
    config_0 = module_0.Config()

def test_case_2():
    config_0 = module_0.Config()
    var_0 = config_0.save()

def test_case_3():
    config_0 = module_0.Config()
    var_0 = config_0.load()
    var_1 = config_0.save()

def test_case_4():
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.delete()

def test_case_5():
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.save(base_config_dict_0)