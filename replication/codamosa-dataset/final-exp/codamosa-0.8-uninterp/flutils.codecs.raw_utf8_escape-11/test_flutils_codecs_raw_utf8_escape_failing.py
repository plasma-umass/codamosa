# Automatically generated by Pynguin.
import flutils.codecs.raw_utf8_escape as module_0
import collections as module_1
import codecs as module_2

def test_case_0():
    try:
        str_0 = 'UQ(e\nhNqHVHvp_StrTw'
        tuple_0 = module_0.encode(str_0, str_0)
        tuple_1 = module_0.encode(str_0)
        byte_string_0 = None
        tuple_2 = module_0.decode(byte_string_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xca\x861g1\x85>F\xee\xd2|\\J\xfc$\xa8Gh:'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        user_string_0 = module_1.UserString(list_0)
        tuple_0 = module_0.encode(user_string_0)
    except BaseException:
        pass

def test_case_2():
    try:
        module_0.register()
        bytes_0 = b'\x19c\xf8(4\xee\xdf{\xff[\xa4'
        tuple_0 = module_0.decode(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '<9VJ",$HhoMrwm$X'
        set_0 = set()
        module_0.register()
        module_0.register()
        tuple_0 = module_0.decode(set_0)
        tuple_1 = module_0.encode(str_0)
        module_0.register()
        module_0.register()
        tuple_2 = module_0.encode(str_0)
        tuple_3 = module_0.encode(str_0)
        byte_string_0 = None
        tuple_4 = module_0.decode(byte_string_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        list_1 = [list_0, list_0]
        tuple_0 = module_0.decode(list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.register()
        str_0 = 'g$iFybooirV^>K&KiQ'
        int_0 = 2407
        tuple_0 = (str_0, int_0)
        tuple_1 = module_0.decode(tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        module_0.register()
        str_0 = 'eutf8h'
        var_0 = module_2.getdecoder(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        module_0.register()
        bytes_0 = b'a\xbc2\xc3)\xc4\xcf\n\xd5\xaa\x1b\x16\x90\x07'
        str_0 = "Convert a given command into a tuple for use by\n    :obj:`subprocess.Popen`.\n\n    Args:\n        cmd (:obj:`Sequence <typing.Sequence>`): The command to be converted.\n\n    This is for converting a command of type string or bytes to a tuple of\n    strings for use by :obj:`subprocess.Popen`.\n\n    Example:\n\n        >>> from flutils.cmdutils import prep_cmd\n        >>> prep_cmd('ls -Flap')\n        ('ls', '-Flap')\n    "
        module_0.register()
        tuple_0 = module_0.encode(str_0)
        module_0.register()
        module_0.register()
        str_1 = "\\\n[8q\t>\x0b%&nOw@ix#'p#"
        tuple_1 = module_0.encode(str_0)
        module_0.register()
        user_string_0 = module_1.UserString(bytes_0)
        tuple_2 = module_0.decode(bytes_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'p\xaa\xa9\xfc\x8f\xe6\xe4\n46\x92\x07u\xd6n'
        user_string_0 = module_1.UserString(bytes_0)
        tuple_0 = module_0.encode(user_string_0, user_string_0)
    except BaseException:
        pass