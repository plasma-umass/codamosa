# Automatically generated by Pynguin.
import thonny.roughparse as module_0

def test_case_0():
    try:
        str_0 = '&X*Fv_f,}3"~\r5'
        bool_0 = False
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        str_1 = "Sv?qp+q}pa'e^-j9W8h\n"
        var_1 = rough_parser_0.set_str(str_1)
        dict_0 = {}
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, rough_parser_0)
        var_2 = string_translate_pseudo_mapping_0.__iter__()
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "}.~:`j46B\\1y5;'"
        bool_0 = True
        set_0 = {bool_0}
        rough_parser_0 = module_0.RoughParser(bool_0, set_0)
        var_0 = rough_parser_0.set_str(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 97.74
        str_0 = '\\ *z/+Kk'
        rough_parser_0 = module_0.RoughParser(str_0, str_0)
        var_0 = rough_parser_0.find_good_parse_start(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        bytes_0 = b'\xa9p\x8e'
        str_0 = 'vijTM!}H@,.\t6\ri^?('
        rough_parser_0 = module_0.RoughParser(bytes_0, str_0)
        var_0 = rough_parser_0.set_lo(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '&X*Fvf,}3"\r5'
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = '\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ',,$AHYBD>8BEmlbv'
        bool_0 = False
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        str_1 = ']\n'
        var_1 = rough_parser_0.set_str(str_1)
        bool_1 = False
        var_2 = rough_parser_0.find_good_parse_start(bool_1)
        var_3 = rough_parser_0.get_base_indent_string()
        var_4 = rough_parser_0.get_continuation_type()
        var_5 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '&X*Fvf,}3C\r5'
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = '\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '&X*Fvf,}3"\r5'
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = '\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '&X*Fvf,}3"\r5'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = '\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.is_block_opener()
        bytes_0 = b'H[Z\xb6\x841\xbd\xe6\xb0\xe4\xca\xa1\xd0\xa4\xaf'
        var_2 = rough_parser_0.find_good_parse_start(bytes_0)
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 100032
        float_0 = 675.3755351290931
        rough_parser_0 = module_0.RoughParser(int_0, float_0)
        bool_0 = False
        var_0 = rough_parser_0.set_lo(bool_0)
        var_1 = rough_parser_0.get_last_open_bracket_pos()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '&X*Fvf,}3"\r5'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = '\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.is_block_opener()
        var_2 = rough_parser_0.get_last_stmt_bracketing()
        bytes_0 = b'H[Z\xb6\x841\xbd\xe6\xb0\xe4\xca\xa1\xd0\xa4\xaf'
        var_3 = rough_parser_0.find_good_parse_start(bytes_0)
        var_4 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "r RsIOC's)Az2X\n;"
        hyper_parser_0 = module_0.HyperParser(str_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ',,$AHYBD>8BEmlbv'
        bool_0 = False
        list_0 = [str_0, str_0, str_0]
        int_0 = None
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        str_1 = '\n'
        var_1 = rough_parser_0.set_str(str_1)
        var_2 = rough_parser_0.find_good_parse_start(list_0)
        var_3 = rough_parser_0.get_base_indent_string()
        float_0 = 0.8
        var_4 = rough_parser_0.get_continuation_type()
        hyper_parser_0 = module_0.HyperParser(rough_parser_0, float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\\ *z/+Kk'
        str_1 = 'i0qzXaEua!2.H#E!kR;'
        set_0 = {str_1, str_0, str_1}
        rough_parser_0 = module_0.RoughParser(str_1, set_0)
        var_0 = rough_parser_0.get_num_lines_in_stmt()
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '&X*Fvf,}3C\r5'
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = ''
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'gC0)58'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3376
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = "Sv?qp+\\p'-9W8\n"
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.is_block_closer()
        var_3 = rough_parser_0.get_base_indent_string()
        var_4 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_16():
    try:
        tuple_0 = ()
        str_0 = '/,,$AHYBD>8BEmlbv'
        bool_0 = False
        dict_0 = {str_0: bool_0, bool_0: tuple_0, str_0: tuple_0, bool_0: str_0}
        str_1 = '^)l.MO;\nG'
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, str_1)
        var_0 = string_translate_pseudo_mapping_0.__len__()
        list_0 = []
        int_0 = 3287
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        var_1 = rough_parser_0.set_lo(bool_0)
        bytes_0 = None
        dict_1 = {bytes_0: bytes_0}
        hyper_parser_0 = module_0.HyperParser(list_0, dict_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '&X*Fv_f,}3"~\r5'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = ']\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.find_good_parse_start()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_18():
    try:
        bool_0 = False
        tuple_0 = ()
        tuple_1 = (tuple_0,)
        dict_0 = {tuple_1: tuple_0, tuple_0: tuple_0}
        bool_1 = True
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, bool_1)
        var_0 = string_translate_pseudo_mapping_0.get(bool_0)
        bytes_0 = b'\xd6\x8b'
        int_0 = 5
        rough_parser_0 = module_0.RoughParser(bytes_0, int_0)
        var_1 = rough_parser_0.find_good_parse_start()
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '&n*Fv_f,}3"~\r5'
        list_0 = [str_0, str_0, str_0]
        int_0 = None
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = ']\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'gC0)58'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3376
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = "Sv?qp+\\p'h-9W8\n"
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = ',,$AHYBD>8BEmlbv'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = 'Sv?qp+q}pe^-j9W8h\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.get_num_lines_in_stmt()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = ',,$AHYBD>8BEmlbv'
        bool_0 = False
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        str_1 = 'Sv?qp+q}pe^-j9W8h\n'
        var_1 = rough_parser_0.set_str(str_1)
        var_2 = rough_parser_0.get_last_open_bracket_pos()
        var_3 = rough_parser_0.get_base_indent_string()
        var_4 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '&X*Fv_f,}3"~\r5'
        bool_0 = False
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        str_1 = 'Sv?qp+q}pe^-j9W8h\n'
        var_1 = rough_parser_0.set_str(str_1)
        var_2 = rough_parser_0.get_base_indent_string()
        var_3 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'gC)58'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3326
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = "S4(v?qp+\\p'-9W8\n"
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.find_good_parse_start(rough_parser_0)
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'gC0)5'
        list_0 = [str_0, str_0, str_0]
        int_0 = 3325
        rough_parser_0 = module_0.RoughParser(list_0, int_0)
        str_1 = 'S?qp-\\W8\n'
        var_0 = rough_parser_0.set_str(str_1)
        var_1 = rough_parser_0.get_base_indent_string()
        bool_0 = True
        var_2 = rough_parser_0.set_lo(bool_0)
    except BaseException:
        pass