# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'{\n  "method": "index",\n  "params": [\n    [\n      "est-dsk1",\n      "test-dik%",\n      "test-disk3"\n    ],\n   {\n      "test1": "test1",\n      "test2": "test2"\n    }\n  ],\n  "jsonrpc": "2.0",\n  "id": "1"\n}'
    json_rpc_server_0 = module_0.JsonRpcServer()
    var_0 = json_rpc_server_0.register(json_rpc_server_0)
    var_1 = json_rpc_server_0.handle_request(bytes_0)

def test_case_2():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '{\n"method": "add",\n"params": [1, 2],\n"id": 12345\n}'
    var_0 = json_rpc_server_0.handle_request(str_0)

def test_case_3():
    bytes_0 = b'{\n  "method": "index",\n  "params": [\n    [\n      "test-disk1",\n      "test-disk2",\n      "test-disk3"\n    ],\n    {\n      "test1": "test1",\n      "test2": "test2"\n    }\n  ],\n  "jsonrpc": "2.0",\n  "id": "1"\n}'
    json_rpc_server_0 = module_0.JsonRpcServer()
    var_0 = json_rpc_server_0.handle_request(bytes_0)

def test_case_4():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    var_1 = json_rpc_server_0.response(str_0)

def test_case_5():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    var_1 = json_rpc_server_0.response()
    var_2 = json_rpc_server_0.response(str_0)

def test_case_6():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    str_1 = 'test_method'
    var_0 = setattr(json_rpc_server_0, str_0, str_1)
    var_1 = json_rpc_server_0.response()
    str_2 = 'a string'
    var_2 = json_rpc_server_0.response(str_2)
    bytes_0 = b'a byte string'
    var_3 = json_rpc_server_0.response(bytes_0)