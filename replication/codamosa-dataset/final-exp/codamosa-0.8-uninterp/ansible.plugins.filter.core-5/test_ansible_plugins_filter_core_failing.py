# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0
import ansible.template as module_1

def test_case_0():
    try:
        bytes_0 = b's\x05:('
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        var_0 = module_0.to_nice_yaml(bytes_0, filter_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 13
        list_0 = [int_0]
        var_0 = module_0.to_nice_yaml(list_0, *list_0)
        var_1 = module_0.combine(*list_0)
        str_0 = '3~X!+LWkeisQ0'
        str_1 = 'q&LxOLy5=*=I#'
        dict_0 = {str_0: list_0, str_1: str_1, str_1: list_0}
        var_2 = module_0.regex_search(dict_0, list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        var_0 = module_0.combine()
        str_0 = '{'
        bool_0 = True
        dict_1 = {str_0: str_0}
        list_0 = [dict_0, bool_0]
        str_1 = 'XOh#'
        var_1 = module_0.to_json(str_1)
        var_2 = module_0.to_uuid(list_0)
        var_3 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        set_0 = {list_0, list_0}
        dict_0 = {}
        var_0 = module_0.regex_replace(dict_0)
        str_0 = 'sB&b=Yo oWQQ)f'
        str_1 = '<FDI'
        str_2 = "6y\\IZGoKw?`U.'\n-y"
        str_3 = 'NGAq`tF&OhvXp='
        dict_1 = {str_0: list_0, str_1: set_0, str_2: str_1, str_3: str_0}
        var_1 = module_0.randomize_list(set_0, dict_1)
        str_4 = 'Lmy\x0b<e](3_5'
        str_5 = '\x0b!7 ?'
        ansible_undefined_0 = module_1.AnsibleUndefined()
        async_iterator_0 = ansible_undefined_0.__aiter__()
        str_6 = 'w3p)E":p="OFA'
        str_7 = "!<6v:3^-p&'eZc[Ggi"
        dict_2 = {str_6: str_4, str_5: str_7}
        var_2 = module_0.to_nice_json(async_iterator_0, **dict_2)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        list_0 = [bool_0]
        var_0 = module_0.to_datetime(bool_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '{'
        bool_0 = True
        var_0 = module_0.quote(dict_0)
        dict_1 = {str_0: str_0}
        list_0 = [dict_0, bool_0]
        var_1 = module_0.to_uuid(list_0)
        var_2 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'cN-Db\x0b2,_D.Bb0Y'
        dict_0 = {str_0: str_0}
        float_0 = 2237.502763
        var_0 = module_0.rand(dict_0, str_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        filter_module_0 = module_0.FilterModule()
        list_0 = None
        set_0 = set()
        var_0 = module_0.rand(filter_module_0, list_0, set_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '{'
        bool_0 = True
        dict_1 = {str_0: str_0}
        str_1 = 'w~'
        var_0 = module_0.randomize_list(str_1)
        list_0 = [dict_0, bool_0]
        var_1 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'C<hj?`C$W%A!"J*${0L'
        ansible_undefined_0 = module_1.AnsibleUndefined()
        var_0 = module_0.get_hash(str_0, ansible_undefined_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'enabled'
        set_0 = {str_0}
        list_0 = []
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
        var_1 = module_0.get_encrypted_password(set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        set_0 = None
        list_0 = [dict_0, dict_0, set_0, set_0]
        var_0 = module_0.combine(*list_0)
        list_1 = [dict_0]
        bytes_0 = b'\xa2\x18\xe3\x88\x08'
        var_1 = module_0.to_uuid(list_1, bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        tuple_0 = None
        var_0 = module_0.to_uuid(tuple_0)
        int_0 = 2141
        int_1 = -629
        var_1 = module_0.to_uuid(int_0, int_1)
    except BaseException:
        pass

def test_case_13():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '{'
        bool_0 = True
        dict_1 = {str_0: str_0}
        list_0 = [dict_0, bool_0]
        var_0 = module_0.to_uuid(list_0)
        var_1 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 3031
        list_0 = [int_0, int_0, int_0]
        str_0 = ''
        var_0 = module_0.extract(list_0, str_0, str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '6'
        var_0 = module_0.b64decode(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        dict_0 = {}
        set_0 = None
        var_0 = module_0.subelements(dict_0, set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 13
        list_0 = [int_0]
        str_0 = 'JO%w=!\x0bB@c!\x0crsg,&!>J'
        var_0 = module_0.subelements(list_0, str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = {}
        set_0 = None
        list_0 = [dict_0, set_0, set_0, dict_0]
        var_0 = module_0.combine(*list_0)
        str_0 = '!\'ssXmy-R"[],jy\x0b,5Z'
        var_1 = module_0.subelements(str_0, set_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '|'
        list_0 = [str_0, str_0, str_0, str_0]
        tuple_0 = (str_0, list_0, str_0)
        bool_0 = True
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_20():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.combine()
        str_0 = ''
        var_1 = module_0.regex_search(str_0, str_0)
        var_2 = module_0.list_of_dict_key_value_elements_to_dict(filter_module_0)
    except BaseException:
        pass

def test_case_21():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.path_join(filter_module_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'Q6xN$J%_FHmc&'
        set_0 = {str_0, str_0}
        var_0 = module_0.quote(set_0)
        tuple_0 = (str_0,)
        var_1 = module_0.path_join(tuple_0)
        bytes_0 = b'\x8b^\x8f\xc0\x88\xac'
        float_0 = 2.0
        tuple_1 = (float_0,)
        var_2 = module_0.randomize_list(bytes_0, tuple_1)
        bool_0 = False
        filter_module_0 = module_0.FilterModule()
        var_3 = module_0.to_uuid(filter_module_0)
        var_4 = module_0.to_uuid(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_23():
    try:
        filter_module_0 = module_0.FilterModule()
        filter_module_1 = module_0.FilterModule()
        var_0 = filter_module_1.filters()
        bool_0 = False
        int_0 = None
        var_1 = module_0.strftime(bool_0, int_0)
    except BaseException:
        pass

def test_case_24():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '{'
        bool_0 = True
        tuple_0 = ()
        list_0 = None
        var_0 = module_0.ternary(tuple_0, str_0, list_0)
        dict_1 = {str_0: str_0}
        list_1 = [dict_0, bool_0]
        var_1 = module_0.subelements(list_1, str_0, dict_1)
    except BaseException:
        pass

def test_case_25():
    try:
        float_0 = 1000.0
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.regex_replace(filter_module_0)
        var_1 = filter_module_0.filters()
        list_0 = [float_0, var_0]
        var_2 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = ").Y\r13h\x0b;'//\n!4.H"
        str_1 = '#'
        dict_0 = {str_0: str_0, str_1: str_0}
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0)
        str_2 = ';W$e2'
        var_1 = module_0.to_bool(str_2)
        float_0 = 0.0
        bytes_0 = b'O}\xee\xa3\xdb\x16\x82\xcd\x97\x187\xa7\x8e'
        int_0 = 379
        var_2 = module_0.subelements(float_0, bytes_0, int_0)
    except BaseException:
        pass

def test_case_27():
    try:
        bool_0 = False
        int_0 = 736
        str_0 = 'V"'
        var_0 = module_0.rand(int_0, bool_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_28():
    try:
        complex_0 = None
        var_0 = module_0.strftime(complex_0)
    except BaseException:
        pass

def test_case_29():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.randomize_list(filter_module_0)
        str_0 = 'Tx'
        str_1 = 'l(;.S[8\x0bf,\r:$4@Lxx'
        str_2 = '/var/run/yum.pid'
        dict_0 = {str_1: str_1}
        var_1 = module_0.to_bool(dict_0)
        list_0 = [str_2, var_0, str_0]
        tuple_0 = ()
        var_2 = module_0.do_groupby(str_2, list_0, tuple_0)
    except BaseException:
        pass

def test_case_30():
    try:
        float_0 = 2237.502763
        int_0 = 736
        str_0 = 'V"'
        complex_0 = None
        dict_0 = {int_0: str_0, complex_0: float_0}
        var_0 = module_0.rand(dict_0, int_0, str_0)
    except BaseException:
        pass

def test_case_31():
    try:
        bytes_0 = b''
        list_0 = [bytes_0]
        bool_0 = False
        tuple_0 = (list_0, bool_0, bool_0)
        int_0 = None
        var_0 = module_0.flatten(tuple_0, int_0)
        list_1 = []
        str_0 = 'USI&Yr-<`)`Wi'
        dict_0 = {str_0: str_0, str_0: bytes_0}
        var_1 = module_0.combine(*list_1, **dict_0)
    except BaseException:
        pass

def test_case_32():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.to_yaml(filter_module_0)
    except BaseException:
        pass

def test_case_33():
    try:
        list_0 = None
        tuple_0 = None
        var_0 = module_0.to_uuid(tuple_0)
        bytes_0 = b']\xfeT=7\x06\x8cq\x08)zM\x1c\x0e\xa4\xf3N'
        var_1 = module_0.fileglob(bytes_0)
        str_0 = 'd5(51{ :c'
        dict_0 = {str_0: list_0}
        var_2 = module_0.to_yaml(str_0)
        var_3 = module_0.subelements(dict_0, str_0)
    except BaseException:
        pass

def test_case_34():
    try:
        int_0 = 0
        list_0 = [int_0, int_0, int_0, int_0]
        var_0 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = "1]4w\x0c'"
        var_0 = module_0.strftime(str_0, str_0)
    except BaseException:
        pass

def test_case_36():
    try:
        int_0 = 2069
        str_0 = ''
        filter_module_0 = None
        var_0 = module_0.regex_findall(int_0, str_0, filter_module_0)
        filter_module_1 = module_0.FilterModule()
        int_1 = 3
        var_1 = filter_module_1.filters()
        var_2 = module_0.to_bool(int_1)
        str_1 = None
        bool_0 = True
        var_3 = filter_module_1.filters()
        dict_0 = {str_1: bool_0, str_1: str_1, str_1: bool_0, str_1: str_1}
        var_4 = module_0.to_nice_yaml(dict_0)
        list_0 = []
        bool_1 = False
        var_5 = module_0.subelements(int_0, list_0, bool_1)
    except BaseException:
        pass

def test_case_37():
    try:
        dict_0 = {}
        set_0 = None
        list_0 = [dict_0, dict_0, dict_0, set_0]
        filter_module_0 = module_0.FilterModule()
        list_1 = [filter_module_0]
        var_0 = module_0.ternary(list_0, filter_module_0, list_1)
        list_2 = [dict_0, dict_0, set_0, set_0]
        var_1 = module_0.combine(*list_2)
        bytes_0 = b'\xcc\x072asjMV\x9aqwg'
        var_2 = module_0.subelements(bytes_0, list_2)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'cN-Db\x0b2,_D.Bb0Y'
        dict_0 = {str_0: str_0}
        filter_module_0 = module_0.FilterModule()
        str_1 = None
        str_2 = "xP[R,]olZk\x0b~=Rj'("
        int_0 = -2294
        tuple_0 = (str_1, str_2, filter_module_0, int_0)
        float_0 = None
        var_0 = module_0.rand(filter_module_0, tuple_0, float_0)
        var_1 = module_0.strftime(dict_0)
    except BaseException:
        pass

def test_case_39():
    try:
        int_0 = 2044
        str_0 = ''
        filter_module_0 = None
        var_0 = module_0.regex_findall(int_0, str_0, filter_module_0)
        filter_module_1 = module_0.FilterModule()
        int_1 = 3
        var_1 = filter_module_1.filters()
        var_2 = module_0.to_bool(int_1)
        str_1 = None
        bool_0 = True
        var_3 = filter_module_1.filters()
        str_2 = '^9cVa!{d2WP&'
        dict_0 = {str_1: bool_0, str_1: str_1, str_1: bool_0, str_2: str_1}
        var_4 = module_0.to_nice_yaml(dict_0)
        str_3 = 'k0u{]\x0c?\ta\x0b8i OnSu'
        float_0 = -1523.5
        list_0 = []
        var_5 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
        var_6 = filter_module_1.filters()
        var_7 = module_0.get_encrypted_password(filter_module_1, str_3, float_0)
    except BaseException:
        pass

def test_case_40():
    try:
        int_0 = -36
        str_0 = 'abcd'
        var_0 = module_0.regex_replace(str_0, str_0, str_0)
        var_1 = module_0.regex_replace(str_0, str_0, str_0)
        str_1 = ')C-Yoyf@=C}>fS$iM'
        str_2 = '|K)C(u+u?X}30)qN=p'
        var_2 = module_0.from_yaml_all(str_2)
        str_3 = '1]4w'
        var_3 = module_0.combine()
        var_4 = module_0.comment(str_3)
        list_0 = [str_1]
        list_1 = [list_0]
        var_5 = module_0.randomize_list(int_0)
        var_6 = module_0.strftime(list_0, list_1)
    except BaseException:
        pass

def test_case_41():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '}'
        complex_0 = None
        bool_0 = True
        var_0 = module_0.mandatory(dict_0, bool_0)
        str_1 = '\\\r|k(JSl6~dx'
        dict_1 = {str_1: str_0}
        tuple_0 = (dict_1, dict_0, dict_0)
        var_1 = filter_module_0.filters()
        list_0 = [tuple_0, dict_1, tuple_0]
        var_2 = module_0.extract(complex_0, str_1, tuple_0, list_0)
    except BaseException:
        pass

def test_case_42():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.combine()
        str_0 = ''
        var_1 = module_0.regex_search(str_0, str_0)
        str_1 = 'in run() - task %s'
        dict_0 = {}
        str_2 = ']-`}V'
        tuple_0 = ()
        var_2 = module_0.extract(str_1, dict_0, str_2, tuple_0)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'posix_basic'
        var_0 = module_0.comment(str_0)
        str_1 = 'posix_basic'
        var_1 = module_0.path_join(str_1)
        var_2 = module_0.combine()
        str_2 = '[0bxECj\n>}\r^'
        bytes_0 = b'\xe9d\xdc\xee+\xd0i\xdfR\xc2Pi'
        filter_module_0 = module_0.FilterModule()
        var_3 = module_0.do_groupby(str_2, bytes_0, filter_module_0)
    except BaseException:
        pass

def test_case_44():
    try:
        list_0 = None
        str_0 = 'd5(51{ :c'
        dict_0 = {str_0: list_0}
        var_0 = module_0.subelements(dict_0, str_0)
    except BaseException:
        pass

def test_case_45():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '{'
        bool_0 = True
        dict_1 = {str_0: str_0}
        list_0 = [dict_0, bool_0]
        var_0 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = '#'
        str_1 = 'Group {0} upgraded.'
        str_2 = 'N)8z6\x0bl^S'
        dict_0 = {str_0: str_0, str_1: str_0, str_2: str_2}
        list_0 = [str_1]
        bytes_0 = None
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.rand(dict_0, list_0, bytes_0, filter_module_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'this is a test'
        str_1 = 'Q`$r_;!|'
        var_0 = module_0.regex_escape(str_0, str_1)
    except BaseException:
        pass

def test_case_48():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '}'
        bool_0 = True
        var_0 = module_0.mandatory(dict_0, bool_0)
        float_0 = 363.6
        list_0 = [float_0, str_0, float_0]
        list_1 = [bool_0, dict_0]
        float_1 = 60.34
        var_1 = module_0.regex_findall(list_0, filter_module_0, list_1, float_1)
    except BaseException:
        pass

def test_case_49():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        bool_0 = True
        var_0 = module_0.mandatory(dict_0, bool_0)
        dict_1 = {}
        var_1 = filter_module_0.filters()
        list_0 = [dict_0, bool_0]
        var_2 = filter_module_0.filters()
        str_0 = '\n'
        var_3 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_50():
    try:
        var_0 = module_0.combine()
        bytes_0 = b'\xa1\xc3{|7\xa9v\xd2E\xbaw~\xd54\xea\xf5'
        list_0 = None
        str_0 = '\n'
        list_1 = [str_0, bytes_0]
        var_1 = module_0.regex_search(bytes_0, list_0, *list_1)
    except BaseException:
        pass

def test_case_51():
    try:
        bytes_0 = b''
        list_0 = [bytes_0, bytes_0]
        bool_0 = True
        tuple_0 = (list_0, bool_0, bool_0)
        int_0 = None
        var_0 = module_0.flatten(tuple_0, int_0)
        list_1 = []
        var_1 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_52():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {filter_module_0: filter_module_0}
        str_0 = '{'
        dict_1 = {str_0: str_0}
        list_0 = [dict_0, dict_1]
        var_0 = module_0.subelements(list_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_53():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.combine()
        set_0 = None
        bytes_0 = b'z\xf7T\xbbm:\x06\xe7K'
        float_0 = -6581.0
        int_0 = -523
        var_1 = module_0.rand(set_0, bytes_0, float_0, filter_module_0, int_0)
    except BaseException:
        pass

def test_case_54():
    try:
        str_0 = 'iG.'
        var_0 = module_0.regex_search(str_0, str_0)
        str_1 = '12'
        str_2 = 'DU\x0bkDwWBO'
        float_0 = None
        var_1 = module_0.b64decode(float_0)
        var_2 = module_0.regex_replace(str_2)
        var_3 = module_0.regex_search(str_1, str_0)
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        float_1 = 100.0
        list_0 = [str_1]
        var_4 = module_0.regex_search(filter_module_0, float_1, *list_0)
    except BaseException:
        pass

def test_case_55():
    try:
        str_0 = 'Vlvble'
        ansible_undefined_0 = module_1.AnsibleUndefined(str_0)
        var_0 = module_0.mandatory(ansible_undefined_0)
    except BaseException:
        pass

def test_case_56():
    try:
        dict_0 = {}
        bool_0 = None
        set_0 = None
        list_0 = [dict_0, dict_0, set_0, set_0]
        var_0 = module_0.combine(*list_0)
        str_0 = 'posix_basic'
        str_1 = None
        dict_1 = {str_0: str_0, str_0: list_0, str_1: list_0}
        list_1 = [dict_0, bool_0]
        bytes_0 = b'[+\xfe\xd2\x98\x07\xf8\x198\x0e\xa0m~'
        var_1 = module_0.ternary(bool_0, dict_1, list_1, bytes_0)
        var_2 = module_0.randomize_list(list_0)
        str_2 = 'posix_extended'
        var_3 = module_0.fileglob(str_2)
        var_4 = module_0.get_hash(list_0, set_0)
    except BaseException:
        pass

def test_case_57():
    try:
        str_0 = ''
        var_0 = module_0.regex_replace(str_0, str_0, str_0)
        var_1 = module_0.regex_replace(str_0, str_0, str_0)
        str_1 = 'a'
        var_2 = module_0.regex_replace(str_0, str_1, str_0)
        str_2 = ';U?'
        int_0 = None
        bool_0 = False
        var_3 = module_0.randomize_list(int_0, bool_0)
        float_0 = 551.56
        var_4 = module_0.regex_escape(float_0)
        var_5 = module_0.comment(str_2)
        ansible_undefined_0 = module_1.AnsibleUndefined(bool_0, str_2, bool_0)
        async_iterator_0 = ansible_undefined_0.__aiter__()
        var_6 = module_0.mandatory(ansible_undefined_0, async_iterator_0)
    except BaseException:
        pass

def test_case_58():
    try:
        int_0 = -36
        str_0 = '1]4w'
        var_0 = module_0.mandatory(int_0, str_0)
        str_1 = 'abcd'
        var_1 = module_0.regex_replace(str_1, str_1, str_1)
        var_2 = module_0.regex_replace(str_1, str_1, str_1)
        str_2 = "MMo'yPgo_q!<&m[B.~"
        list_0 = [str_0, str_2, var_2, int_0]
        list_1 = [var_1, int_0, list_0]
        var_3 = module_0.combine(*list_1)
    except BaseException:
        pass