# Automatically generated by Pynguin.
import argparse as module_0
import requests.models as module_1
import httpie.core as module_2
import httpie.context as module_3

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        response_0 = module_1.Response()
        tuple_0 = module_2.get_output_options(namespace_0, response_0)
    except BaseException:
        pass

def test_case_1():
    try:
        namespace_0 = module_0.Namespace()
        environment_0 = module_3.Environment(namespace_0)
        exit_status_0 = module_2.program(namespace_0, environment_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xbb\xee\xc4\xccW\xdc'
        list_0 = [bytes_0]
        str_0 = None
        list_1 = module_2.decode_raw_args(list_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = []
        environment_0 = module_3.Environment()
        exit_status_0 = module_2.program(var_0, environment_0)
    except BaseException:
        pass

def test_case_4():
    try:
        environment_0 = module_3.Environment()
        var_0 = module_2.print_debug_info(environment_0)
        str_0 = 'Dyb)-VCI+c*u;F(\x0bK'
        list_0 = [str_0, str_0, str_0, str_0]
        list_1 = module_2.decode_raw_args(list_0, str_0)
        str_1 = 'c=DQ|n@?i!~^0'
        exit_status_0 = module_2.main(str_1)
        str_2 = ']Kk\x0cY6'
        dict_0 = {str_0: list_1, str_2: list_1}
        exit_status_1 = module_2.main(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'sC$2+4ocG'
        list_0 = [str_0, str_0, str_0]
        list_1 = [str_0, list_0, str_0]
        environment_0 = module_3.Environment(list_1)
        exit_status_0 = module_2.main(list_0, environment_0)
        str_1 = 'https://api.github.com/users/jakubroztocil'
        list_2 = [str_1, str_0]
        exit_status_1 = module_2.main(list_2)
        str_2 = [str_1, str_1, str_1, str_1]
        exit_status_2 = module_2.main(str_2)
        environment_1 = None
        var_0 = module_2.print_debug_info(environment_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    Specify a custom boundary string for multipart/form-data requests.\n    Only has effect only together with --form.\n\n    '
        list_0 = [str_0, str_0, str_0]
        list_1 = [str_0, list_0, str_0]
        environment_0 = module_3.Environment(list_1)
        exit_status_0 = module_2.main(list_0, environment_0)
        str_1 = 'https://api.github.com/users/jakubroztocil'
        list_2 = [str_1, str_0]
        exit_status_1 = module_2.main(list_2)
        str_2 = [str_1, str_1, str_1, str_1]
        exit_status_2 = module_2.main(str_2)
        environment_1 = None
        var_0 = module_2.print_debug_info(environment_1)
    except BaseException:
        pass