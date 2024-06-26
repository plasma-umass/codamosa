# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = 'method'
        var_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_1 = module_1.dumps(var_0)
        var_2 = json_rpc_server_0.handle_request(var_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x14\x89\x1bV\xe9\x08'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        list_0 = [set_0]
        float_0 = -451.0887
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = None
        tuple_0 = (str_0, float_0, bytes_0)
        var_0 = json_rpc_server_0.register(tuple_0)
        var_1 = json_rpc_server_0.error(set_0, list_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.method_not_found()
    except BaseException:
        pass

def test_case_3():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.response()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        json_rpc_server_0 = module_0.JsonRpcServer(*list_0)
        var_0 = json_rpc_server_0.parse_error()
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        json_rpc_server_0 = module_0.JsonRpcServer(**dict_0)
        json_rpc_server_1 = module_0.JsonRpcServer(**dict_0)
        json_rpc_server_2 = module_0.JsonRpcServer(**dict_0)
        var_0 = json_rpc_server_0.invalid_request()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Dvq9B4$T[fCB\\'
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = [dict_0, str_0, str_0, str_0]
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.invalid_params(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.internal_error()
    except BaseException:
        pass