# Automatically generated by Pynguin.
import requests.models as module_0
import httpie.context as module_1
import httpie.output.writer as module_2
import typing as module_3
import httpie.models as module_4
import httpie.output.streams as module_5
import argparse as module_6

def test_case_0():
    try:
        response_0 = module_0.Response()
        environment_0 = module_1.Environment()
        var_0 = {}
        bool_0 = True
        var_1 = module_2.write_message(response_0, environment_0, var_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        base_stream_0 = None
        i_o_0 = module_3.IO()
        bool_0 = False
        var_0 = module_2.write_stream(base_stream_0, i_o_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        h_t_t_p_message_0 = module_4.HTTPMessage(list_0)
        dict_0 = {h_t_t_p_message_0: h_t_t_p_message_0, list_0: h_t_t_p_message_0, h_t_t_p_message_0: h_t_t_p_message_0}
        base_stream_0 = module_5.BaseStream(h_t_t_p_message_0, dict_0)
        h_t_t_p_message_1 = module_4.HTTPMessage(base_stream_0)
        int_0 = -429
        dict_1 = {}
        text_i_o_0 = module_3.TextIO(**dict_1)
        base_stream_1 = module_5.BaseStream(h_t_t_p_message_1, int_0, text_i_o_0)
        bool_0 = None
        var_0 = module_2.write_stream_with_colors_win_py3(base_stream_1, text_i_o_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        environment_0 = module_1.Environment()
        namespace_0 = None
        tuple_0 = module_2.get_stream_type_and_kwargs(environment_0, namespace_0)
    except BaseException:
        pass

def test_case_4():
    try:
        prepared_request_0 = module_0.PreparedRequest()
        environment_0 = module_1.Environment()
        namespace_0 = module_6.Namespace()
        var_0 = module_2.write_message(prepared_request_0, environment_0, namespace_0)
        float_0 = 2394.891
        var_1 = module_2.write_message(prepared_request_0, environment_0, namespace_0, float_0)
    except BaseException:
        pass