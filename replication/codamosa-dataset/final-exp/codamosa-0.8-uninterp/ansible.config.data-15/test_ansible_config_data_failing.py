# Automatically generated by Pynguin.
import ansible.config.data as module_0

def test_case_0():
    try:
        str_0 = '\\X'
        set_0 = {str_0}
        dict_0 = {}
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(set_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        config_data_0 = module_0.ConfigData()
        str_0 = 'ANSIBLE_CALLBACK_PLUGINS'
        var_0 = config_data_0.get_setting(str_0)
        int_0 = -762
        var_1 = config_data_0.get_setting(int_0, config_data_0)
    except BaseException:
        pass

def test_case_3():
    try:
        config_data_0 = module_0.ConfigData()
        set_0 = {config_data_0, config_data_0, config_data_0}
        var_0 = config_data_0.get_settings(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        config_data_0 = module_0.ConfigData()
        dict_0 = {config_data_0: config_data_0}
        var_0 = config_data_0.update_setting(config_data_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'_'
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(bytes_0)
    except BaseException:
        pass