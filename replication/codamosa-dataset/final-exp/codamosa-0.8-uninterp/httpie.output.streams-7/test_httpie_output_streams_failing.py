# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.processing as module_1
import httpie.output.streams as module_2

def test_case_0():
    try:
        str_0 = 'B@-Ql'
        h_t_t_p_message_0 = module_0.HTTPMessage(str_0)
        conversion_0 = module_1.Conversion()
        base_stream_0 = module_2.BaseStream(h_t_t_p_message_0, conversion_0)
        str_1 = None
        optional_0 = conversion_0.get_converter(str_1)
        iterable_0 = base_stream_0.__iter__()
        bytes_0 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_1():
    try:
        raw_stream_0 = module_2.RawStream()
    except BaseException:
        pass

def test_case_2():
    try:
        encoded_stream_0 = module_2.EncodedStream()
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        conversion_0 = module_1.Conversion(**dict_0)
        list_0 = []
        formatting_0 = module_1.Formatting(list_0)
        pretty_stream_0 = module_2.PrettyStream(conversion_0, formatting_0, **dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n    The main function.\n\n    Pre-process args, handle some special types of invocations,\n    and run the main program with error handling.\n\n    Return exit status code.\n\n    '
        h_t_t_p_message_0 = module_0.HTTPMessage(str_0)
        bytes_0 = b'\xac\xc4L\xf0\xff\x88'
        binary_suppressed_error_0 = module_2.BinarySuppressedError()
        base_stream_0 = module_2.BaseStream(h_t_t_p_message_0, bytes_0, binary_suppressed_error_0)
        iterable_0 = base_stream_0.iter_body()
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, tuple_0]
        h_t_t_p_message_0 = module_0.HTTPMessage(list_0)
        set_0 = set()
        base_stream_0 = module_2.BaseStream(h_t_t_p_message_0, set_0, set_0)
    except BaseException:
        pass