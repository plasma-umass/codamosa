# Automatically generated by Pynguin.
import flutils.pathutils as module_0
import pathlib as module_1
import getpass as module_2

def test_case_0():
    try:
        str_0 = '/some/path/that/does/not/exist/*'
        module_0.chmod(str_0)
        int_0 = None
        path_0 = module_0.directory_present(str_0, int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        posix_path_0 = module_1.PosixPath()
        module_0.chmod(posix_path_0)
        path_like_0 = None
        str_0 = module_0.exists_as(path_like_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1961
        struct_passwd_0 = module_0.get_os_user()
        struct_group_0 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ' Test chown function.\n    '
        var_0 = module_2.getuser()
        str_1 = '~/tmp/flutils.tests.osutils.txt'
        module_0.chown(str_1, var_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1961
        struct_passwd_0 = module_0.get_os_user(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'RsOALR'
        struct_passwd_0 = module_0.get_os_user(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        struct_group_0 = module_0.get_os_group()
        bytes_0 = b'0\xae)\xbd'
        path_0 = module_0.normalize_path(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '/'
        path_0 = module_0.directory_present(str_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        posix_path_0 = module_1.PosixPath()
        int_0 = 3748
        struct_group_0 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '~/tmp/flutils.tests.osutils.txt'
        module_0.chown(str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        posix_path_0 = module_1.PosixPath()
        struct_passwd_0 = module_0.get_os_user()
        optional_0 = None
        path_0 = module_0.normalize_path(posix_path_0)
        path_1 = module_0.normalize_path(posix_path_0)
        module_0.chmod(posix_path_0, optional_0)
        list_0 = [optional_0]
        struct_group_0 = module_0.get_os_group(list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ' Cannot be a keyword.'
        generator_0 = module_0.find_paths(str_0)
        generator_1 = module_0.find_paths(str_0)
        generator_2 = module_0.find_paths(str_0)
        path_0 = module_0.directory_present(str_0)
        bytes_0 = b'a'
        path_1 = module_0.normalize_path(bytes_0)
        path_2 = module_0.directory_present(bytes_0)
        bool_0 = False
        module_0.chown(bytes_0, bool_0)
        generator_3 = module_0.find_paths(str_0)
        str_1 = module_0.exists_as(bytes_0)
        struct_group_0 = module_0.get_os_group()
        str_2 = module_0.exists_as(str_0)
        struct_group_1 = module_0.get_os_group()
        module_0.path_absent(bytes_0)
        module_0.path_absent(str_0)
        str_3 = module_0.exists_as(bytes_0)
        path_3 = module_0.directory_present(bytes_0)
        optional_0 = None
        path_4 = module_0.directory_present(bytes_0, optional_0, str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '/'
        module_0.path_absent(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = ',o'
        str_1 = '/etc/hosts'
        path_0 = module_0.normalize_path(str_1)
        int_0 = -480
        module_0.chmod(str_1, int_0)
        path_1 = module_0.directory_present(str_1, str_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '/tc/hoss'
        str_1 = module_0.exists_as(str_0)
        str_2 = '/dev/sda'
        str_3 = module_0.exists_as(str_2)
        str_4 = module_0.exists_as(str_2)
        str_5 = '/dev/stdin'
        str_6 = module_0.exists_as(str_2)
        module_0.path_absent(str_5)
        module_0.path_absent(str_2)
        str_7 = module_0.exists_as(str_6)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '~/tmp/flutils.*'
        module_0.chown(str_0)
        bool_0 = True
        module_0.chown(str_0, bool_0)
        str_1 = 'flutils_test_user'
        str_2 = 'flutils_test_group'
        module_0.chown(str_0, str_1, str_2)
    except BaseException:
        pass

def test_case_16():
    try:
        set_0 = set()
        struct_passwd_0 = module_0.get_os_user(set_0)
    except BaseException:
        pass