# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -152
    list_0 = [int_0]
    validation_result_0 = module_0.ValidationResult(list_0)

def test_case_2():
    str_0 = 'age'
    str_1 = {str_0: str_0}
    str_2 = {str_0: str_1, str_0: str_1}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_2)

def test_case_3():
    str_0 = '9x\rZ`?'
    dict_0 = {}
    list_0 = [dict_0, str_0, str_0]
    module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0, **dict_0)
    var_0 = module_argument_spec_validator_0.validate(dict_0)

def test_case_4():
    str_0 = 'name'
    str_1 = 'age'
    str_2 = {str_0: str_0}
    str_3 = 'int'
    str_4 = {str_3: str_3}
    str_5 = {str_0: str_2, str_1: str_4}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_5)
    var_0 = argument_spec_validator_0.validate(str_2)
    var_1 = var_0.error_messages
    var_2 = var_0.validated_parameters

def test_case_5():
    str_0 = 'name'
    str_1 = 'age'
    str_2 = 'type'
    str_3 = {str_2: str_0}
    str_4 = 'int'
    str_5 = {str_2: str_4}
    str_6 = {str_0: str_3, str_1: str_5}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_6)
    var_0 = argument_spec_validator_0.validate(str_3)
    var_1 = var_0.error_messages

def test_case_6():
    str_0 = '<'
    str_1 = {str_0: str_0}
    str_2 = {}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_2)
    var_0 = argument_spec_validator_0.validate(str_1)

def test_case_7():
    str_0 = 'test_param'
    str_1 = 'required'
    str_2 = 'type'
    str_3 = 'choices'
    bool_0 = True
    str_4 = [str_2]
    var_0 = {str_1: bool_0, str_2: str_4, str_3: str_4}
    var_1 = {str_0: var_0}
    str_5 = [str_0]
    str_6 = [str_5]
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_1, str_6)
    var_2 = {}
    var_3 = argument_spec_validator_0.validate(var_2)
    var_4 = var_3.error_messages