# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\x06\xde\x07.t\r\x84\x1e\xf0\xe4a\x91\x10\xbc\x8f\x80\xb8\xd0\x83'
    list_0 = [bytes_0]
    var_0 = module_0.symmetric_difference(bytes_0, list_0, list_0)

def test_case_2():
    bytes_0 = b"\xf5\x8e\x9afp\xc5'+*"
    str_0 = 'Sends a OPTIONS request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        '
    var_0 = module_0.max(bytes_0, str_0)

def test_case_3():
    bool_0 = True
    var_0 = module_0.logarithm(bool_0)

def test_case_4():
    bool_0 = False
    bool_1 = True
    var_0 = module_0.power(bool_0, bool_1)

def test_case_5():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_6():
    bytes_0 = b'm*\\\x89o[k|yqx8\xce-\xb7\x0cA\xcf'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.difference(bytes_0, list_0, bytes_0)

def test_case_7():
    str_0 = 'The human_to_bytes function should return the expected number of bytes.'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = False
    var_0 = module_0.unique(dict_0, dict_0, dict_0, bool_0)

def test_case_8():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    bytes_0 = b'\x06\xde\x07.t\r\x84\x1e\xf0\xe4a\x91\x10\xbc\x8f\x80\xb8\xd0\x83'
    list_0 = [set_0, bool_0, bytes_0]
    var_0 = module_0.symmetric_difference(bytes_0, list_0, list_0)