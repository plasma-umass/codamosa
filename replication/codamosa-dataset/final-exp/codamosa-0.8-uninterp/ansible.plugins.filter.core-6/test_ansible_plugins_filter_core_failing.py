# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0
import glob as module_1
import ansible.template as module_2

def test_case_0():
    try:
        str_0 = 'hello'
        var_0 = module_0.get_hash(str_0)
        filter_module_0 = module_0.FilterModule()
        list_0 = [str_0]
        var_1 = module_0.to_yaml(filter_module_0, *list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        list_0 = [tuple_0]
        str_0 = "IfqDo'l-W"
        var_0 = module_0.to_yaml(str_0)
        float_0 = -278.4
        set_0 = {var_0}
        str_1 = 'Vz|'
        tuple_1 = (set_0, list_0, str_1)
        list_1 = [tuple_1]
        var_1 = module_0.get_hash(float_0, list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'pSes|stA|ring'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.to_nice_yaml(dict_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 2620
        var_0 = module_0.to_nice_yaml(int_0)
        float_0 = 0.1
        bool_0 = False
        var_1 = module_0.rand(float_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xe6\x9d\x88'
        list_0 = [bytes_0, bytes_0]
        var_0 = module_0.quote(list_0)
        var_1 = module_0.to_nice_json(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b't\x9a\x92[7\x16\xe5\xd6\x13\xc8\xb7XB^\xa9\xba\xa2#\xd1'
        tuple_0 = (bytes_0,)
        list_0 = [bytes_0, tuple_0, tuple_0]
        var_0 = module_0.strftime(tuple_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 2293.07151
        list_0 = None
        set_0 = {list_0, float_0, list_0}
        float_1 = -1440.42
        var_0 = module_0.regex_findall(list_0, set_0, float_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'ptest string'
        int_0 = -451
        list_0 = [str_0, int_0]
        var_0 = module_0.regex_search(str_0, list_0, *list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'E<'
        var_0 = module_0.from_yaml(str_0)
        filter_module_0 = None
        var_1 = module_0.comment(filter_module_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = None
        list_0 = [int_0, int_0, int_0, int_0]
        bool_0 = True
        var_0 = module_0.rand(int_0, list_0, bool_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '+?D'
        filter_module_0 = module_0.FilterModule()
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.rand(str_0, filter_module_0, list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        list_0 = None
        var_0 = module_0.get_hash(bool_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        filter_module_0 = module_0.FilterModule()
        dict_0 = {}
        var_0 = module_0.get_encrypted_password(dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        set_0 = set()
        bytes_0 = b'\x0c\x87\x0c\xa0J\x1f\xba\xe5\x83'
        list_0 = []
        bool_0 = True
        var_0 = module_0.get_encrypted_password(set_0, bytes_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        filter_module_0 = module_0.FilterModule()
        int_0 = -4103
        var_0 = module_0.to_uuid(int_0, filter_module_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'ptest string'
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b''
        var_0 = module_0.comment(bytes_0)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = 497.370857
        set_0 = {float_0}
        list_0 = [set_0, float_0, set_0]
        var_0 = module_0.extract(float_0, set_0, list_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ''
        str_1 = '*'
        var_0 = module_0.fileglob(str_1)
        var_1 = module_1.glob(str_1)
        ansible_undefined_0 = None
        set_0 = {ansible_undefined_0, str_1, str_0, ansible_undefined_0}
        filter_module_0 = module_0.FilterModule()
        var_2 = module_0.do_groupby(ansible_undefined_0, set_0, filter_module_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bool_0 = True
        var_0 = module_0.b64encode(bool_0)
        bytes_0 = b''
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        list_1 = []
        var_1 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_20():
    try:
        bytes_0 = b'\xce'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        int_0 = -1561
        var_0 = module_0.subelements(list_0, list_0, int_0)
    except BaseException:
        pass

def test_case_21():
    try:
        list_0 = []
        str_0 = 'iS*'
        list_1 = [list_0, list_0, list_0]
        var_0 = module_0.subelements(str_0, list_1)
    except BaseException:
        pass

def test_case_22():
    try:
        set_0 = set()
        dict_0 = {}
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0)
        bool_0 = False
        var_1 = module_0.regex_replace(bool_0)
        var_2 = module_0.combine()
        var_3 = module_0.regex_search(set_0, set_0)
    except BaseException:
        pass

def test_case_23():
    try:
        filter_module_0 = module_0.FilterModule()
        int_0 = -2205
        set_0 = {int_0, int_0, int_0}
        var_0 = module_0.path_join(set_0)
    except BaseException:
        pass

def test_case_24():
    try:
        bytes_0 = b'C\xa26F\x17h\x0b^V\x9b:\xd5\xd0N\x85+)be'
        var_0 = module_0.to_nice_yaml(bytes_0)
        str_0 = 'ansible_port'
        list_0 = [str_0]
        var_1 = module_0.to_yaml(list_0)
        bytes_1 = b'\xc8\xfb\xea\xd1gS"\xea\xab\xc8Bca\xfa\xbb\xf1'
        var_2 = module_0.to_uuid(list_0, bytes_1)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '\re[SAHaDb#\n#.{f\ntH'
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.randomize_list(str_0, filter_module_0)
        bytes_0 = b'\xba6\x85c\x0e\xe3\x8fX\xe3e\xd1\x81\\}\xcc\xea\xac\x03\xac '
        dict_0 = {}
        dict_1 = None
        var_1 = module_0.regex_search(bytes_0, dict_0, **dict_1)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'ptest string'
        list_0 = [str_0, str_0]
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.subelements(list_0, filter_module_0)
    except BaseException:
        pass

def test_case_27():
    try:
        bytes_0 = b'\xb0\x8a;'
        list_0 = [bytes_0, bytes_0]
        str_0 = 'we have included files to process'
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.subelements(list_0, str_0, filter_module_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = '3h_Kj'
        bool_0 = False
        dict_0 = {str_0: str_0, str_0: bool_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.to_nice_yaml(dict_0)
        var_1 = module_0.dict_to_list_of_dict_key_value_elements(bool_0)
    except BaseException:
        pass

def test_case_29():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = ')\r2RMQ'
        var_0 = module_0.to_datetime(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        bool_0 = None
        str_0 = 'wU}5v'
        dict_0 = {str_0: bool_0}
        var_0 = module_0.from_yaml(bool_0)
        var_1 = module_0.combine(**dict_0)
    except BaseException:
        pass

def test_case_31():
    try:
        list_0 = None
        var_0 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
    except BaseException:
        pass

def test_case_32():
    try:
        bytes_0 = b'\xce\xfa'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
        var_0 = module_0.to_bool(list_0)
        set_0 = None
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(list_0, set_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = 'test stri*g'
        str_1 = 'Error while attempting to fork: %s'
        var_0 = module_0.regex_search(str_0, str_1)
        str_2 = '\\g<str>'
        str_3 = '.71'
        str_4 = 'vnD6]Rlw3E'
        dict_0 = {str_2: str_2, str_3: var_0, str_4: str_1}
        list_0 = [str_1, str_3]
        str_5 = '* ySAB>de1s_wr7'
        float_0 = 0.0001
        var_1 = module_0.extract(dict_0, list_0, str_5, float_0)
    except BaseException:
        pass

def test_case_34():
    try:
        var_0 = module_0.regex_replace()
        complex_0 = None
        var_1 = module_0.to_bool(complex_0)
        str_0 = 'fo.ba*az?'
        str_1 = 'fake'
        var_2 = module_0.regex_escape(str_0, str_1)
    except BaseException:
        pass

def test_case_35():
    try:
        bytes_0 = None
        int_0 = 4
        dict_0 = {int_0: bytes_0}
        var_0 = module_0.subelements(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_36():
    try:
        dict_0 = None
        filter_module_0 = module_0.FilterModule()
        bytes_0 = b"\xf8\xe0:\xb3\xf0\x99\x96\xfeM\x9e\xc5k\xa4\x80\xfc\xd8%\x90'"
        str_0 = '{AYxTol+\n\\A0^'
        str_1 = 'python'
        dict_1 = {str_0: bytes_0, str_1: str_0}
        var_0 = module_0.to_bool(dict_1)
        bytes_1 = b''
        str_2 = 'GO5yD0{'
        var_1 = module_0.ternary(bytes_1, filter_module_0, dict_0, str_2)
        list_0 = None
        tuple_0 = (dict_0, list_0, str_0)
        var_2 = module_0.path_join(tuple_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = 'R{2Ax~jY^FAMT#dShv'
        str_1 = 'Ypmt3V'
        dict_0 = {str_1: str_0}
        var_0 = module_0.regex_findall(str_0, dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        bytes_0 = b'\xce\xfa'
        str_0 = '$7M6n_>@BiN\ni>%X'
        str_1 = None
        dict_0 = {str_0: str_0, str_1: str_1, str_0: bytes_0}
        var_0 = module_0.dict_to_list_of_dict_key_value_elements(dict_0)
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        set_0 = set()
        filter_module_0 = module_0.FilterModule()
        var_1 = filter_module_0.filters()
        var_2 = module_0.from_yaml(set_0)
        list_1 = []
        var_3 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_39():
    try:
        str_0 = 'foo.bar*baz?'
        str_1 = 'foo.bar*baz?'
        var_0 = module_0.regex_escape(str_1, str_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'OU\rE`>,PZ1b;T6~"'
        var_0 = module_0.comment(str_0)
        str_1 = 'u$[YbAglu9`t[\x0c56T'
        bytes_0 = b'k"\x0b\xfb{\xaa\x0e\xd7'
        bool_0 = True
        list_0 = []
        var_1 = module_0.extract(str_1, bytes_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = '*'
        var_0 = module_0.fileglob(str_0)
        list_0 = [var_0]
        var_1 = module_0.combine(*list_0)
    except BaseException:
        pass

def test_case_42():
    try:
        set_0 = None
        var_0 = module_0.quote(set_0)
        float_0 = -3226.2923
        str_0 = '>CaLD'
        dict_0 = {str_0: float_0}
        filter_module_0 = module_0.FilterModule(**dict_0)
    except BaseException:
        pass

def test_case_43():
    try:
        int_0 = None
        float_0 = -66.764
        bytes_0 = b'%\x0c\t\xe8\x98e\x1c\xbe`>T\x88\x18\x17'
        set_0 = set()
        tuple_0 = (float_0, bytes_0, set_0, set_0)
        str_0 = 'F5vSKG~GSs0QdD+)nc*'
        tuple_1 = (tuple_0, tuple_0, str_0)
        list_0 = [int_0, int_0, int_0, tuple_1]
        dict_0 = {}
        var_0 = module_0.combine(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_44():
    try:
        set_0 = set()
        float_0 = -912.32
        list_0 = [set_0, float_0, float_0]
        str_0 = ''
        int_0 = -324
        tuple_0 = (str_0, int_0)
        var_0 = module_0.regex_findall(float_0, list_0, tuple_0, list_0)
    except BaseException:
        pass

def test_case_45():
    try:
        set_0 = set()
        str_0 = '\x0b"S\'._j~eL"'
        var_0 = module_0.from_yaml_all(str_0)
        bytes_0 = None
        list_0 = [set_0, bytes_0, bytes_0, set_0, set_0, bytes_0]
        var_1 = module_0.regex_search(list_0, set_0)
    except BaseException:
        pass

def test_case_46():
    try:
        bytes_0 = b''
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        list_1 = []
        var_0 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_47():
    try:
        bytes_0 = b'\xce\xfa'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        bytes_1 = b'7'
        str_0 = 'ssh_key_comment'
        var_0 = module_0.ternary(dict_0, bytes_1, str_0)
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
        int_0 = 3
        list_1 = [int_0]
        var_1 = module_0.subelements(list_0, list_1)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'Error while attempting to fork: %s'
        int_0 = 1
        var_0 = module_0.to_bool(int_0)
        list_0 = [str_0, str_0]
        var_1 = module_0.subelements(str_0, list_0)
    except BaseException:
        pass

def test_case_49():
    try:
        float_0 = 0.1
        bool_0 = False
        var_0 = module_0.rand(float_0, bool_0)
    except BaseException:
        pass

def test_case_50():
    try:
        str_0 = 'ptest string'
        str_1 = 'test (?P<str>string)'
        var_0 = module_0.regex_search(str_0, str_1)
        var_1 = module_0.combine()
        bytes_0 = b'q\x0b\xa6N\x8b\x91\xf0\xa2\x1c\xc8[$'
        str_2 = '\r-J*W{J\x0bKB'
        dict_0 = {str_2: bytes_0, str_2: var_1}
        str_3 = 'F0Xar]ikEP_"|'
        list_0 = []
        str_4 = '_Im;fU4D9ruiW'
        var_2 = module_0.rand(dict_0, str_3, list_0, str_4)
    except BaseException:
        pass

def test_case_51():
    try:
        str_0 = 'python'
        bool_0 = False
        str_1 = 'Could not detect which major revision of yum is in use, which is required to determine module backend.'
        var_0 = module_0.rand(str_0, bool_0, str_1)
    except BaseException:
        pass

def test_case_52():
    try:
        bool_0 = False
        var_0 = module_0.to_bool(bool_0)
        filter_module_0 = module_0.FilterModule()
        var_1 = module_0.mandatory(filter_module_0)
        bytes_0 = b"\r'.\xce\xf3\x05\xa6\rk\x18\x00\xf8\x145B\x06\x82\xff:"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
        int_0 = -505
        var_2 = module_0.subelements(list_0, list_0, int_0)
    except BaseException:
        pass

def test_case_53():
    try:
        str_0 = '/tmp/alice/onekey.pub'
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = [str_1]
        str_3 = 'no\tL.a.realdkey'
        var_0 = module_0.subelements(str_2, str_3)
    except BaseException:
        pass

def test_case_54():
    try:
        str_0 = 'name'
        str_1 = 'groups'
        str_2 = 'authorized'
        str_3 = 'alice'
        str_4 = 'wheel'
        str_5 = [str_4]
        str_6 = '/tmp/alice/onekey.pub'
        str_7 = [str_6]
        str_8 = {str_0: str_3, str_1: str_5, str_2: str_7}
        str_9 = [str_8]
        var_0 = module_0.subelements(str_9, str_1)
        bool_0 = True
        var_1 = module_0.subelements(str_9, str_1, bool_0)
        int_0 = 0
        var_2 = str_9[int_0]
        var_3 = module_0.subelements(var_2, str_1)
    except BaseException:
        pass

def test_case_55():
    try:
        str_0 = 'foo.bar*baz?'
        var_0 = module_0.regex_escape(str_0)
        str_1 = 'posix_basic'
        var_1 = module_0.regex_escape(str_0, str_1)
        str_2 = 'foo.bar*baz?'
        dict_0 = {str_2: str_2}
        int_0 = 32602
        bool_0 = False
        str_3 = '#'
        set_0 = {str_3, int_0}
        var_2 = module_0.rand(dict_0, int_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_56():
    try:
        str_0 = 'bar'
        ansible_undefined_0 = module_2.AnsibleUndefined(str_0)
        var_0 = module_0.mandatory(ansible_undefined_0)
    except BaseException:
        pass

def test_case_57():
    try:
        str_0 = 'bar'
        ansible_undefined_0 = module_2.AnsibleUndefined(str_0)
        str_1 = 'BAR is not defined!'
        var_0 = module_0.mandatory(ansible_undefined_0, str_1)
    except BaseException:
        pass

def test_case_58():
    try:
        list_0 = []
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        str_0 = '-g'
        type_0 = None
        ansible_undefined_0 = module_2.AnsibleUndefined(str_0, type_0)
        async_iterator_0 = ansible_undefined_0.__aiter__()
        var_0 = module_0.ternary(filter_module_0, ansible_undefined_0, filter_module_0, async_iterator_0)
        var_1 = module_0.list_of_dict_key_value_elements_to_dict(list_0)
        set_0 = None
        float_0 = -1570.0
        var_2 = ansible_undefined_0.__contains__(float_0)
        str_1 = 'H[~i\\:\x0b0VR:$|b{Bas*+'
        str_2 = '|'
        str_3 = 'JWQ>_i%R,;7+zKNp|'
        dict_1 = {str_1: list_0, str_2: str_2, str_3: set_0}
        int_0 = 1243
        str_4 = 'Mwk|\\BLN2oZ'
        var_3 = module_0.comment(str_4, **dict_1)
        var_4 = module_0.do_groupby(set_0, dict_1, int_0)
    except BaseException:
        pass

def test_case_59():
    try:
        str_0 = 'foo.bar'
        var_0 = module_0.regex_escape(str_0)
        str_1 = 'posix_basic'
        var_1 = module_0.regex_escape(str_0, str_1)
        str_2 = 'posix_extended'
        var_2 = module_0.regex_escape(str_0, str_2)
    except BaseException:
        pass