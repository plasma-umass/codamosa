# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0
import ansible.parsing.vault as module_1
import ansible.utils.display as module_2

def test_case_0():
    try:
        tuple_0 = ()
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.set_basedir(tuple_0)
        bool_0 = True
        var_1 = data_loader_0.set_vault_secrets(bool_0)
        var_2 = data_loader_0.get_basedir()
        data_loader_1 = module_0.DataLoader()
        set_0 = {tuple_0, tuple_0, data_loader_0, data_loader_1}
        var_3 = data_loader_0.set_vault_secrets(set_0)
        list_0 = [var_0]
        var_4 = data_loader_0.load(list_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = './test/loader_tests/test_load_from_file.yml'
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = ''
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'XV4P\x0bB2['
        tuple_0 = ()
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\r$K'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.is_executable(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 811.013119
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'XV4P\x0bB2['
        tuple_0 = ()
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '`dQx/Fo]*\x0b\\)'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_basedir()
        var_1 = data_loader_0.get_basedir()
        str_0 = '\x0b#;^slm'
        var_2 = data_loader_0.is_file(str_0)
        bool_0 = True
        var_3 = data_loader_0.get_real_file(bool_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        data_loader_0 = module_0.DataLoader()
        bytes_0 = b'0\xa6\xf4\x10\xcf\x900\xe2N3'
        str_0 = '_o'
        var_0 = data_loader_0.path_dwim_relative_stack(bytes_0, data_loader_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        int_0 = 2322
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(list_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        data_loader_0 = module_0.DataLoader()
        list_0 = [data_loader_0, data_loader_0]
        var_0 = data_loader_0.is_directory(list_0)
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.cleanup_all_tmp_files()
        str_0 = 'XV4P\x0bB2['
        tuple_0 = ()
        var_2 = data_loader_0.path_dwim_relative_stack(str_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = True
        data_loader_0 = module_0.DataLoader()
        data_loader_1 = module_0.DataLoader()
        var_0 = data_loader_1.list_directory(bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        data_loader_0 = module_0.DataLoader()
        tuple_0 = ()
        list_0 = None
        list_1 = None
        set_0 = set()
        var_0 = data_loader_0.path_dwim_relative_stack(tuple_0, list_0, list_1, set_0)
    except BaseException:
        pass

def test_case_14():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_all_tmp_files()
        var_1 = data_loader_0.set_basedir(var_0)
        data_loader_1 = module_0.DataLoader()
        data_loader_2 = module_0.DataLoader()
        float_0 = -2143.5233
        tuple_0 = (float_0,)
        var_2 = data_loader_1.cleanup_all_tmp_files()
        data_loader_3 = None
        var_3 = data_loader_2.cleanup_tmp_file(data_loader_3)
        var_4 = data_loader_1.load_from_file(tuple_0)
    except BaseException:
        pass

def test_case_15():
    try:
        data_loader_0 = module_0.DataLoader()
        int_0 = -1175
        dict_0 = {data_loader_0: data_loader_0, data_loader_0: data_loader_0, data_loader_0: int_0, data_loader_0: int_0}
        bool_0 = False
        set_0 = set()
        var_0 = data_loader_0.set_vault_secrets(set_0)
        float_0 = 733.0
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.load_from_file(dict_0, bool_0, float_0)
    except BaseException:
        pass

def test_case_16():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '\nl/,p\\A\x0by+\taf+\x0c'
        tuple_0 = ()
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, str_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '/home/localadmin/backup/my.yml'
        bool_0 = True
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)
        data_loader_1 = module_0.DataLoader()
        complex_0 = None
        set_0 = {bool_0, data_loader_1}
        float_0 = 110.296904
        data_loader_2 = module_0.DataLoader()
        var_1 = data_loader_2.path_dwim_relative(complex_0, set_0, float_0)
    except BaseException:
        pass

def test_case_18():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'tasks'
        bool_0 = False
        var_0 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)
        data_loader_1 = module_0.DataLoader()
        var_1 = data_loader_1.load_from_file(data_loader_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '/home/localadmin/backup/my.yml'
        bool_0 = True
        data_loader_0 = module_0.DataLoader()
        str_1 = 'Dup@<$V@S7u'
        var_0 = data_loader_0.path_dwim_relative_stack(str_1, bool_0, str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        tuple_0 = ()
        str_0 = ''
        float_0 = 2019.5596
        set_0 = set()
        bytes_0 = b'\xe9+b}\xc2\xdc\xb52k\xf3\xe5\xf5XF\xda\xc8\x86'
        data_loader_0 = module_0.DataLoader()
        list_0 = [data_loader_0, bytes_0]
        var_0 = data_loader_0.path_dwim_relative_stack(str_0, float_0, str_0, list_0)
        vault_lib_0 = module_1.VaultLib()
        var_1 = data_loader_0.cleanup_tmp_file(str_0)
        bytes_1 = b'@\x80'
        var_2 = data_loader_0.path_dwim_relative_stack(set_0, bytes_1, tuple_0)
    except BaseException:
        pass

def test_case_21():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = '/{ome/,ocaladmin/backup/my.yml'
        float_0 = 1012.7412680745284
        var_0 = data_loader_0.set_basedir(float_0)
        str_1 = 'my.yml'
        bytes_0 = b'\xfc\xe9\xd8?\x8ab\xe2J\xa6h\x8e \xf4A\x8dY,'
        str_2 = '$|0{@dvX8W1LZ'
        tuple_0 = (data_loader_0, str_2)
        int_0 = 2269
        var_1 = data_loader_0.set_vault_secrets(int_0)
        var_2 = data_loader_0.is_file(tuple_0)
        var_3 = data_loader_0.path_dwim(str_2)
        var_4 = data_loader_0.cleanup_tmp_file(data_loader_0)
        bool_0 = True
        var_5 = data_loader_0.path_dwim_relative(str_0, str_1, str_1, bool_0)
        data_loader_1 = module_0.DataLoader()
        float_1 = -1911.674994
        bytes_1 = b'\xdb\xc8\xe9m\x0b\x98\xdd\x17\x1b\xdb\xe7\xc0\xee\x1b\xc1\xa6'
        list_0 = [bytes_0, bytes_1, float_1]
        data_loader_2 = module_0.DataLoader()
        var_6 = data_loader_2.find_vars_files(bytes_1, bytes_0, list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.cleanup_all_tmp_files()
        float_0 = 1012.8
        var_1 = data_loader_0.set_basedir(float_0)
        str_0 = 'tasks'
        bytes_0 = b'\xfc\xe9\xd8?\x8ab\xe2J\xa6h\x8e \xf4A\x8dY,'
        int_0 = 2269
        var_2 = data_loader_0.set_vault_secrets(int_0)
        var_3 = data_loader_0.path_dwim(str_0)
        var_4 = data_loader_0.cleanup_tmp_file(data_loader_0)
        bool_0 = True
        var_5 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)
        set_0 = {var_5}
        data_loader_1 = module_0.DataLoader()
        var_6 = data_loader_1.path_dwim_relative_stack(set_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '.'
        data_loader_0 = module_0.DataLoader()
        var_0 = data_loader_0.get_real_file(str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        data_loader_0 = module_0.DataLoader()
        int_0 = None
        tuple_0 = ()
        var_0 = data_loader_0.get_basedir()
        var_1 = data_loader_0.cleanup_tmp_file(tuple_0)
        str_0 = ''
        var_2 = data_loader_0.find_vars_files(str_0, str_0)
        var_3 = data_loader_0.cleanup_all_tmp_files()
        var_4 = data_loader_0.get_basedir()
        var_5 = data_loader_0.set_basedir(tuple_0)
        tuple_1 = (data_loader_0, str_0)
        var_6 = data_loader_0.set_vault_secrets(int_0)
        var_7 = data_loader_0.is_file(tuple_1)
        bool_0 = False
        var_8 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)
        set_0 = {var_8}
        data_loader_1 = module_0.DataLoader()
        bytes_0 = b'@\x80'
        str_1 = 'x@E1'
        var_9 = data_loader_0.path_dwim_relative_stack(set_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_25():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = 'tasks'
        int_0 = 2254
        var_0 = data_loader_0.path_dwim(str_0)
        var_1 = data_loader_0.cleanup_tmp_file(int_0)
        bool_0 = False
        var_2 = data_loader_0.path_dwim_relative(str_0, str_0, str_0, bool_0)
        data_loader_1 = module_0.DataLoader()
        display_0 = module_2.Display()
        str_1 = '~+<q=e(\n71%I@]D'
        bytes_0 = b'\x16'
        var_3 = data_loader_1.load_from_file(str_1, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_26():
    try:
        data_loader_0 = module_0.DataLoader()
        str_0 = ''
        var_0 = data_loader_0.load_from_file(str_0)
    except BaseException:
        pass