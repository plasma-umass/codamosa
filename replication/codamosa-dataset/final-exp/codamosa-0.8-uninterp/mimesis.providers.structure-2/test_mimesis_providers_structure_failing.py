# Automatically generated by Pynguin.
import mimesis.providers.structure as module_0

def test_case_0():
    try:
        structure_0 = module_0.Structure()
        str_0 = 'accesskTey'
        str_1 = structure_0.html_attribute_value(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        structure_0 = module_0.Structure(**dict_0)
        list_0 = [structure_0, dict_0]
        str_0 = structure_0.html_attribute_value()
        structure_1 = module_0.Structure(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        structure_0 = module_0.Structure()
        list_0 = [structure_0, structure_0, structure_0, structure_0]
        str_0 = "K0L?22W{8?;?='1mS"
        str_1 = structure_0.html_attribute_value(list_0, str_0)
    except BaseException:
        pass