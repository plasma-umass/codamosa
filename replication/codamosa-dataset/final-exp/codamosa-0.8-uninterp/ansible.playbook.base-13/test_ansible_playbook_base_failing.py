# Automatically generated by Pynguin.
import ansible.playbook.base as module_0
import ansible.playbook.attribute as module_1

def test_case_0():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.serialize()
        base_0 = None
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.load_data(base_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.dump_attrs()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.get_variable_manager()
        set_0 = {field_attribute_base_1, field_attribute_base_1, var_1, field_attribute_base_1}
        var_2 = field_attribute_base_1.squash()
        var_3 = field_attribute_base_1.load_data(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        bytes_0 = b'O\xa0(\xf6\xb5\xd5\x07\xae\x8ev\x00\xba\xb2B\xf4\x08\x80\xfar'
        var_0 = field_attribute_base_0.load_data(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        str_0 = 'string value'
        field_attribute_0 = module_1.FieldAttribute()
        var_0 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_0, field_attribute_0)
        var_1 = int(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.copy()
        var_2 = field_attribute_base_1.dump_attrs()
        var_3 = field_attribute_base_1.get_ds()
        str_0 = '{y&p48jIHg?Rt"'
        set_0 = {field_attribute_base_1, str_0}
        tuple_0 = (str_0, set_0)
        var_4 = field_attribute_base_0.post_validate(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        var_1 = field_attribute_base_0.deserialize(field_attribute_base_0)
    except BaseException:
        pass

def test_case_6():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        var_1 = field_attribute_base_0.get_loader()
        list_0 = []
        var_2 = field_attribute_base_0.dump_me(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        field_attribute_0 = module_1.FieldAttribute()
        str_0 = '5'
        tuple_0 = ()
        var_0 = field_attribute_base_0.load_data(tuple_0)
        var_1 = field_attribute_base_0.serialize()
        var_2 = int(str_0)
        var_3 = field_attribute_base_0.squash()
        base_0 = module_0.Base()
        var_4 = base_0.get_search_path()
        var_5 = field_attribute_base_0.get_loader()
        str_1 = "N8SEUm4'x/+#$+PIg"
        var_6 = field_attribute_base_0.load_data(str_1, field_attribute_0, field_attribute_base_0)
    except BaseException:
        pass

def test_case_8():
    try:
        base_0 = module_0.Base()
        var_0 = base_0.get_path()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_0.dump_attrs()
        bool_0 = True
        var_2 = field_attribute_base_0.preprocess_data(bool_0)
        set_0 = set()
        var_3 = field_attribute_base_0.get_loader()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_4 = field_attribute_base_1.load_data(set_0)
        var_5 = field_attribute_base_1.copy()
        var_6 = field_attribute_base_0.from_attrs(field_attribute_base_1)
    except BaseException:
        pass