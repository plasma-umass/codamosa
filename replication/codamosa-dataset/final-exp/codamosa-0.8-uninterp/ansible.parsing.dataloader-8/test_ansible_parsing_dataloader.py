# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0

def test_case_0():
    pass

def test_case_1():
    data_loader_0 = module_0.DataLoader()

def test_case_2():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.load_from_file(str_0, data_loader_0)

def test_case_3():
    list_0 = []
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_exists(list_0)

def test_case_4():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.get_real_file(str_0)

def test_case_5():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.get_real_file(str_0)
    var_1 = data_loader_0.find_vars_files(str_0, str_0)

def test_case_6():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.get_basedir()
    var_1 = data_loader_0.cleanup_all_tmp_files()

def test_case_7():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'Chomz/smeuser/playboHk/ro2es/some_role/taskI/main.yml'
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)

def test_case_8():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/home/someuser/playbooks/roles/some_role/tasks/main.yml'
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)

def test_case_9():
    bool_0 = False
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_tmp_file(bool_0)

def test_case_10():
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.cleanup_all_tmp_files()

def test_case_11():
    data_loader_0 = module_0.DataLoader()
    bytes_0 = b'\xc6\x8b\xfb\xef\xd1\xa7\xcf\xdfM/\x19%E\xec\xebX\x9b'
    data_loader_1 = module_0.DataLoader()
    var_0 = data_loader_1.is_file(bytes_0)

def test_case_12():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'Chomz/smeuser/playboHk/ro2es/some_role/taskI/main.yml'
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)
    str_1 = '] soBk(N7S\x0bG<D`ux0'
    var_1 = data_loader_0.find_vars_files(str_0, str_1)

def test_case_13():
    str_0 = 'EKFn$3C8@cc:j_,*'
    data_loader_0 = module_0.DataLoader()
    var_0 = data_loader_0.path_dwim(str_0)
    list_0 = []
    str_1 = 'sderr'
    str_2 = ''
    data_loader_1 = module_0.DataLoader()
    var_1 = data_loader_1.load(str_1, str_2)
    dict_0 = {str_1: str_1, str_2: list_0}
    data_loader_2 = module_0.DataLoader()
    set_0 = None
    int_0 = 2580
    var_2 = data_loader_1.path_dwim_relative_stack(dict_0, set_0, str_2, int_0)

def test_case_14():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    int_0 = -751
    dict_0 = {str_0: str_0}
    var_0 = data_loader_0.path_dwim_relative_stack(int_0, dict_0, str_0)
    data_loader_1 = module_0.DataLoader()
    var_1 = data_loader_0.cleanup_all_tmp_files()

def test_case_15():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/tmp'
    str_1 = 'yaml'
    str_2 = [str_1]
    bool_0 = True
    str_3 = '.yaml'
    var_0 = str_1 + str_3
    var_1 = data_loader_0.find_vars_files(str_0, str_1, str_2, bool_0)
    var_2 = len(var_1)

def test_case_16():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.get_real_file(str_0)
    bool_0 = False
    var_1 = data_loader_0.get_real_file(str_0, bool_0)

def test_case_17():
    data_loader_0 = module_0.DataLoader()
    str_0 = 'tasks'
    var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0)
    dict_0 = {str_0: str_0}
    var_1 = data_loader_0.path_dwim(dict_0)
    var_2 = data_loader_0.cleanup_all_tmp_files()

def test_case_18():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.get_real_file(str_0)
    float_0 = -101.43
    var_1 = data_loader_0.path_dwim_relative(str_0, var_0, float_0, str_0)

def test_case_19():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.get_real_file(str_0)
    var_1 = data_loader_0.path_exists(str_0)
    dict_0 = {var_1: str_0, var_1: data_loader_0}
    var_2 = data_loader_0.load_from_file(str_0, dict_0)
    bool_0 = False
    var_3 = data_loader_0.get_real_file(str_0, bool_0)
    int_0 = -773
    var_4 = data_loader_0.cleanup_tmp_file(bool_0)
    dict_1 = {var_1: var_0}
    var_5 = data_loader_0.path_dwim_relative_stack(int_0, dict_1, str_0)
    var_6 = data_loader_0.cleanup_tmp_file(data_loader_0)
    var_7 = data_loader_0.cleanup_all_tmp_files()
    str_1 = 'KLHq\r\t7EMWWEB'
    str_2 = '|^Lq=5Z'
    var_8 = data_loader_0.path_dwim_relative(str_1, str_2, bool_0)
    int_1 = 493
    var_9 = data_loader_0.load_from_file(str_0, int_1)

def test_case_20():
    data_loader_0 = module_0.DataLoader()
    str_0 = '/etc/passwd'
    var_0 = data_loader_0.get_real_file(str_0)
    var_1 = data_loader_0.path_exists(str_0)
    dict_0 = {var_1: str_0, var_1: data_loader_0}
    var_2 = data_loader_0.load_from_file(str_0, dict_0)
    bool_0 = False
    var_3 = data_loader_0.get_real_file(str_0, bool_0)
    int_0 = -773
    var_4 = data_loader_0.cleanup_tmp_file(bool_0)
    dict_1 = {var_1: var_0}
    var_5 = data_loader_0.path_dwim_relative_stack(int_0, dict_1, str_0)
    var_6 = data_loader_0.cleanup_all_tmp_files()
    str_1 = 'KLHq\r\t7EMWWEB'
    str_2 = 'HLp7V*56j<t'
    var_7 = data_loader_0.path_dwim_relative(str_1, str_2, bool_0)
    str_3 = '/etc/passwd'
    bytes_0 = b'c\xe36\xb5\x1f\xf9\xa1U/L\xe9\xc7P\xef\xb5F\xcb'
    int_1 = -3032
    var_8 = data_loader_0.load_from_file(str_3, bytes_0, int_1)