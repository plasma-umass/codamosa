# Automatically generated by Pynguin.
import ansible.cli.arguments.option_helpers as module_0
import argparse as module_1

def test_case_0():
    var_0 = module_0.version()

def test_case_1():
    float_0 = -1055.389
    var_0 = module_0.maybe_unfrack_path(float_0)
    var_1 = module_0.version()

def test_case_2():
    str_0 = 'description'
    str_1 = 'epilog'
    var_0 = module_0.create_base_parser(str_1)
    var_1 = module_0.add_meta_options(var_0)

def test_case_3():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_inventory_options(argument_parser_0)

def test_case_4():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_vault_options(argument_parser_0)
    str_0 = '--vaufRlt-id'
    str_1 = 'secret'
    str_2 = 'another'
    str_3 = [str_0, str_1, str_0, str_2, str_2]
    var_1 = argument_parser_0.parse_args(str_3)

def test_case_5():
    var_0 = module_0.unfrack_path()

def test_case_6():
    str_0 = 'D'
    bytes_0 = b'\x1c\xbb\x8b\xb4\x8bS{0\x81\xf0u:\x81\xb5A+\xa0\x1b-'
    bool_0 = False
    unrecognized_argument_0 = module_0.UnrecognizedArgument(bool_0, str_0, bytes_0)
    list_0 = None
    dict_0 = {str_0: unrecognized_argument_0}
    ansible_version_0 = module_0.AnsibleVersion(unrecognized_argument_0, list_0, dict_0)
    dict_1 = {str_0: dict_0, str_0: bytes_0}
    prepend_list_action_0 = module_0.PrependListAction(dict_1, str_0, str_0)
    var_0 = prepend_list_action_0.__call__(unrecognized_argument_0, ansible_version_0, str_0)

def test_case_7():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_async_options(argument_parser_0)
    str_0 = '-P'
    str_1 = [str_0, str_0, str_0]
    var_1 = argument_parser_0.parse_args(str_1)

def test_case_8():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_output_options(argument_parser_0)
    str_0 = '-t'
    str_1 = 'test'
    str_2 = [str_0, str_1]
    var_1 = argument_parser_0.parse_args(str_2)

def test_case_9():
    str_0 = 'ansible'
    argument_parser_0 = module_1.ArgumentParser(str_0)
    var_0 = module_0.add_runas_prompt_options(argument_parser_0)
    str_1 = '--become-password-file'
    str_2 = '/home/xavierc/ansible/ansible_password'
    str_3 = '--become-method'
    str_4 = 'e'
    str_5 = '--become-user'
    str_6 = 'root'
    str_7 = [str_1, str_2, str_3, str_4, str_5, str_6]
    var_1 = argument_parser_0.parse_args(str_7)

def test_case_10():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_runas_options(argument_parser_0)

def test_case_11():
    argument_parser_0 = module_1.ArgumentParser()
    var_0 = module_0.add_subset_options(argument_parser_0)
    str_0 = '-t'
    str_1 = 'test1'
    str_2 = 'test2'
    str_3 = '--skip-tags'
    str_4 = 'skip1'
    str_5 = [str_0, str_1, str_0, str_2, str_3, str_4]
    var_1 = argument_parser_0.parse_args(str_5)