# Automatically generated by Pynguin.
import sanic.blueprint_group as module_0
import sanic.blueprints as module_1

def test_case_0():
    str_0 = '<FSB1}'
    blueprint_group_0 = module_0.BlueprintGroup(str_0)

def test_case_1():
    bytes_0 = None
    blueprint_group_0 = module_0.BlueprintGroup(bytes_0)
    int_0 = 71
    str_0 = ''
    blueprint_0 = module_1.Blueprint(str_0)
    blueprint_group_0.insert(int_0, blueprint_0)

def test_case_2():
    bytes_0 = b'0\x1bR\xd4\xee'
    blueprint_group_0 = module_0.BlueprintGroup(bytes_0)
    var_0 = blueprint_group_0.__iter__()
    blueprint_group_1 = module_0.BlueprintGroup()

def test_case_3():
    str_0 = '{e$yBX#|Qcht.U}H'
    str_1 = '\\^44M'
    bool_0 = True
    str_2 = '#'
    int_0 = 411
    blueprint_group_0 = module_0.BlueprintGroup(int_0)
    dict_0 = {str_0: str_0, str_1: str_0, str_0: bool_0, str_2: blueprint_group_0}
    bytes_0 = b',(O`\xf5Q\xa7\xf0\xdb1\xe3'
    blueprint_group_1 = module_0.BlueprintGroup(dict_0, bytes_0)
    var_0 = blueprint_group_1.__iter__()
    blueprint_group_2 = module_0.BlueprintGroup()
    int_1 = blueprint_group_2.__len__()

def test_case_4():
    str_0 = '8W%+"pc!|\twa}"}Mq'
    str_1 = 'A\t[i$Qtq`S;xf$fKUi'
    str_2 = '`r\tg_e& EiC9 r&6cX'
    blueprint_0 = module_1.Blueprint(str_1, str_2, str_1)
    str_3 = '\n        Read some bytes of request body.\n        '
    str_4 = '\x0blDUg!CDF'
    blueprint_group_0 = module_0.BlueprintGroup(blueprint_0)
    var_0 = blueprint_group_0.middleware()
    dict_0 = {str_4: str_1, str_1: str_0}
    blueprint_group_1 = module_0.BlueprintGroup(str_3, dict_0)
    blueprint_group_1.append(blueprint_0)
    int_0 = -531
    blueprint_group_1.insert(int_0, blueprint_0)
    blueprint_group_2 = module_0.BlueprintGroup()
    var_1 = blueprint_group_1.__iter__()

def test_case_5():
    int_0 = -2
    blueprint_group_0 = module_0.BlueprintGroup(int_0)
    tuple_0 = (blueprint_group_0,)
    list_0 = [tuple_0, tuple_0, int_0, blueprint_group_0]
    dict_0 = {blueprint_group_0: list_0}
    list_1 = [dict_0, int_0, blueprint_group_0]
    blueprint_group_1 = module_0.BlueprintGroup()
    var_0 = blueprint_group_1.middleware(*list_1)

def test_case_6():
    str_0 = '\n        Same as :func:`sanic.Sanic.url_for`, but automatically determine\n        `scheme` and `netloc` base on the request. Since this method is aiming\n        to generate correct schema & netloc, `_external` is implied.\n\n        :param kwargs: takes same parameters as in :func:`sanic.Sanic.url_for`\n        :return: an absolute url to the given view\n        :rtype: str\n        '
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    int_0 = -152
    bytes_0 = b'R\x8f\x87\x02\x0bO\x85\xc0\x05\xf3\xdf\r+\x1f\xa1_iO9y'
    blueprint_group_0 = module_0.BlueprintGroup(int_0, bytes_0)
    var_0 = blueprint_group_0.middleware()
    tuple_0 = ()
    dict_1 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    blueprint_group_1 = module_0.BlueprintGroup(dict_1)
    var_1 = blueprint_group_1.middleware(**dict_0)

def test_case_7():
    str_0 = '8W%+"pc!|\twa}"}Mq'
    float_0 = 1.0
    str_1 = '\x0b\x0binjn;'
    dict_0 = {str_1: float_0, float_0: str_1}
    blueprint_group_0 = module_0.BlueprintGroup(dict_0)
    str_2 = 'A\t[i$Qtq`S;xf$fKUi'
    str_3 = '`#r\tg_e& EiC9 r&6cX'
    blueprint_0 = module_1.Blueprint(str_2, str_3, str_2)
    str_4 = '\n        Read some bytes of request body.\n        '
    str_5 = '\x0blDUg!CDF'
    blueprint_group_1 = module_0.BlueprintGroup(blueprint_0)
    var_0 = blueprint_group_1.middleware()
    int_0 = blueprint_group_1.__len__()
    dict_1 = {str_5: str_2, str_2: str_0}
    blueprint_group_2 = module_0.BlueprintGroup(str_4, dict_1)
    blueprint_group_2.append(blueprint_0)
    var_1 = blueprint_group_0.middleware()
    var_2 = blueprint_group_0.middleware()
    blueprint_group_3 = module_0.BlueprintGroup(blueprint_0, int_0)
    list_0 = [var_2, blueprint_group_3, int_0]
    var_3 = blueprint_group_1.middleware(*list_0)
    blueprint_group_2.insert(int_0, blueprint_0)