# Automatically generated by Pynguin.
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

def test_case_0():
    try:
        bytes_0 = b'N\xbf\xbd9\x9a\x01P\x115S\xe1g\xe7H'
        float_0 = 3.6
        int_0 = 293
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(float_0, int_0)
        var_0 = sorting_help_formatter_0.add_arguments(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        int_0 = 3339
        set_0 = None
        bool_0 = False
        list_0 = [bool_0, dict_0]
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(list_0, bool_0)
        float_0 = 0.0001
        ansible_version_0 = module_0.AnsibleVersion(float_0, set_0, set_0, list_0, int_0)
        str_0 = '--print'
        bytes_0 = b'\xc3\x85\xe17\x93\xc2\x023g\xd4\xb0Q\xb5+\xa08c\xd6\xbd'
        str_1 = '6Eu"pB'
        tuple_0 = None
        ansible_version_1 = module_0.AnsibleVersion(int_0, dict_0)
        tuple_1 = (tuple_0, ansible_version_1)
        str_2 = 'Added host %s to inventory'
        ansible_version_2 = module_0.AnsibleVersion(str_1, bytes_0, str_1, tuple_1, str_2)
        sorting_help_formatter_1 = module_0.SortingHelpFormatter(ansible_version_2)
        float_1 = 0.2
        unrecognized_argument_0 = module_0.UnrecognizedArgument(bytes_0, sorting_help_formatter_1, float_1)
        var_0 = unrecognized_argument_0.__call__(sorting_help_formatter_0, ansible_version_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 150
        bool_0 = True
        prepend_list_action_0 = module_0.PrependListAction(int_0, bool_0)
        bytes_0 = b'\x83\x7f\xac\xa23\xd3\x1aQ\xb5\x1f\xf5\xe7\x84\xac.\x0b~\x1c'
        var_0 = module_0.add_output_options(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        namespace_0 = module_1.Namespace()
        str_0 = '[~M'
        float_0 = -2089.0
        bool_0 = False
        dict_0 = {float_0: float_0, float_0: namespace_0, str_0: bool_0}
        prepend_list_action_0 = module_0.PrependListAction(namespace_0, bool_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        var_0 = module_0.add_fork_options(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = None
        var_0 = module_0.add_inventory_options(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = -120.35092
        var_0 = module_0.add_runas_options(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 636.757
        var_0 = module_0.add_runtask_options(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = ()
        var_0 = module_0.add_tasknoplay_options(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = None
        var_0 = module_0.add_subset_options(tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -789
        var_0 = module_0.add_vault_options(int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -913.32624
        list_0 = [float_0]
        var_0 = module_0.add_runas_prompt_options(float_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'WedTZN%^ $FAHtqE%i^'
        set_0 = {str_0, str_0, str_0}
        bool_0 = False
        dict_0 = {str_0: bool_0, bool_0: str_0, bool_0: str_0}
        prepend_list_action_0 = module_0.PrependListAction(set_0, set_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = None
        unrecognized_argument_0 = None
        list_0 = [bool_0, bool_0, bool_0, unrecognized_argument_0]
        str_0 = 'jBDVV[NQi)bHc@0g5<'
        bytes_0 = b'?\x04\xae\xb6<\xa6?\xc4\x89\xae[p'
        ansible_version_0 = module_0.AnsibleVersion(list_0, str_0, list_0, bytes_0)
        bytes_1 = b'\xbe\xeb\x19'
        str_1 = '`i'
        bool_1 = False
        prepend_list_action_0 = module_0.PrependListAction(str_1, bool_1, ansible_version_0)
        int_0 = 555
        tuple_0 = (bytes_1,)
        float_0 = -2059.192109
        var_0 = ansible_version_0.__call__(int_0, tuple_0, float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = -825
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(int_0)
        var_0 = module_0.add_fork_options(sorting_help_formatter_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'Runas test'
        argument_parser_0 = module_1.ArgumentParser(str_0)
        var_0 = module_0.add_runas_options(argument_parser_0)
        var_1 = argument_parser_0.parse_args(argument_parser_0)
    except BaseException:
        pass

def test_case_16():
    try:
        namespace_0 = module_1.Namespace()
        str_0 = '[~h8M'
        var_0 = module_0.ensure_value(namespace_0, str_0, namespace_0)
        var_1 = module_0.version()
        float_0 = 2.0
        str_1 = '\t#\x0bc'
        argument_parser_0 = module_1.ArgumentParser(namespace_0, str_1)
        bool_0 = None
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(bool_0)
        list_0 = [str_0, bool_0]
        tuple_0 = (str_1,)
        list_1 = [list_0, float_0]
        var_2 = module_0.add_output_options(argument_parser_0)
        str_2 = '-Command'
        dict_0 = {str_0: argument_parser_0, str_1: tuple_0, str_2: list_1}
        str_3 = 'j*f,M572~1M'
        prepend_list_action_0 = module_0.PrependListAction(dict_0, str_3, str_1, argument_parser_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        var_0 = module_0.version()
        int_0 = 732
        str_0 = '~P\x0c'
        list_0 = [str_0, int_0]
        bytes_0 = b'l\xf6\xc0\x96\xa5\xea\x08E\xb9\x11Ol'
        set_0 = {int_0}
        int_1 = -825
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(int_1)
        float_0 = -1971.9802170550765
        bool_0 = False
        unrecognized_argument_0 = module_0.UnrecognizedArgument(float_0, bool_0)
        bytes_1 = b'\xdf=\xcf&V\xc8\x1dj\x93\x1f\xb1\x83\x90\x81'
        tuple_0 = ()
        prepend_list_action_0 = module_0.PrependListAction(sorting_help_formatter_0, tuple_0, set_0)
        list_1 = None
        argument_parser_0 = module_1.ArgumentParser(list_1)
        var_1 = module_0.add_subset_options(argument_parser_0)
        var_2 = module_0.unfrack_path(str_0)
        str_1 = 'FC/G[ETQ'
        bytes_2 = None
        ansible_version_0 = module_0.AnsibleVersion(list_0, sorting_help_formatter_0, sorting_help_formatter_0)
        ansible_version_1 = module_0.AnsibleVersion(ansible_version_0, bool_0, bytes_0, ansible_version_0, set_0, prepend_list_action_0)
        unrecognized_argument_1 = module_0.UnrecognizedArgument(str_1, bytes_2, ansible_version_1, tuple_0, unrecognized_argument_0)
        var_3 = module_0.create_base_parser(prepend_list_action_0)
        prepend_list_action_1 = module_0.PrependListAction(tuple_0, tuple_0, str_0, prepend_list_action_0, bytes_1)
    except BaseException:
        pass

def test_case_18():
    try:
        var_0 = module_0.version()
        float_0 = 0.0001
        bytes_0 = b'\x932lnG\xe0\xafo\xdc'
        dict_0 = {bytes_0: var_0, float_0: float_0, var_0: float_0, var_0: bytes_0}
        bytes_1 = b'V\x0f\xdf\xc4\x89\xf9*\x8a\xd9N$\xf1v\x86P"r\x1d\x15\x11'
        argument_parser_0 = module_1.ArgumentParser(bytes_0, dict_0, bytes_1)
        var_1 = module_0.add_runtask_options(argument_parser_0)
        var_2 = module_0.add_check_options(float_0)
    except BaseException:
        pass

def test_case_19():
    try:
        var_0 = module_0.version()
        int_0 = 732
        str_0 = '}\x0c'
        set_0 = {int_0}
        int_1 = -780
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(int_1)
        tuple_0 = ()
        prepend_list_action_0 = module_0.PrependListAction(sorting_help_formatter_0, tuple_0, set_0)
        var_1 = sorting_help_formatter_0.add_arguments(tuple_0)
        bytes_0 = b'"\xd8\xbc\x9b\xfcm\x1f\xe7'
        var_2 = module_0.create_base_parser(prepend_list_action_0)
        prepend_list_action_1 = module_0.PrependListAction(tuple_0, tuple_0, str_0, prepend_list_action_0, bytes_0)
    except BaseException:
        pass

def test_case_20():
    try:
        float_0 = -4729.5
        dict_0 = {float_0: float_0}
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(dict_0)
        var_0 = module_0.add_vault_options(sorting_help_formatter_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'tf'
        float_0 = 0.5
        list_0 = []
        list_1 = [list_0]
        bool_0 = False
        unrecognized_argument_0 = module_0.UnrecognizedArgument(float_0, list_0, list_1, bool_0)
        str_1 = '?'
        dict_0 = {str_0: str_0, unrecognized_argument_0: float_0}
        float_1 = -1877.51
        ansible_version_0 = module_0.AnsibleVersion(unrecognized_argument_0, str_1, list_1, dict_0, float_1)
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(ansible_version_0)
        namespace_0 = module_1.Namespace()
        dict_1 = {str_1: unrecognized_argument_0}
        prepend_list_action_0 = module_0.PrependListAction(sorting_help_formatter_0, namespace_0, str_1, dict_0, dict_1, bool_0)
        sorting_help_formatter_1 = module_0.SortingHelpFormatter(unrecognized_argument_0, dict_1, dict_0)
    except BaseException:
        pass