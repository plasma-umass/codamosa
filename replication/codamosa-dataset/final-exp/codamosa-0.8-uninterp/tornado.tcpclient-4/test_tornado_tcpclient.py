# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import ssl as module_1
import tornado.ioloop as module_2
import datetime as module_3
import tornado.netutil as module_4
import socket as module_5
import _asyncio as module_6

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    s_s_l_context_0 = module_1.SSLContext()
    t_c_p_client_0 = module_0.TCPClient(s_s_l_context_0)

def test_case_3():
    s_s_l_context_0 = module_1.SSLContext()
    t_c_p_client_0 = module_0.TCPClient(s_s_l_context_0)
    t_c_p_client_0.close()

def test_case_4():
    dict_0 = {}
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    bool_0 = True
    connector_0 = module_0._Connector(list_0, bool_0)
    connector_0.clear_timeouts()
    timedelta_0 = module_3.timedelta()
    connector_0.on_connect_timeout()

def test_case_5():
    dict_0 = {}
    resolver_0 = module_4.Resolver(**dict_0)
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0]
    bool_0 = True
    connector_0 = module_0._Connector(list_0, bool_0)
    timedelta_0 = module_3.timedelta()
    connector_0.on_timeout()

def test_case_6():
    dict_0 = {}
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    bool_0 = True
    connector_0 = module_0._Connector(list_0, bool_0)
    connector_0.clear_timeouts()
    timedelta_0 = module_3.timedelta()
    connector_0.set_connect_timeout(timedelta_0)
    connector_0.on_timeout()

def test_case_7():
    str_0 = 'q]fw`lX+'
    dict_0 = {}
    resolver_0 = module_4.Resolver(**dict_0)
    int_0 = 2071
    awaitable_0 = resolver_0.resolve(str_0, int_0)
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0, tuple_0]
    bool_0 = True
    connector_0 = module_0._Connector(list_0, bool_0)
    connector_0.clear_timeout()
    connector_0.clear_timeouts()
    connector_0.on_timeout()
    callable_0 = None
    connector_1 = module_0._Connector(list_0, callable_0)
    connector_0.close_streams()

def test_case_8():
    str_0 = 'q]fw`lX+'
    dict_0 = {}
    resolver_0 = module_4.Resolver(**dict_0)
    int_0 = 2071
    awaitable_0 = resolver_0.resolve(str_0, int_0)
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    bool_0 = True
    connector_0 = module_0._Connector(list_0, bool_0)
    float_0 = 554.9454
    connector_0.set_timeout(float_0)
    connector_0.clear_timeouts()
    list_1 = [tuple_0, tuple_0, tuple_0]
    str_1 = ''
    connector_1 = module_0._Connector(list_1, str_1)
    list_2 = [tuple_0, tuple_0]
    connector_1.clear_timeouts()
    int_1 = 200
    connector_2 = module_0._Connector(list_2, int_1)
    connector_1.on_timeout()
    timedelta_0 = module_3.timedelta(**dict_0)
    callable_0 = None
    connector_3 = module_0._Connector(list_2, callable_0)
    connector_1.close_streams()
    connector_2.on_connect_timeout()

def test_case_9():
    dict_0 = {}
    resolver_0 = module_4.Resolver(**dict_0)
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    address_family_0 = module_5.AddressFamily.AF_NETLINK
    connector_0 = module_0._Connector(list_0, address_family_0)
    connector_0.on_connect_timeout()
    future_0 = module_6.Future()
    connector_0.on_connect_done(address_family_0, address_family_0, tuple_0, future_0)

def test_case_10():
    dict_0 = {}
    resolver_0 = module_4.Resolver(**dict_0)
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop(**dict_0)
    tuple_0 = (dict_0, i_o_loop_0)
    list_0 = [tuple_0, tuple_0]
    bool_0 = True
    connector_0 = module_0._Connector(list_0, bool_0)
    float_0 = 4249.3877
    connector_0.set_connect_timeout(float_0)
    timedelta_0 = module_3.timedelta()
    connector_0.on_timeout()
    connector_0.clear_timeouts()