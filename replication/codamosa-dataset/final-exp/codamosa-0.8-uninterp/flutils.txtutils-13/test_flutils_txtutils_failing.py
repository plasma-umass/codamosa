# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        sequence_0 = None
        int_0 = module_0.len_without_ansi(sequence_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 574
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, max_lines=int_0)
        str_0 = '|GQy%O(`.p1+~'
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 2
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0)
        str_0 = 'Generator that expands the given attr_map and yields an _AttrMapping\n    amed tuple.\n\n    An attr_map is a tuple with each row containing a :term:`foreign-name`\n    which is a specially formatted string.\n    '
        str_1 = ansi_text_wrapper_0.fill(str_0)
        bool_0 = False
        bool_1 = True
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_1, bool_0, max_lines=int_0, placeholder=str_1)
        list_0 = ansi_text_wrapper_1.wrap(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "Lk0qB1aM'K\t?tq}_Y;6w"
        int_0 = -229
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
        bool_0 = True
        str_2 = 'P'
        str_3 = ansi_text_wrapper_0.fill(str_2)
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0)
        list_0 = ansi_text_wrapper_1.wrap(str_1)
        bool_1 = False
        bool_2 = False
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(bool_1, bool_2)
        str_4 = '-'
        list_1 = ansi_text_wrapper_2.wrap(str_4)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ')QzenjitOs!'
        int_0 = -99
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, max_lines=int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ezO*<k'
        int_0 = 2
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0)
        str_1 = 'Generator that expands the given attr_map and yields an _AttrMapping\n    amed tuple.\n\n    An attr_map is a tuple with each row containing a :term:`foreign-name`\n    which is a specially formatted string.\n    '
        str_2 = ansi_text_wrapper_0.fill(str_1)
        str_3 = ansi_text_wrapper_0.fill(str_2)
        bool_0 = False
        bool_1 = True
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_1, bool_0, max_lines=int_0, placeholder=str_0)
        list_0 = ansi_text_wrapper_1.wrap(str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'The path: %r must be an absolute path.  A path is considered absolute if it has both a root and (if the flavour allows) a drive.'
        bool_0 = True
        float_0 = -229.6972
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, max_lines=float_0, placeholder=str_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = None
        int_0 = -1909
        bool_0 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, bool_0, bool_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'cVa\nk[\x0cZc'
        str_1 = 'ez.L<'
        int_0 = -229
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_0)
        str_2 = ansi_text_wrapper_0.fill(str_1)
        bool_0 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, max_lines=int_0, placeholder=str_0)
        str_3 = '\x1b['
        list_0 = ansi_text_wrapper_0.wrap(str_3)
        str_4 = ansi_text_wrapper_1.fill(str_2)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "LkIqB1aM'K\tDtq}_s;6w"
        str_1 = 'cVa\n9[\x0cZTc'
        str_2 = 'ezO*<k'
        list_0 = [str_1, str_0, str_1, str_2]
        int_0 = module_0.len_without_ansi(list_0)
        int_1 = 2
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(max_lines=int_1)
        str_3 = ansi_text_wrapper_0.fill(str_0)
        int_2 = 941
        str_4 = '}zr+!q'
        str_5 = 'The path: %r can NOT be created as a directory because it already exists as a %s.'
        str_6 = None
        bool_0 = True
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(str_5, str_6, bool_0, bool_0, int_1, max_lines=int_0)
        str_7 = '+:~SS~\\ZJ1<1'
        str_8 = 't,,,\nY\x0bKx$J0q{7'
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_1, str_7, str_8, bool_0, bool_0, placeholder=str_3)
        str_9 = ansi_text_wrapper_2.fill(str_4)
        str_10 = None
        bool_1 = True
        ansi_text_wrapper_3 = module_0.AnsiTextWrapper(str_9, bool_1, bool_0, int_2, placeholder=str_2)
        list_1 = ansi_text_wrapper_3.wrap(str_10)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
        int_0 = module_0.len_without_ansi(str_0)
        bool_0 = False
        str_1 = 'wQS'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, placeholder=str_1)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass