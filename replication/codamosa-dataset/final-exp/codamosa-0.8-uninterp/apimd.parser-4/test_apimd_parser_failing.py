# Automatically generated by Pynguin.
import ast as module_0
import apimd.parser as module_1
import builtins as module_2

def test_case_0():
    try:
        str_0 = 'Lm54(&zBpH<y]1&5~H'
        list_0 = [str_0]
        assign_0 = module_0.Assign(*list_0)
        bool_0 = False
        dict_0 = {}
        parser_0 = module_1.Parser(bool_0, dict_0)
        parser_0.globals(str_0, assign_0)
        str_1 = None
        str_2 = module_1.code(str_0)
        str_3 = module_1.esc_underscore(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        name_0 = module_0.Name()
        str_0 = '"1'
        str_1 = None
        str_2 = "=s\x0bS'#j6:<s"
        str_3 = None
        str_4 = 'typing.Container'
        str_5 = 'collections.Counter'
        str_6 = '9\x0cjCroE{Of{;$q'
        dict_0 = {str_1: str_2, str_0: str_0, str_3: str_4, str_5: str_6}
        resolver_0 = module_1.Resolver(str_0, dict_0, str_3)
        a_s_t_0 = resolver_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'oC'
        list_0 = [str_0]
        dict_0 = {str_0: str_0}
        arguments_0 = module_0.arguments(*list_0, **dict_0)
        int_0 = -2007
        bool_0 = True
        parser_0 = module_1.Parser(bool_0, int_0, bool_0)
        parser_0.func_api(str_0, str_0, arguments_0, list_0, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '5j>9$kT{G6tXso2NwJ'
        list_0 = [str_0]
        str_1 = 'Rik5p/*{Ubg'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
        import_from_0 = module_0.ImportFrom(*list_0, **dict_0)
        dict_1 = {}
        parser_0 = module_1.Parser(dict_1)
        parser_0.imports(str_0, import_from_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'N[njk<\x0ba'
        import_0 = module_0.Import()
        list_0 = [import_0, import_0, import_0, import_0]
        ann_assign_0 = module_0.AnnAssign(*list_0)
        parser_0 = module_1.Parser()
        parser_0.globals(str_0, ann_assign_0)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'x=/N[!o52"V>BO\\<f'
        str_1 = 't<F.?'
        dict_0 = {str_1: str_0, str_1: str_0}
        parser_0 = module_1.Parser(dict_0, dict_0)
        str_2 = parser_0.compile()
        class_def_0 = module_0.ClassDef()
        parser_0.api(str_0, class_def_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        expr_0 = module_0.expr()
        list_0 = [expr_0, expr_0]
        list_1 = []
        bool_0 = True
        str_1 = '# Module `{}`'
        str_2 = None
        str_3 = '\rJ8g'
        str_4 = '2p'
        dict_0 = {str_1: str_2, str_2: str_2, str_3: str_4}
        parser_0 = module_1.Parser(bool_0, dict_0)
        parser_0.class_api(str_0, str_0, list_0, list_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\x0c-[08[\\2>0JMJ8-DK&'
        dict_0 = {}
        parser_0 = module_1.Parser(dict_0)
        module_x_var_0 = None
        parser_0.load_docstring(str_0, module_x_var_0)
        bool_0 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        iterable_0 = None
        str_0 = module_1.table(items=iterable_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = ''
        class_def_0 = module_0.ClassDef()
        bool_0 = False
        int_0 = 1733
        dict_0 = {}
        str_1 = None
        str_2 = '/!t2HCY5~c7'
        str_3 = '\x0c|G/L((O<C'
        str_4 = '+ahmEip:<%R(@4ok8'
        dict_1 = {str_1: str_2, str_3: str_4}
        parser_0 = module_1.Parser(bool_0, int_0, bool_0, dict_0, dict_1, dict_1, dict_1)
        parser_0.api(str_0, class_def_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'c`e]'
        str_1 = 'mLhi(9B'
        list_0 = [str_1]
        str_2 = '#(%m}&.3'
        dict_0 = {str_2: list_0}
        attribute_0 = module_0.Attribute(*list_0, **dict_0)
        str_3 = 'nYgX+>$s+'
        str_4 = 'd'
        str_5 = '6.v-TmC'
        str_6 = '.B:\x0c63'
        dict_1 = {str_4: str_3, str_3: str_5, str_4: str_6}
        str_7 = 'z\n\nf);+#(\x0c'
        resolver_0 = module_1.Resolver(str_3, dict_1, str_7)
        a_s_t_0 = resolver_0.visit_Attribute(attribute_0)
        dict_2 = {str_1: str_0}
        class_def_0 = module_0.ClassDef(**dict_2)
        str_8 = 'gH'
        bool_0 = False
        str_9 = None
        int_0 = -1732
        str_10 = None
        int_1 = -1177
        str_11 = 'l2Hv3'
        int_2 = 1
        dict_3 = {str_9: int_0, str_10: int_1, str_11: int_2}
        dict_4 = {}
        parser_0 = module_1.Parser(bool_0, dict_3, dict_4, dict_4)
        parser_0.api(str_0, class_def_0, prefix=str_8)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -3547.573429
        list_0 = [float_0]
        dict_0 = {}
        constant_0 = module_0.Constant(*list_0, **dict_0)
        str_0 = '8'
        str_1 = 'Ag`:q5RR_'
        str_2 = 'A'
        str_3 = None
        dict_1 = {str_0: str_1, str_2: str_3}
        resolver_0 = module_1.Resolver(str_0, dict_1)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
        str_4 = None
        str_5 = module_1.esc_underscore(str_4)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'NC<0-PAC3\r4FF+\\{'
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = 'qB|zDNUWZpO(RUut'
        list_0 = []
        ann_assign_0 = module_0.AnnAssign(**dict_0)
        list_1 = [ann_assign_0]
        int_0 = -2301
        str_2 = 'xhm+]BmX|$'
        str_3 = None
        set_0 = {str_2, str_0, str_2, str_3}
        str_4 = '|LMfg@u+#EI'
        dict_1 = {str_0: set_0, str_4: set_0}
        parser_0 = module_1.Parser(int_0, dict_1)
        parser_0.class_api(str_0, str_1, list_0, list_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'T}^\x0cEB/*'
        bool_0 = module_1.is_magic(str_0)
        str_1 = '"-lKjo'
        list_0 = []
        str_2 = '4n8bm<EE\r&/\n=B0f5'
        bool_1 = module_1.is_public_family(str_2)
        dict_0 = {}
        list_1 = [dict_0, dict_0]
        str_3 = '\x0c(p'
        str_4 = module_1.esc_underscore(str_3)
        dict_1 = {}
        dict_2 = {}
        parser_0 = module_1.Parser(dict_2)
        parser_0.class_api(str_1, str_1, list_0, list_1)
        bool_2 = True
        int_0 = 2498
        parser_1 = module_1.Parser(bool_2, int_0, dict_2)
        list_2 = [bool_2, str_2]
        subscript_0 = module_0.Subscript(*list_2)
        resolver_0 = module_1.Resolver(str_1, dict_2)
        resolver_1 = module_1.Resolver(str_2, dict_1)
        a_s_t_0 = resolver_1.visit_Subscript(subscript_0)
        str_5 = None
        list_3 = [str_5, resolver_0, dict_0, str_4]
        function_def_0 = module_0.FunctionDef(*list_3)
        parser_1.api(str_5, function_def_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '_r'
        dict_0 = {}
        list_0 = [dict_0, dict_0]
        dict_1 = None
        list_1 = [list_0]
        list_2 = [dict_1, str_0, list_1]
        attribute_0 = module_0.Attribute(*list_2)
        dict_2 = module_2.dict()
        resolver_0 = module_1.Resolver(str_0, dict_2)
        a_s_t_0 = resolver_0.visit_Attribute(attribute_0)
        parser_0 = module_1.Parser(dict_2)
        import_0 = module_0.Import(*list_1)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '\x0c-[08[\\2>0JMJ8-DK&'
        str_1 = ''
        list_0 = [str_1, str_1]
        arguments_0 = module_0.arguments(*list_0)
        none_type_0 = None
        bool_0 = None
        str_2 = 'KB&'
        int_0 = 0
        dict_0 = {str_2: int_0, str_2: int_0}
        str_3 = '2'
        str_4 = '}$K'
        dict_1 = {str_3: str_2, str_4: str_4, str_3: str_3}
        parser_0 = module_1.Parser(dict_0, dict_1, dict_1, dict_1)
        parser_0.func_api(str_1, str_0, arguments_0, none_type_0, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '5j>9$kT{G6tXso2NwJ'
        list_0 = [str_0, str_0]
        str_1 = 'Rik5p/*{Ubg'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
        import_from_0 = module_0.ImportFrom(*list_0, **dict_0)
        dict_1 = module_2.dict()
        parser_0 = module_1.Parser(dict_1)
        parser_0.imports(str_0, import_from_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 2079
        bool_0 = True
        dict_0 = {}
        str_0 = 'a=`'
        str_1 = 'F9.F9eNXi!TR+VM`'
        set_0 = {str_0, str_0, str_1, str_1}
        dict_1 = {str_0: set_0, str_1: set_0, str_0: set_0}
        dict_2 = {}
        parser_0 = module_1.Parser(int_0, bool_0, dict_0, dict_1, dict_2)
        str_2 = parser_0.compile()
        str_3 = 'm\nBnBDVP_'
        ann_assign_0 = None
        parser_0.globals(str_3, ann_assign_0)
        list_0 = [str_2, str_1]
        constant_0 = module_0.Constant(*list_0)
        str_4 = 'Nx@/h.Ukm}EI>\x0b'
        resolver_0 = module_1.Resolver(str_4, dict_2)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 2079
        bool_0 = True
        dict_0 = {}
        str_0 = 'a=`'
        str_1 = 'gi'
        str_2 = 'F9.p9eNXi!TR+V\r`'
        set_0 = {str_0, str_1, str_2, str_2}
        dict_1 = {str_0: set_0, str_2: set_0, str_0: set_0}
        dict_2 = {}
        parser_0 = module_1.Parser(int_0, bool_0, dict_0, dict_1, dict_2)
        str_3 = parser_0.compile()
        list_0 = [str_3, str_2]
        str_4 = 'Nx@/h.Ukm}EI>\x0b'
        resolver_0 = module_1.Resolver(str_4, dict_2)
        assign_0 = module_0.Assign(*list_0)
        str_5 = 'Pa^VAWa;F\\PC\x0c`'
        str_6 = 'Ih'
        dict_3 = {str_2: bool_0, str_5: set_0, str_1: resolver_0, str_6: list_0}
        class_def_0 = module_0.ClassDef(*list_0, **dict_3)
        parser_0.api(str_2, class_def_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '}E'
        bool_0 = module_1.is_public_family(str_0)
        str_1 = 'gG@R.8+cUJn'
        str_2 = 'typingFozenSet'
        parser_0 = module_1.Parser(bool_0)
        parser_0.parse(str_0, str_2)
        str_3 = '\n'
        module_x_var_0 = None
        parser_0.load_docstring(str_3, module_x_var_0)
        assign_0 = None
        parser_0.globals(str_1, assign_0)
        str_4 = '&'
        assign_1 = module_0.Assign()
        parser_0.globals(str_4, assign_1)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'Sx'
        bool_0 = module_1.is_public_family(str_0)
        str_1 = 'gG@R.8+cUJn'
        str_2 = 'tJpiHFoz:enSet'
        parser_0 = module_1.Parser(bool_0)
        parser_0.parse(str_0, str_2)
        module_x_var_0 = None
        parser_0.load_docstring(str_0, module_x_var_0)
        assign_0 = None
        parser_0.globals(str_1, assign_0)
        str_3 = '&'
        assign_1 = module_0.Assign()
        parser_0.globals(str_3, assign_1)
    except BaseException:
        pass