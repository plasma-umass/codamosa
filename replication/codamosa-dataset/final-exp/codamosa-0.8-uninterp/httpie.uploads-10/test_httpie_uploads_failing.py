# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import httpie.uploads as module_1
import requests_toolbelt.multipart.encoder as module_2
import requests.models as module_3
import typing as module_4

def test_case_0():
    try:
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict()
        bool_0 = False
        list_0 = [bool_0]
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(bool_0, list_0)
        iterable_0 = chunked_upload_stream_0.__iter__()
        multipart_encoder_0 = module_2.MultipartEncoder(iterable_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'file'
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict()
        tuple_0 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_0)
        bool_0 = True
        prepared_request_0 = module_3.PreparedRequest()
        var_0 = module_1.compress_request(prepared_request_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        prepared_request_0 = module_3.PreparedRequest()
        bool_0 = True
        var_0 = module_1.compress_request(prepared_request_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
        str_0 = '9_qS2p-zI*'
        var_0 = multipart_encoder_0.to_string()
        i_o_0 = module_4.IO(**dict_0)
        var_1 = i_o_0.read()
        bool_0 = True
        var_2 = module_1.prepare_request_body(str_0, var_1, bool_0)
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        var_3 = multipart_encoder_0.to_string()
        list_0 = []
        chunked_multipart_upload_stream_1 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict()
        str_1 = 'help'
        var_4 = module_1.prepare_request_body(multipart_encoder_0, list_0, str_1)
        var_5 = multipart_encoder_0.to_string()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        dict_0 = {list_0: list_0, list_0: list_0, list_0: list_0}
        multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
        str_0 = '!y>H'
        tuple_0 = (multipart_encoder_0, str_0)
        str_1 = ']|~^ 09~4tox'
        tuple_1 = (list_0, tuple_0, str_1)
        list_1 = [tuple_1]
        dict_1 = {}
        i_o_0 = module_4.IO(**dict_1)
        var_0 = i_o_0.__enter__()
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(list_1, var_0)
        multipart_encoder_1 = module_2.MultipartEncoder(chunked_upload_stream_0, list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        request_data_dict_0 = module_0.RequestDataDict()
        list_0 = [request_data_dict_0]
        request_data_dict_1 = module_0.RequestDataDict(*list_0)
        i_o_0 = module_4.IO()
        callable_0 = None
        var_0 = module_1.prepare_request_body(request_data_dict_1, callable_0)
        var_1 = i_o_0.readline()
        var_2 = i_o_0.__enter__()
        multipart_encoder_0 = module_2.MultipartEncoder(var_2)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        multipart_encoder_0 = module_2.MultipartEncoder(dict_0)
        str_0 = 'p -^&#&y]Wh\x0bk<#p'
        var_0 = multipart_encoder_0.to_string()
        tuple_0 = (multipart_encoder_0, str_0)
        i_o_0 = module_4.IO(**dict_0)
        var_1 = i_o_0.read()
        chunked_multipart_upload_stream_0 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        iterable_0 = chunked_multipart_upload_stream_0.__iter__()
        bytes_0 = b"\x84\x98\xb3\x8d\xd0:\xd6\x13\xba'[C\xcegu"
        tuple_1 = (tuple_0, bytes_0, multipart_encoder_0)
        list_0 = [tuple_1, bytes_0]
        chunked_upload_stream_0 = module_1.ChunkedUploadStream(list_0, tuple_1)
        str_1 = None
        list_1 = None
        dict_1 = {str_1: var_1, str_1: multipart_encoder_0, str_1: list_1}
        multipart_request_data_dict_0 = module_0.MultipartRequestDataDict(**dict_1)
        tuple_2 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_1)
        list_2 = []
        optional_0 = None
        chunked_multipart_upload_stream_1 = module_1.ChunkedMultipartUploadStream(multipart_encoder_0)
        multipart_request_data_dict_1 = module_0.MultipartRequestDataDict()
        var_2 = module_1.prepare_request_body(bytes_0, list_2, optional_0, multipart_request_data_dict_1)
        var_3 = multipart_encoder_0.to_string()
        int_0 = 1529
        var_4 = i_o_0.read(int_0)
        tuple_3 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_1, str_0, str_0)
        prepared_request_0 = module_3.PreparedRequest()
        prepared_request_1 = module_3.PreparedRequest()
        bool_0 = False
        multipart_encoder_1 = module_2.MultipartEncoder(iterable_0)
        chunked_multipart_upload_stream_2 = module_1.ChunkedMultipartUploadStream(multipart_encoder_1)
        tuple_4 = module_1.get_multipart_data_and_content_type(multipart_request_data_dict_0, str_1, str_0)
        request_data_dict_0 = module_0.RequestDataDict()
        var_5 = module_1.prepare_request_body(multipart_encoder_1, chunked_multipart_upload_stream_2, int_0, list_2, i_o_0)
        var_6 = module_1.compress_request(prepared_request_1, bool_0)
    except BaseException:
        pass