# Automatically generated by Pynguin.
import httpie.output.streams as module_0
import httpie.output.processing as module_1
import httpie.models as module_2

def test_case_0():
    try:
        raw_stream_0 = module_0.RawStream()
    except BaseException:
        pass

def test_case_1():
    try:
        encoded_stream_0 = module_0.EncodedStream()
    except BaseException:
        pass

def test_case_2():
    try:
        conversion_0 = module_1.Conversion()
        list_0 = []
        dict_0 = {}
        formatting_0 = module_1.Formatting(list_0, **dict_0)
        pretty_stream_0 = module_0.PrettyStream(conversion_0, formatting_0)
    except BaseException:
        pass

def test_case_3():
    try:
        h_t_t_p_message_0 = None
        base_stream_0 = module_0.BaseStream(h_t_t_p_message_0)
        iterable_0 = base_stream_0.__iter__()
        raw_stream_0 = module_0.RawStream()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'formatting'
        binary_suppressed_error_0 = module_0.BinarySuppressedError()
        list_0 = [binary_suppressed_error_0, str_0]
        h_t_t_p_message_0 = module_2.HTTPMessage(list_0)
        base_stream_0 = module_0.BaseStream(h_t_t_p_message_0)
        bytes_0 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_5():
    try:
        h_t_t_p_message_0 = None
        base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, h_t_t_p_message_0)
        iterable_0 = base_stream_0.iter_body()
    except BaseException:
        pass

def test_case_6():
    try:
        h_t_t_p_message_0 = None
        base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, h_t_t_p_message_0)
        iterable_0 = base_stream_0.__iter__()
        dict_0 = {}
        optional_0 = None
        base_stream_1 = module_0.BaseStream(h_t_t_p_message_0, dict_0, optional_0)
    except BaseException:
        pass