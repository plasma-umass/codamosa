# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    try:
        explicit_null_auth_0 = None
        var_0 = module_0.load_json_preserve_order(explicit_null_auth_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 985.3602525084842
        var_0 = module_0.get_content_type(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xda\xa8c\x8a\xb4Cn\xd7\xcc\xd9g\x02k\xfeA\xbd\xec'
        float_0 = 0.1
        var_0 = module_0.humanize_bytes(float_0)
        var_1 = module_0.get_content_type(bytes_0)
    except BaseException:
        pass