# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    try:
        complex_0 = None
        list_0 = [complex_0]
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Unexpected gpg output'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        int_0 = 2870
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator()
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = {}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_0)
        list_0 = []
        var_1 = argument_spec_validator_0.validate(list_0, *list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'test_pvram_CnXe'
        str_1 = 'parar_two'
        str_2 = {str_0: str_1}
        str_3 = {str_0: str_0, str_1: str_2}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_3)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = {}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_0)
        var_1 = {argument_spec_validator_0: var_0, argument_spec_validator_0: var_0}
        var_2 = argument_spec_validator_0.validate(var_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'name'
        str_1 = 'type'
        str_2 = {str_1: str_0}
        str_3 = {str_0: str_2}
        str_4 = 'full_name'
        str_5 = [str_0, str_4, str_2]
        str_6 = [str_5]
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_3, str_6)
        str_7 = {str_0: str_5, str_4: str_5}
        var_0 = argument_spec_validator_0.validate(str_7)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'name'
        str_1 = 'age'
        str_2 = 'type'
        str_3 = 'str'
        str_4 = {str_2: str_3}
        str_5 = 'int'
        str_6 = {str_2: str_5}
        str_7 = {str_0: str_4, str_1: str_6}
        str_8 = 'bo'
        str_9 = '42'
        str_10 = {str_0: str_8, str_1: str_9}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_7)
        var_0 = argument_spec_validator_0.validate(str_10)
        var_1 = var_0.error_messages
        var_2 = Exception(str_3)
        var_3 = var_0.validated_
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = {}
        int_0 = 22
        list_0 = [str_0]
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
        var_0 = module_argument_spec_validator_0.validate(int_0)
    except BaseException:
        pass