# Automatically generated by Pynguin.
import ansible.cli.arguments.option_helpers as module_0
import operator as module_1

def test_case_0():
    try:
        var_0 = module_0.version()
        bytes_0 = b',\xf7\xf4'
        str_0 = "?WJB,vesmf'Do)"
        unrecognized_argument_0 = module_0.UnrecognizedArgument(bytes_0, bytes_0, str_0)
        var_1 = module_0.version()
        list_0 = [var_0, var_0, var_0]
        var_2 = module_0.add_runtask_options(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x1ap8?\xd7B\x16%\xeb\xef\x18I,Rz\x8aO \xcf'
        int_0 = -3019
        str_0 = 'Fud]'
        list_0 = [int_0]
        set_0 = set()
        prepend_list_action_0 = module_0.PrependListAction(bytes_0, str_0, list_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        str_0 = "Z$['"
        var_0 = module_0.ensure_value(tuple_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.version()
        int_0 = -352
        set_0 = set()
        var_1 = module_0.ensure_value(int_0, set_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 60.0
        var_0 = module_0.add_verbosity_options(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Q\nJ|_fQE'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.add_async_options(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = None
        var_0 = module_0.add_check_options(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = None
        var_0 = module_0.add_fork_options(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = module_0.version()
        int_0 = 2709
        var_1 = module_0.add_inventory_options(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = module_0.version()
        list_0 = [var_0, var_0, var_0]
        attrgetter_0 = module_1.attrgetter(*list_0)
        var_1 = module_0.add_meta_options(attrgetter_0)
    except BaseException:
        pass

def test_case_10():
    try:
        var_0 = module_0.version()
        bytes_0 = b'e\xcf\xfb)/\xde/\x96W\x90\xef\xccy\x84\xf4\xdf\x04u\x08'
        var_1 = module_0.add_module_options(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = 60.0
        var_0 = module_0.add_runas_options(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = module_0.version()
        float_0 = -1413.2993269196143
        var_1 = module_0.add_runas_prompt_options(float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        var_0 = module_0.version()
        list_0 = [var_0, var_0, var_0]
        var_1 = module_0.add_runtask_options(list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        var_0 = module_0.version()
        bytes_0 = b')\xfft@\xe2~W'
        dict_0 = None
        set_0 = {var_0, bytes_0, dict_0}
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(set_0)
        var_1 = module_0.add_tasknoplay_options(sorting_help_formatter_0)
    except BaseException:
        pass

def test_case_15():
    try:
        var_0 = module_0.version()
        bool_0 = True
        var_1 = module_0.add_subset_options(bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        var_0 = module_0.unfrack_path()
        int_0 = -2106
        bool_0 = True
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(int_0, bool_0)
        int_1 = 1450
        var_1 = sorting_help_formatter_0.add_arguments(int_1)
    except BaseException:
        pass

def test_case_17():
    try:
        complex_0 = None
        float_0 = 3021.520481543491
        str_0 = 'xG&7wc-"}m'
        var_0 = module_0.version(str_0)
        var_1 = module_0.create_base_parser(complex_0, float_0)
        dict_0 = {complex_0: complex_0, float_0: complex_0}
        set_0 = None
        var_2 = module_0.maybe_unfrack_path(set_0)
        bool_0 = False
        unrecognized_argument_0 = module_0.UnrecognizedArgument(bool_0, float_0)
        ansible_version_0 = None
        str_1 = 'RBt%8AhU\x0b{;c2lvL'
        var_3 = unrecognized_argument_0.__call__(ansible_version_0, dict_0, ansible_version_0, str_1)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'xG&7wc-"}m'
        var_0 = module_0.version(str_0)
        set_0 = set()
        bool_0 = False
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(set_0, bool_0)
        float_0 = -1420.4575
        prepend_list_action_0 = None
        tuple_0 = (float_0,)
        ansible_version_0 = module_0.AnsibleVersion(prepend_list_action_0, tuple_0)
        unrecognized_argument_0 = module_0.UnrecognizedArgument(prepend_list_action_0, ansible_version_0)
        list_0 = None
        prepend_list_action_1 = module_0.PrependListAction(unrecognized_argument_0, list_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'xG&7wc-"}m'
        var_0 = module_0.version(str_0)
        int_0 = -335
        set_0 = set()
        list_0 = [int_0, int_0]
        var_1 = module_0.add_runas_prompt_options(set_0, list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        var_0 = module_0.version()
        str_0 = 'H\t +'
        str_1 = 'h\tA8IH&](P,]Y"'
        int_0 = 509
        sorting_help_formatter_0 = None
        set_0 = {str_0, sorting_help_formatter_0}
        ansible_version_0 = module_0.AnsibleVersion(str_0, str_1, int_0, set_0, sorting_help_formatter_0)
        sorting_help_formatter_1 = module_0.SortingHelpFormatter(ansible_version_0)
        var_1 = module_0.add_runtask_options(sorting_help_formatter_1)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'xG&7wc-"}m'
        var_0 = module_0.version(str_0)
        str_1 = ';\r/kn#P'
        float_0 = None
        sorting_help_formatter_0 = module_0.SortingHelpFormatter(float_0)
        list_0 = []
        var_1 = sorting_help_formatter_0.add_arguments(list_0)
        bool_0 = False
        set_0 = None
        prepend_list_action_0 = module_0.PrependListAction(bool_0, set_0, str_1, sorting_help_formatter_0)
    except BaseException:
        pass