# Automatically generated by Pynguin.
import ansible.modules.debconf as module_0

def test_case_0():
    try:
        str_0 = '\'ZP11I\'H COCqut9ja"\x0c'
        bytes_0 = b''
        var_0 = module_0.get_selections(str_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'4\n\xc9J\x015~\xbb\xb7 \xff\xde\xdaVP\xc3\x92'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        float_0 = -1778.7
        tuple_0 = None
        int_0 = 255
        var_0 = module_0.set_selection(bytes_0, bytes_0, list_0, float_0, tuple_0, int_0)
    except BaseException:
        pass