# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.netutil as module_1
import tornado.ioloop as module_2
import concurrent.futures._base as module_3
import socket as module_4
import _asyncio as module_5
import tornado.gen as module_6

def test_case_0():
    try:
        list_0 = []
        dict_0 = {}
        connector_0 = module_0._Connector(list_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '+*$#Lu\nxpGUqd'
        int_0 = -1981
        t_c_p_client_0 = module_0.TCPClient()
        i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0)
        int_1 = 5319
        tuple_0 = (int_1,)
        list_0 = [tuple_0, tuple_0, tuple_0]
        resolver_0 = module_1.Resolver()
        t_c_p_client_1 = module_0.TCPClient(resolver_0)
        connector_0 = module_0._Connector(list_0, t_c_p_client_1)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        list_0 = []
        i_o_loop_1.make_current()
        selectable_0 = module_2._Selectable(*list_0)
        i_o_loop_1.close_fd(selectable_0)
        tuple_1 = (tuple_0, i_o_loop_1)
        resolver_0 = module_1.Resolver()
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        t_c_p_client_0.close()
        list_1 = [tuple_1, tuple_1, tuple_1]
        connector_0 = module_0._Connector(list_1, tuple_0)
        connector_0.close_streams()
        connector_0.close_streams()
        callable_0 = None
        connector_1 = module_0._Connector(list_1, callable_0)
        connector_0.clear_timeout()
        connector_1.on_timeout()
        future_0 = module_3.Future()
        address_family_0 = module_4.AddressFamily.AF_X25
        future_1 = module_5.Future()
        iterator_0 = None
        connector_1.on_connect_done(iterator_0, address_family_0, tuple_1, future_1)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        tuple_1 = (tuple_0, i_o_loop_1)
        list_0 = [tuple_1, tuple_1, tuple_1]
        bytes_0 = b'\xf4\xad\xa6\xb7\xa3\xb1\x8136h\xd0\xfdj\xd0C?Wpx'
        connector_0 = module_0._Connector(list_0, bytes_0)
        connector_0.on_timeout()
        future_0 = module_3.Future()
        connector_0.try_connect(future_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        i_o_loop_2 = i_o_loop_0.instance()
        i_o_loop_3 = i_o_loop_2.instance()
        tuple_1 = (tuple_0, i_o_loop_3)
        list_0 = [tuple_1, tuple_1, tuple_1]
        int_0 = -1279
        list_1 = [int_0]
        connector_0 = module_0._Connector(list_0, list_1)
        connector_0.on_connect_timeout()
        float_0 = 425.36
        connector_0.on_timeout()
        connector_0.try_connect(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        i_o_loop_2 = i_o_loop_0.instance()
        i_o_loop_3 = i_o_loop_2.instance()
        int_0 = 8
        tuple_1 = i_o_loop_0.split_fd(int_0)
        tuple_2 = (tuple_0, i_o_loop_3)
        list_0 = [tuple_2, tuple_2]
        str_0 = '&f'
        connector_0 = module_0._Connector(list_0, str_0)
        future_0 = connector_0.start()
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        i_o_loop_2 = i_o_loop_0.instance()
        tuple_1 = (tuple_0, i_o_loop_1)
        list_0 = [tuple_1, tuple_1, tuple_1]
        int_0 = 426
        list_1 = [int_0]
        connector_0 = module_0._Connector(list_0, list_1)
        connector_0.on_connect_timeout()
        float_0 = 20.0
        connector_0.set_timeout(float_0)
        optional_0 = i_o_loop_1.current()
        float_1 = 425.36
        connector_0.on_timeout()
        connector_0.try_connect(float_1)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        list_0 = []
        selectable_0 = module_2._Selectable(*list_0)
        i_o_loop_1.close_fd(selectable_0)
        tuple_1 = (tuple_0, i_o_loop_1)
        list_1 = [tuple_1, tuple_1, tuple_1]
        connector_0 = module_0._Connector(list_1, tuple_0)
        connector_0.close_streams()
        connector_0.on_timeout()
        future_0 = module_3.Future()
        address_family_0 = module_4.AddressFamily.AF_X25
        future_1 = module_5.Future()
        connector_0.on_connect_done(tuple_0, address_family_0, tuple_1, future_1)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = None
        i_o_loop_0 = module_2.IOLoop()
        tuple_1 = (tuple_0, i_o_loop_0)
        list_0 = [tuple_1, tuple_1]
        future_0 = module_3.Future()
        connector_0 = module_0._Connector(list_0, future_0)
        connector_0.on_connect_timeout()
        list_1 = [tuple_1, tuple_1, tuple_1]
        bytes_0 = b'\xf4\xad\xa6\xb7W\xb1\x8136h\x80\xfdj\xd0C?Wpx'
        connector_1 = module_0._Connector(list_1, bytes_0)
        connector_1.on_connect_timeout()
        iterator_0 = None
        address_family_0 = module_4.AddressFamily.AF_X25
        awaitable_0 = None
        list_2 = [awaitable_0, awaitable_0, awaitable_0, awaitable_0]
        future_1 = module_6.convert_yielded(list_2)
        connector_0.on_connect_done(iterator_0, address_family_0, tuple_1, future_1)
    except BaseException:
        pass