# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.streams as module_1
import httpie.output.processing as module_2

def test_case_0():
    try:
        int_0 = 8
        h_t_t_p_message_0 = module_0.HTTPMessage(int_0)
        bool_0 = True
        set_0 = {int_0, h_t_t_p_message_0, int_0, bool_0}
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, set_0)
        iterable_0 = base_stream_0.iter_body()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '(lkqci\tHJWLMuN'
        h_t_t_p_message_0 = module_0.HTTPMessage(str_0)
        float_0 = -1832.47
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, float_0)
        bytes_0 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_2():
    try:
        raw_stream_0 = module_1.RawStream()
    except BaseException:
        pass

def test_case_3():
    try:
        encoded_stream_0 = module_1.EncodedStream()
    except BaseException:
        pass

def test_case_4():
    try:
        conversion_0 = module_2.Conversion()
        formatting_0 = None
        buffered_pretty_stream_0 = module_1.BufferedPrettyStream(conversion_0, formatting_0)
    except BaseException:
        pass

def test_case_5():
    try:
        binary_suppressed_error_0 = module_1.BinarySuppressedError()
        h_t_t_p_message_0 = module_0.HTTPMessage(binary_suppressed_error_0)
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0)
        int_0 = 8
        h_t_t_p_message_1 = module_0.HTTPMessage(int_0)
        callable_0 = None
        base_stream_1 = module_1.BaseStream(h_t_t_p_message_1, callable_0)
        conversion_0 = module_2.Conversion()
        str_0 = ''
        base_stream_2 = module_1.BaseStream(h_t_t_p_message_1, str_0, callable_0)
    except BaseException:
        pass