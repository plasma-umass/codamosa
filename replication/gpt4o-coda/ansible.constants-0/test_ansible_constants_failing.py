# Automatically generated by Pynguin.
import ansible.constants as module_0

def test_case_0():
    try:
        int_0 = -1393
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(int_0, int_0, int_0)
        var_0 = deprecated_sequence_constant_0.__len__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 999999999999
        str_0 = "do the fact collection\n\n        'collected_facts' is a object (a dict, likely) that holds all previously\n          facts. This is intended to be used if a FactCollector needs to reference\n          another fact (for ex, the system arch) and should not be modified (usually).\n\n          Returns a dict of facts.\n\n          "
        set_0 = {str_0, str_0, str_0, str_0}
        int_1 = -1703
        bytes_0 = b'\xf1=\x87\x83\xb9Us\xa9\xee\xa00\xdd\xbc'
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(set_0, int_1, bytes_0)
        int_2 = -3699
        deprecated_sequence_constant_1 = module_0._DeprecatedSequenceConstant(deprecated_sequence_constant_0, int_2, deprecated_sequence_constant_0)
        var_0 = deprecated_sequence_constant_1.__getitem__(int_0)
    except BaseException:
        pass