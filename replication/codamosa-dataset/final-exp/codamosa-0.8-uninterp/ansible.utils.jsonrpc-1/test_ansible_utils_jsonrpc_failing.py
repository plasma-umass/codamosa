# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0

def test_case_0():
    try:
        bool_0 = False
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.handle_request(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 3207.0
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.handle_request(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n        "method": "rpc_method",\n        "params": [[], {}],\n        "id": 1\n    }'
        var_0 = json_rpc_server_0.handle_request(str_0)
        bytes_0 = b'\xdfR\xf4\xc2\x10\x0cX \xd3\x8f\r'
        var_1 = json_rpc_server_0.register(bytes_0)
        set_0 = {json_rpc_server_0}
        var_2 = json_rpc_server_0.handle_request(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.invalid_request()
    except BaseException:
        pass

def test_case_4():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.response()
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.parse_error(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n        "method": "rpc_method",\n        "params": [[], {}],\n       "id": 1\n    }'
        var_0 = json_rpc_server_0.handle_request(str_0)
        dict_0 = {var_0: str_0, str_0: str_0, var_0: var_0, json_rpc_server_0: json_rpc_server_0}
        var_1 = json_rpc_server_0.internal_error(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"method":"test123"}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '{"jsonrpc": "2.0", "id": "1", "method": "rpc.run", "params": [["arg1", "arg2"], {"hello": "world"}]}'
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass