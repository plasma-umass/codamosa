# Automatically generated by Pynguin.
import ansible.module_utils.common.arg_spec as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = 210.19
    validation_result_0 = module_0.ValidationResult(float_0)

def test_case_2():
    str_0 = 'type'
    str_1 = {str_0: str_0}
    str_2 = {str_0: str_1}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_2)

def test_case_3():
    var_0 = {}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_0)
    var_1 = {}
    var_2 = argument_spec_validator_0.validate(var_1)

def test_case_4():
    bytes_0 = b'n\x9d\x00\xc3\x0b\xb4\xdaD'
    validation_result_0 = module_0.ValidationResult(bytes_0)
    dict_0 = {}
    dict_1 = {}
    list_0 = [validation_result_0, bytes_0, dict_0, validation_result_0, dict_0]
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, dict_1, list_0)
    var_0 = argument_spec_validator_0.validate(dict_1, **dict_0)

def test_case_5():
    str_0 = 'test'
    str_1 = 'str'
    str_2 = {str_1: str_1}
    str_3 = {str_0: str_2}
    str_4 = 'string'
    str_5 = {str_0: str_4}
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_3)
    var_0 = argument_spec_validator_0.validate(str_5)
    var_1 = var_0.errors
    var_2 = var_0.error_messages
    var_3 = var_0.validated_parameters

def test_case_6():
    str_0 = 'name'
    str_1 = 'age'
    str_2 = 'occupation'
    str_3 = 'type'
    str_4 = 'str'
    str_5 = {str_3: str_4}
    str_6 = 'int'
    str_7 = {str_3: str_6}
    bool_0 = True
    var_0 = {str_3: str_3, str_4: bool_0}
    var_1 = {str_0: str_5, str_1: str_7, str_2: var_0}
    str_8 = [str_0, str_1]
    str_9 = [str_8]
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_1, str_9)
    str_10 = 'Alice'
    int_0 = 42
    var_2 = {str_0: str_10, str_1: int_0}
    var_3 = argument_spec_validator_0.validate(var_2)

def test_case_7():
    str_0 = 'age'
    str_1 = 'occupbtion'
    str_2 = 'EOPNOTSUPP'
    str_3 = {str_0: str_2}
    str_4 = 'int'
    str_5 = {str_4: str_4}
    str_6 = 'required'
    bool_0 = True
    var_0 = {str_2: str_2, str_6: bool_0}
    var_1 = {str_4: str_3, str_0: str_5, str_1: var_0}
    str_7 = [str_6]
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_1, str_7)
    str_8 = {str_1: str_7}
    var_2 = argument_spec_validator_0.validate(str_8)
    str_9 = 'le'
    int_0 = 42
    var_3 = {str_4: str_9, str_0: int_0}
    var_4 = argument_spec_validator_0.validate(var_3)

def test_case_8():
    bytes_0 = b'n\x9d\x00\xc3\x0b\xb4\xdaD'
    list_0 = [bytes_0]
    validation_result_0 = module_0.ValidationResult(list_0)
    dict_0 = {}
    dict_1 = {}
    list_1 = [bytes_0, dict_0, dict_1, dict_0]
    argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, dict_1, list_1)
    list_2 = [validation_result_0, bytes_0]
    var_0 = argument_spec_validator_0.validate(dict_1, *list_2)
    list_3 = module_1.list()
    str_0 = 'v\x0c nL@'
    dict_2 = {str_0: list_3, str_0: var_0, str_0: dict_0}
    var_1 = argument_spec_validator_0.validate(dict_2, **dict_2)

def test_case_9():
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
    var_2 = var_0.unsupported_parameters
    var_3 = set()
    var_4 = var_0.validated_parameters