# Automatically generated by Pynguin.
import thefuck.rules.no_such_file as module_0

def test_case_0():
    try:
        str_0 = '\n'
        var_0 = module_0.match(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'z\xbe\x1e\x85\xde\xb3\xcd'
        var_0 = module_0.get_new_command(bytes_0)
    except BaseException:
        pass