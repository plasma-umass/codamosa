# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    try:
        str_0 = 'Debian'
        dict_0 = None
        str_1 = 'i-+g8?iS'
        float_0 = 825.7
        var_0 = module_0.setup_virtualenv(str_0, dict_0, dict_0, str_1, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Vb?@2;(]jz,'
        str_1 = 'P*Z4I2 '
        package_0 = module_0.Package(str_0, str_1)
        str_2 = 'distribu'
        package_1 = module_0.Package(str_2)
        float_0 = None
        var_0 = package_1.canonicalize_name(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xf1T]h\x115\xa0,QT\xaa\xe7E\xe9\xf4\x94'
        dict_0 = {bytes_0: bytes_0}
        float_0 = 0.2
        list_0 = [dict_0, float_0, float_0, float_0]
        package_0 = module_0.Package(list_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        str_0 = "A/0Y83{6$e4'L"
        package_0 = module_0.Package(str_0)
        var_0 = package_0.__str__()
        int_0 = 250
        bytes_0 = b'_9o\x82\xfa{\xccj\x8d\x1b\x9e^\xb0\xb5\xa0eX K'
        set_0 = {bytes_0, int_0, str_0, list_0}
        var_1 = package_0.is_satisfied_by(set_0)
        package_1 = module_0.Package(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'distribute'
        package_0 = module_0.Package(str_0)
        bytes_0 = b'\x1eR;DM0:\x0fe-)\x81\xdf\xd1\xeb/\xf5'
        var_0 = package_0.is_satisfied_by(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 347.0
        package_0 = module_0.Package(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dstribute'
        package_0 = module_0.Package(str_0)
        bytes_0 = b'\x1eR;DM0:\x0fe-)\x81\xdf\xd1\xeb/\xf5'
        var_0 = package_0.is_satisfied_by(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 2327
        str_0 = '6NSQH$!,HaY|uB;lg'
        package_0 = module_0.Package(int_0, str_0)
    except BaseException:
        pass