# Automatically generated by Pynguin.
import ansible.playbook.base as module_0
import ansible.playbook.attribute as module_1

def test_case_0():
    pass

def test_case_1():
    base_0 = module_0.Base()

def test_case_2():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()

def test_case_3():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()

def test_case_4():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    set_0 = set()
    str_0 = '"aeU(\x0bt4l .sG\t{AwZ\''
    dict_0 = {str_0: field_attribute_base_0, str_0: field_attribute_base_0}
    field_attribute_base_2 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_2.load_data(set_0, dict_0)
    var_1 = field_attribute_base_0.get_loader()

def test_case_5():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.validate()

def test_case_6():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()

def test_case_7():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()

def test_case_8():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()

def test_case_9():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    str_0 = 'test_attr'
    field_attribute_0 = module_1.FieldAttribute()
    str_1 = {str_0: str_0}
    var_0 = field_attribute_base_0.from_attrs(str_1)

def test_case_10():
    base_0 = module_0.Base()
    var_0 = base_0.get_search_path()

def test_case_11():
    base_0 = module_0.Base()
    float_0 = -1928.535283
    var_0 = base_0.validate(float_0)

def test_case_12():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()
    var_1 = field_attribute_base_0.get_ds()
    var_2 = field_attribute_base_0.validate(field_attribute_base_0)
    dict_0 = {}
    var_3 = field_attribute_base_0.load_data(dict_0)

def test_case_13():
    base_0 = module_0.Base()
    var_0 = base_0.validate()
    str_0 = '5'
    field_attribute_base_0 = module_0.FieldAttributeBase()
    list_0 = []
    base_meta_0 = None
    field_attribute_0 = module_1.FieldAttribute(base_meta_0, str_0)
    var_1 = field_attribute_base_0.load_data(list_0, field_attribute_0)

def test_case_14():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()
    set_0 = None
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_1.squash()
    var_2 = field_attribute_base_1.squash()
    str_0 = '\x0b'
    var_3 = field_attribute_base_0.copy()
    bytes_0 = b'\x84\xad\xff\x08\x90\xc6o\x90\xfa\xc4|\xf9\xe1eg\\\xdc'
    dict_0 = {str_0: field_attribute_base_1, str_0: var_0, str_0: set_0}
    int_0 = None
    base_0 = module_0.Base()
    var_4 = field_attribute_base_1.validate(base_0)
    field_attribute_0 = module_1.FieldAttribute(str_0, bytes_0, dict_0, int_0)
    str_1 = None
    field_attribute_base_2 = module_0.FieldAttributeBase()
    var_5 = field_attribute_base_2.copy()
    var_6 = field_attribute_base_2.get_validated_value(set_0, field_attribute_0, str_1, bytes_0)

def test_case_15():
    base_0 = module_0.Base()
    var_0 = base_0.validate()