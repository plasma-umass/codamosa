# Automatically generated by Pynguin.
import flutils.pathutils as module_0
import pathlib as module_1
import os as module_2

def test_case_0():
    try:
        str_0 = 'koH'
        int_0 = 0
        module_0.chmod(str_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'EMy.#$S=6mzw'
        module_0.chown(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '-e>zk"\x0czoeyv>'
        path_0 = module_0.normalize_path(str_0)
        path_1 = module_0.directory_present(str_0)
        module_0.chown(str_0)
        str_1 = 'D1L;LdK\nA)%\nPt,>(NQ'
        str_2 = 'c,a!7'
        generator_0 = module_0.find_paths(str_2)
        str_3 = module_0.exists_as(str_1)
        struct_group_0 = module_0.get_os_group()
        str_4 = '0$m~33W-zU)@CCumy*V&'
        generator_1 = module_0.find_paths(str_4)
        str_5 = '\rr\rp[(>ltU9[DToJ'
        module_0.path_absent(str_5)
        module_0.path_absent(str_4)
        str_6 = '%{&7J0WP'
        dict_0 = {str_4: str_4, str_5: str_4, str_6: str_5, str_4: str_5}
        struct_group_1 = module_0.get_os_group()
        list_0 = [str_4]
        posix_path_0 = module_1.PosixPath(*list_0)
        str_7 = None
        module_0.chown(posix_path_0, str_7)
        path_like_0 = module_2.PathLike(**dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'JY_Df'
        path_0 = module_0.directory_present(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/pnguin/-e>z"\x0cz8Ie'
        generator_0 = module_0.find_paths(str_0)
        path_0 = module_0.directory_present(str_0)
        module_0.chown(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = None
        str_0 = module_0.exists_as(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/p4nguin/->>zk"\x0czoeyv>'
        int_0 = 744
        module_0.chmod(str_0, int_0)
        struct_group_0 = module_0.get_os_group(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        struct_passwd_0 = module_0.get_os_user(bool_0)
        str_0 = 'JY_Df'
        path_0 = module_0.directory_present(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        struct_group_0 = module_0.get_os_group()
        bytes_0 = b'\xe4\xed\xb4G\xea\x961\xf8\xef\x82\x8b\xcc\x02\xc7bnD\x8a'
        generator_0 = module_0.find_paths(bytes_0)
        int_0 = 749
        struct_passwd_0 = module_0.get_os_user(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/pnguin/-e>z"\x0cz8Ie'
        path_0 = module_0.directory_present(str_0)
        path_1 = module_0.normalize_path(str_0)
        module_0.chown(str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '/dev/null'
        str_1 = module_0.exists_as(str_0)
        module_0.path_absent(str_0)
        bytes_0 = b'\x95\xb6\xabD'
        module_0.chmod(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        struct_group_0 = module_0.get_os_group()
        str_0 = '/pbBguin'
        module_0.path_absent(str_0)
        module_0.chmod(str_0)
        path_like_0 = None
        list_0 = [path_like_0, path_like_0, path_like_0, path_like_0]
        windows_path_0 = module_1.WindowsPath(*list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '/'
        path_0 = module_0.normalize_path(str_0)
        module_0.path_absent(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 3163
        struct_group_0 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = 353.137
        struct_passwd_0 = module_0.get_os_user(float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        struct_passwd_0 = module_0.get_os_user()
        int_0 = -2107
        struct_group_0 = module_0.get_os_group(int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b''
        module_0.path_absent(bytes_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b'g\xf8\x1f\x9f\xc2\xf2\xf5'
        generator_0 = module_0.find_paths(bytes_0)
        bytes_1 = b'\xe4\xed\xb4G\xea\x961\xf8\xef\x82\x8b\xcc\x02\xc7bnD\x8a'
        generator_1 = module_0.find_paths(bytes_1)
        str_0 = '/bguin/->zk"\x0c/;ev'
        none_type_0 = None
        path_0 = module_0.directory_present(str_0, none_type_0)
        module_0.path_absent(str_0)
        module_0.path_absent(str_0)
        int_0 = 749
        module_0.chmod(str_0, int_0)
        str_1 = module_0.exists_as(str_0)
        struct_passwd_0 = module_0.get_os_user(int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        list_0 = []
        struct_group_0 = module_0.get_os_group(list_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '~/tmp/*'
        generator_0 = module_0.find_paths(str_0)
        var_0 = list(generator_0)
        var_1 = len(var_0)
        int_0 = 0
        var_2 = var_0[int_0]
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '/pynguin/-e>zk"\x0czoeyv>'
        none_type_0 = None
        path_0 = module_0.directory_present(str_0, none_type_0)
        path_1 = module_0.directory_present(str_0)
        module_0.path_absent(str_0)
        module_0.path_absent(str_0)
        bool_0 = None
        module_0.chmod(str_0, bool_0)
        str_1 = module_0.exists_as(str_0)
        bool_1 = True
        module_0.chown(str_0, str_1, bool_1)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = '/'
        path_0 = module_0.directory_present(str_0)
        bool_0 = True
        module_0.chown(str_0, bool_0)
        module_0.path_absent(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        struct_group_0 = module_0.get_os_group()
        bytes_0 = b'\xe4\xed\xb4G\xea\x961\xf8\xef\x82\x8b\xcc\x02\xc7bnD\x8a'
        generator_0 = module_0.find_paths(bytes_0)
        str_0 = '/pyngu*n/-zk"\x0c/;eyv'
        path_0 = module_0.directory_present(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        bytes_0 = b'\xe4\xed\xb4G\xea\x961\xf8\xef\x82\x8b\xcc\x02\xc7bnD\x8a'
        generator_0 = module_0.find_paths(bytes_0)
        str_0 = '/Upyngn/-f\x0c/;ynv'
        none_type_0 = None
        path_0 = module_0.directory_present(str_0, none_type_0)
    except BaseException:
        pass

def test_case_24():
    try:
        bytes_0 = b'\xe4\xed\xb4G\xea\x961\xf8\xef\x82\x8b\xcc\x02\xc7bnD\x8a'
        generator_0 = module_0.find_paths(bytes_0)
        str_0 = '/Upyngn/-f\x0c/;ynv'
        none_type_0 = None
        path_0 = module_0.directory_present(str_0, none_type_0)
        path_1 = module_0.directory_present(str_0)
        module_0.path_absent(str_0)
        bool_0 = False
        module_0.chown(str_0, bool_0)
        module_0.path_absent(str_0)
        var_0 = path_1.touch()
        str_1 = module_0.exists_as(str_0)
        module_0.chown(str_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '/pynguin'
        none_type_0 = None
        path_0 = module_0.directory_present(str_0, none_type_0)
        path_1 = module_0.directory_present(str_0)
        module_0.path_absent(str_0)
        module_0.path_absent(str_0)
        int_0 = 749
        module_0.chmod(str_0, int_0)
        str_1 = module_0.exists_as(str_0)
        struct_group_0 = module_0.get_os_group()
        dict_0 = {}
        path_like_0 = module_2.PathLike(**dict_0)
    except BaseException:
        pass