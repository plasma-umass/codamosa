# Automatically generated by Pynguin.
import ansible.playbook.base as module_0
import ansible.playbook.attribute as module_1

def test_case_0():
    pass

def test_case_1():
    base_0 = module_0.Base()

def test_case_2():
    field_attribute_base_0 = module_0.FieldAttributeBase()

def test_case_3():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()

def test_case_4():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()

def test_case_5():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()
    var_1 = field_attribute_base_0.get_loader()

def test_case_6():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()
    var_1 = field_attribute_base_0.get_variable_manager()

def test_case_7():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.validate()

def test_case_8():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()

def test_case_9():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()

def test_case_10():
    field_attribute_0 = module_1.FieldAttribute()
    field_attribute_base_0 = module_0.FieldAttributeBase()
    str_0 = 'value'
    var_0 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_0, str_0)

def test_case_11():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_attrs()

def test_case_12():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()

def test_case_13():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = {}
    var_1 = field_attribute_base_0.deserialize(var_0)

def test_case_14():
    base_0 = module_0.Base()
    var_0 = base_0.get_path()

def test_case_15():
    base_0 = module_0.Base()
    var_0 = base_0.get_search_path()

def test_case_16():
    bytes_0 = b'%\x9c\xe1\x00\xa2c/\xf7\x8d:c\xfe\xe52\x9f'
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.validate(bytes_0)

def test_case_17():
    dict_0 = {}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.load_data(dict_0)
    field_attribute_base_1 = module_0.FieldAttributeBase()
    base_0 = module_0.Base()
    var_1 = base_0.get_dep_chain()
    var_2 = field_attribute_base_1.serialize()
    var_3 = field_attribute_base_1.get_variable_manager()
    var_4 = field_attribute_base_0.dump_attrs()
    var_5 = field_attribute_base_0.validate()
    base_1 = module_0.Base()
    var_6 = base_1.get_search_path()
    field_attribute_base_2 = module_0.FieldAttributeBase()
    var_7 = field_attribute_base_2.get_loader()
    base_2 = module_0.Base()
    var_8 = base_0.get_dep_chain()

def test_case_18():
    field_attribute_0 = module_1.FieldAttribute()
    field_attribute_base_0 = module_0.FieldAttributeBase()
    bool_0 = True
    var_0 = field_attribute_base_0.copy()
    dict_0 = {field_attribute_base_0: bool_0, bool_0: field_attribute_0, bool_0: field_attribute_base_0, field_attribute_base_0: field_attribute_base_0}
    base_0 = module_0.Base()
    var_1 = base_0.get_path()
    var_2 = field_attribute_base_0.deserialize(dict_0)
    var_3 = field_attribute_base_0.serialize()
    var_4 = field_attribute_base_0.dump_me()
    str_0 = '\\R4t":R%q!?J'
    base_1 = module_0.Base()
    var_5 = base_1.get_path()
    var_6 = None
    var_7 = field_attribute_base_0.from_attrs(dict_0)
    var_8 = field_attribute_base_0.squash()
    var_9 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_0, var_6)

def test_case_19():
    dict_0 = {}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_variable_manager()
    var_1 = field_attribute_base_0.from_attrs(dict_0)

def test_case_20():
    str_0 = 'X;QwTo$DK!2?^,>l4Cq*'
    str_1 = 'f0tc~26k//'
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.from_attrs(dict_0)