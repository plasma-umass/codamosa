# Automatically generated by Pynguin.
import ansible.parsing.utils.jsonify as module_0

def test_case_0():
    try:
        bytes_0 = b'\x1ct/<\x90\xee\x08\xea\x98G\x1cH!\x06\x08@Kw'
        var_0 = module_0.jsonify(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ';y,>>LS8\t$aJvg\x0cm/B{/'
        set_0 = {str_0, str_0, str_0, str_0}
        int_0 = None
        var_0 = module_0.jsonify(int_0)
        float_0 = 0.0
        var_1 = module_0.jsonify(set_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\n\x8f,\xcb\x1f\x08\xdfV\x84\xd7'
        var_0 = module_0.jsonify(bytes_0, bytes_0)
    except BaseException:
        pass