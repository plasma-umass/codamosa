# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    try:
        connection_0 = module_0.Connection()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1032
        list_0 = [int_0, int_0, int_0]
        connection_0 = module_0.Connection(*list_0)
        bool_0 = False
        var_0 = connection_0.exec_command(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1032
        list_0 = [int_0, int_0, int_0]
        connection_0 = module_0.Connection(*list_0)
        list_1 = None
        var_0 = connection_0.put_file(list_1, list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b''
        bytes_1 = b'\x89\x9c]w'
        list_0 = [bytes_1, bytes_1, bytes_1, bytes_1]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.fetch_file(bytes_0, bytes_0)
    except BaseException:
        pass