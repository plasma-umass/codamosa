# Automatically generated by Pynguin.
import flutils.pathutils as module_0
import pathlib as module_1

def test_case_0():
    try:
        str_0 = '/pynguin/G\\}~)H'
        path_0 = module_0.directory_present(str_0)
        module_0.path_absent(str_0)
        str_1 = 'Mr4.!Iqld'
        struct_group_0 = module_0.get_os_group(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1000000
        struct_passwd_0 = module_0.get_os_user(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Mr4.!Iqld'
        struct_passwd_0 = module_0.get_os_user(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        struct_group_0 = module_0.get_os_group()
        struct_passwd_0 = module_0.get_os_user()
        bytes_0 = b'\xe9d\xad\xc0'
        str_0 = module_0.exists_as(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'5'
        str_0 = module_0.exists_as(bytes_0)
        int_0 = 3706
        path_0 = module_0.directory_present(bytes_0, int_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '/pykgui/\\}~)H'
        path_0 = module_0.directory_present(str_0)
        int_0 = 327
        path_1 = module_0.directory_present(str_0, int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '~/fobar/az'
        path_0 = module_0.directory_present(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        struct_passwd_0 = module_0.get_os_user()
        struct_group_0 = module_0.get_os_group()
        dict_0 = {struct_passwd_0: struct_passwd_0, struct_passwd_0: struct_passwd_0}
        struct_group_1 = module_0.get_os_group(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '/pynuin'
        path_0 = module_0.directory_present(str_0)
        module_0.path_absent(str_0)
        str_1 = ":Gv?;u\t'?%AK"
        generator_0 = module_0.find_paths(str_1)
        posix_path_0 = module_1.PosixPath()
        str_2 = '7kh]LD2uJ4b&_-'
        str_3 = None
        dict_0 = {str_2: posix_path_0, str_1: str_1, str_0: str_3}
        windows_path_0 = module_1.WindowsPath(**dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/pyngui/\\}~6H'
        generator_0 = module_0.find_paths(str_0)
        str_1 = '/'
        generator_1 = module_0.find_paths(str_1)
        module_0.chmod(str_0, generator_1)
        module_0.path_absent(str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 2257
        struct_group_0 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -2070
        struct_group_0 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = None
        str_0 = None
        struct_group_0 = module_0.get_os_group(str_0)
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = '3d:G[b'
        tuple_0 = (bytes_0, dict_0, bytes_0, str_1)
        struct_passwd_0 = module_0.get_os_user(tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '/pfnP\\b&/\\~;H'
        path_0 = module_0.directory_present(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '~/tmp/**'
        int_0 = 420
        int_1 = 504
        module_0.chmod(str_0, int_0, int_1)
        module_0.chmod(str_0)
        path_0 = module_0.directory_present(str_0, str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '/tmp/flutils.pathutils.chown.txt'
        module_0.chown(str_0)
        str_1 = '/tmp/flutils.pathutils.chown.txt'
        str_2 = 'nobody'
        module_0.chown(str_1, str_2)
        str_3 = 'OSError not raised'
        var_0 = AssertionError(str_3)
        str_4 = '/tmp/flutils.pathutils.chown.txt'
        str_5 = 'nobody'
        module_0.chown(str_4, str_5)
        str_6 = 'OSError not raised'
        var_1 = AssertionError(str_6)
        str_7 = 'root'
        module_0.chown(str_6, str_7, str_7)
    except BaseException:
        pass

def test_case_16():
    try:
        struct_passwd_0 = module_0.get_os_user()
        str_0 = '/pyngui/\\}~6H'
        path_0 = module_0.directory_present(str_0)
        str_1 = '/'
        generator_0 = module_0.find_paths(str_1)
        path_1 = module_0.directory_present(str_1)
        module_0.chmod(str_0, generator_0)
        module_0.path_absent(str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '/Pr/\\~k'
        path_0 = module_0.directory_present(str_0)
        generator_0 = module_0.find_paths(str_0)
        path_1 = module_0.normalize_path(str_0)
        bool_0 = True
        var_0 = path_0.as_posix()
        module_0.chmod(str_0, bool_0)
        module_0.path_absent(str_0)
        module_0.path_absent(str_0)
        var_1 = path_1.touch()
        module_0.chmod(str_0)
        module_0.chown(str_0, bool_0)
        str_1 = '^'
        module_0.chown(str_0, str_1, str_1)
    except BaseException:
        pass