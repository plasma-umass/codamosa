# Automatically generated by Pynguin.
import httpie.context as module_0
import httpie.output.writer as module_1

def test_case_0():
    pass

def test_case_1():
    environment_0 = module_0.Environment()
    bytes_0 = b'\x1b[31m'
    bytes_1 = b'bar'
    bytes_2 = [bytes_1, bytes_0, bytes_1, bytes_1, bytes_0, bytes_1]
    var_0 = environment_0.stdout
    bool_0 = True
    var_1 = module_1.write_stream_with_colors_win_py3(bytes_2, var_0, bool_0)

def test_case_2():
    environment_0 = module_0.Environment()
    bytes_0 = b'\x1b[31m'
    bytes_1 = b'bar'
    bytes_2 = [bytes_1, bytes_0, bytes_1, bytes_1, bytes_0, bytes_1]
    var_0 = environment_0.stdout
    bool_0 = False
    var_1 = module_1.write_stream_with_colors_win_py3(bytes_2, var_0, bool_0)