# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0

def test_case_0():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_0 = module_0.wrap_var(ansible_unsafe_text_0)
        ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
        ansible_unsafe_text_2 = module_0.AnsibleUnsafeText(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '^\tjX>dAc]|'
        var_0 = module_0.wrap_var(str_0)
        bytes_0 = b'\x16\x01\x8aC\xd8\x02C\xb9\xa7\xa9\x02'
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        var_1 = module_0.wrap_var(bytes_0)
        native_jinja_unsafe_text_1 = module_0.NativeJinjaUnsafeText()
        unsafe_proxy_0 = module_0.UnsafeProxy()
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.to_unsafe_bytes()
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.to_unsafe_text()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 502
        str_0 = 'HkC!HF[f+9]&F`(\x0c_'
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        list_0 = [int_0, str_0]
        var_0 = module_0.wrap_var(list_0)
        dict_0 = {str_0: var_0, str_0: var_0, str_0: str_0, str_0: var_0, str_0: int_0, str_0: str_0}
        ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
        list_1 = [ansible_unsafe_text_0, str_0, int_0]
        var_1 = ansible_unsafe_text_1.encode(*list_1, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        ansible_unsafe_text_1 = None
        var_0 = module_0.wrap_var(ansible_unsafe_text_1)
        dict_0 = {}
        list_0 = [dict_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        var_1 = module_0.to_unsafe_text(**dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        list_0 = [dict_0, dict_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        var_0 = ansible_unsafe_text_0.encode(**dict_0)
        str_0 = 'HkC!HF[f+9]&F`(\x0c_'
        ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
        list_1 = [dict_0, var_0, var_0, str_0]
        var_1 = module_0.wrap_var(list_1)
        var_2 = module_0.wrap_var(ansible_unsafe_text_1)
        list_2 = [ansible_unsafe_text_0, ansible_unsafe_text_0, dict_0, ansible_unsafe_text_0]
        ansible_unsafe_text_2 = module_0.AnsibleUnsafeText(*list_2)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 502
        str_0 = 'HkC!HF[f+9]&F`(\x0c_'
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_0 = ansible_unsafe_text_0.encode()
        var_1 = ansible_unsafe_text_0.encode()
        list_0 = [var_0, str_0]
        var_2 = module_0.wrap_var(list_0)
        dict_0 = {str_0: str_0, str_0: int_0, str_0: str_0}
        ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
        list_1 = [ansible_unsafe_text_0, var_1, str_0, var_1, int_0]
        list_2 = [list_1, ansible_unsafe_text_1, ansible_unsafe_text_1, ansible_unsafe_text_1]
        var_3 = module_0.wrap_var(dict_0)
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_2)
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        ansible_unsafe_0 = module_0.AnsibleUnsafe(**dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ';hDLvWhO\x0cMI.{K3/'
        str_1 = '~--'
        dict_0 = {str_1: str_0}
        list_0 = None
        tuple_0 = (dict_0, list_0)
        bytes_0 = b'\xe5\xe7\xd2\x9f\x16\xba%nOuT\x88\xd5\x08'
        list_1 = [list_0, bytes_0, bytes_0]
        list_2 = [str_0, str_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_2)
        var_0 = unsafe_proxy_0.__new__(tuple_0, bytes_0, *list_1)
    except BaseException:
        pass