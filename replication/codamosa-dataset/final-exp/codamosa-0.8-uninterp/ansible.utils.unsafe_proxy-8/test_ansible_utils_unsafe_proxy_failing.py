# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0

def test_case_0():
    try:
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        int_0 = 308
        var_0 = ansible_unsafe_bytes_0.decode()
        list_0 = [ansible_unsafe_bytes_0, int_0]
        ansible_unsafe_bytes_1 = module_0.AnsibleUnsafeBytes()
        var_1 = ansible_unsafe_bytes_1.decode(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.to_unsafe_bytes()
    except BaseException:
        pass

def test_case_2():
    try:
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_0 = module_0.to_unsafe_text()
    except BaseException:
        pass

def test_case_3():
    try:
        native_jinja_unsafe_text_0 = None
        ansible_unsafe_0 = module_0.AnsibleUnsafe()
        var_0 = module_0.wrap_var(native_jinja_unsafe_text_0)
        native_jinja_unsafe_text_1 = module_0.NativeJinjaUnsafeText()
        list_0 = None
        var_1 = module_0.to_unsafe_text(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_0 = ansible_unsafe_bytes_0.decode()
        str_0 = 'C\t{i\n!)82%l1"'
        dict_0 = None
        list_0 = [ansible_unsafe_text_0, str_0, ansible_unsafe_text_0, dict_0]
        var_1 = module_0.wrap_var(list_0)
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        dict_1 = {}
        unsafe_proxy_0 = module_0.UnsafeProxy(**dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_0 = ansible_unsafe_bytes_0.decode()
        float_0 = 3966.22
        var_1 = module_0.wrap_var(float_0)
        dict_0 = {}
        unsafe_proxy_0 = module_0.UnsafeProxy(**dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ExE`;a&'
        dict_0 = {}
        list_0 = [str_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        dict_1 = {str_0: dict_0, str_0: unsafe_proxy_0}
        unsafe_proxy_1 = module_0.UnsafeProxy(**dict_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'z\xf3\xa9\x86\xbd\xe7>\xbd\xecx\x92\xb1&\x0b\x08\xed\xaf'
        set_0 = {bytes_0, bytes_0, bytes_0}
        var_0 = module_0.wrap_var(set_0)
        dict_0 = {}
        list_0 = None
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText(**dict_0)
        ansible_unsafe_text_1 = module_0.AnsibleUnsafeText(**dict_0)
        var_1 = ansible_unsafe_text_0.encode()
        ansible_unsafe_text_2 = module_0.AnsibleUnsafeText()
        var_2 = ansible_unsafe_text_0.encode(*list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        ansible_unsafe_text_1 = None
        dict_0 = {ansible_unsafe_text_1: ansible_unsafe_text_1, ansible_unsafe_text_1: ansible_unsafe_text_1, ansible_unsafe_text_1: ansible_unsafe_text_1, ansible_unsafe_text_1: ansible_unsafe_text_1}
        var_0 = module_0.wrap_var(dict_0)
        set_0 = set()
        var_1 = module_0.wrap_var(set_0)
        ansible_unsafe_0 = None
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        list_0 = [ansible_unsafe_0, ansible_unsafe_0]
        var_2 = module_0.to_unsafe_text(*list_0)
        list_1 = [ansible_unsafe_0, ansible_unsafe_0]
        str_0 = ";f<'\x0cv_]U<`vmu"
        str_1 = '8P$H}B'
        dict_1 = {str_0: list_1, str_1: list_0}
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText(*list_0, **dict_1)
    except BaseException:
        pass