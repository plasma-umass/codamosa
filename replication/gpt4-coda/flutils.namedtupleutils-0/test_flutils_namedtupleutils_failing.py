# Automatically generated by Pynguin.
import collections.abc as module_0
import flutils.namedtupleutils as module_1
import types as module_2
import collections as module_3

def test_case_0():
    try:
        mapping_0 = module_0.Mapping()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = None
        var_0 = module_1.to_namedtuple(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        var_0 = module_1.to_namedtuple(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        simple_namespace_0 = module_2.SimpleNamespace()
        var_0 = module_1.to_namedtuple(simple_namespace_0)
        var_1 = module_1.to_namedtuple(simple_namespace_0)
        str_0 = 'kRTd[J~\x0c'
        dict_0 = {str_0: str_0}
        var_2 = module_1.to_namedtuple(simple_namespace_0)
        str_1 = '}`Q'
        ordered_dict_0 = module_3.OrderedDict()
        bool_0 = False
        tuple_0 = (ordered_dict_0, simple_namespace_0, bool_0)
        var_3 = module_1.to_namedtuple(tuple_0)
        list_0 = [str_1, dict_0, str_1]
        mapping_0 = module_0.Mapping(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'aI\x0b'
        dict_0 = {str_0: str_0}
        simple_namespace_0 = module_2.SimpleNamespace(**dict_0)
        var_0 = module_1.to_namedtuple(simple_namespace_0)
        str_1 = 'a'
        str_2 = 'b'
        int_0 = 1
        int_1 = 2
        int_2 = {str_1: int_0, str_1: int_0, str_2: int_1}
        var_1 = module_1.to_namedtuple(int_2)
        str_3 = 'c'
        str_4 = 'A :obj:`TextWrapper <textwrap.TextWrapper>` object that correctly\n    wraps text containing ANSI codes.\n\n\n    *New in version 0.6*\n\n    Args:\n        width (int, optional): The maximum length of wrapped lines.\n            As long as there are no individual words in the input text\n            longer than this given ``width``,\n            :obj:`~flutils.txtutils.AnsiTextWrapper`\n            guarantees that no output line will be longer than ``width``\n            characters.  Defaults to: ``70``\n        initial_indent (str, optional): Text that will be prepended\n            to the first line of wrapped output. Counts towards the\n            length of the first line. An empty string value will not\n            indent the first line.  Defaults to: ``\'\'`` an empty string.\n        subsequent_indent (str, optional): Text that will be prepended\n            to all lines of wrapped output except the first. Counts\n            towards the length of each line except the first.\n            Defaults to: ``\'\'`` an empty string.\n        expand_tabs (bool, optional): If :obj:`True`, then all tab\n            characters in text will be expanded to spaces using the\n            :obj:`expandtabs <str.expandtabs>`.  Also see the ``tabsize``\n            argument.  Defaults to: :obj:`True`.\n        replace_whitespace (bool, optional): If :obj:`True`, after tab\n            expansion but before wrapping, the wrap() method will replace\n            each whitespace character with a single space. The whitespace\n            characters replaced are as follows: tab, newline, vertical\n            tab, form-feed, and carriage return (``\'\\t\\n\\v\\f\\r\'``).\n            Defaults to: :obj:`True`.\n        fix_sentence_endings (bool, optional): If :obj:`True`,\n            :obj:`~flutils.txtutils.AnsiTextWrapper`\n            attempts to detect sentence endings and\n            ensure that sentences are always separated by exactly two\n            spaces. This is generally desired for text in a monospaced\n            font. However, the sentence detection algorithm is imperfect;\n            it assumes that a sentence ending consists of a lowercase\n            letter followed by one of \'.\', \'!\', or \'?\', possibly\n            followed by one of \'"\' or "\'", followed by a space.\n            Defaults to: :obj:`False`.\n        break_long_words (bool, optional): If :obj:`True`, then words\n            longer than width will be broken in order to ensure that no\n            lines are longer than width. If it is :obj:`False`, long words\n            will not be broken, and some lines may be longer than width.\n            (Long words will be put on a line by themselves, in order to\n            minimize the amount by which width is exceeded.)\n            Defaults to: :obj:`True`.\n        drop_whitespace (bool, optional): If :obj:`True`, whitespace at\n            the beginning and ending of every line (after wrapping but\n            before indenting) is dropped. Whitespace at the beginning of\n            the paragraph, however, is not dropped if non-whitespace\n            follows it. If whitespace being dropped takes up an entire\n            line, the whole line is dropped. Defaults to: :obj:`True`\n        break_on_hyphens (bool, optional): If :obj:`True`, wrapping will\n            occur preferably on whitespaces and right after hyphens in\n            compound words, as it is customary in English. If\n            :obj:`false`, only whitespaces will be considered as\n            potentially good places for line breaks, but you need to set\n            ``break_long_words`` to :obj:`False` if you want truly\n            insecable words.  Defaults to: :obj:`True`.\n        tabsize (int, optional): If ``expand_tabs`` is :obj:`True`, then\n            all tab characters in text will be expanded to zero or more\n            spaces, depending on the current column and the given tab size.\n            Defaults to: ``8``.\n        max_lines (:obj:`int` or :obj:`None`, optional): If not :obj:`None`,\n            then the output will contain at most ``max_lines lines``, with\n            ``placeholder`` appearing at the end of the output.\n            Defaults to: :obj:`None`.\n        placeholder (str, optional): Text that will appear at the end of\n            the output text if it has been truncated.\n            Defaults to: ``\' [...]\'``\n\n    Note:\n        The ``initial_indent``, ``subsequent_indent`` and ``placeholder``\n        parameters can also contain ANSI codes.\n\n    Note:\n        If ``expand_tabs`` is :obj:`False` and ``replace_whitespace``\n        is :obj:`True`, each tab character will be replaced by a single\n        space, which is not the same as tab expansion.\n\n    Note:\n        If ``replace_whitespace`` is :obj:`False`, newlines may appear\n        in the middle of a line and cause strange output. For this reason,\n        text should be split into paragraphs (using :obj:`str.splitlines`\n        or similar) which are wrapped separately.\n\n    Example:\n        Use :obj:`~flutils.txtutils.AnsiTextWrapper` the same way as using\n        :obj:`TextWrapper <textwrap.TextWrapper>`::\n\n            from flutils.txtutils import AnsiTextWrapper\n            text = (\n                \'\\x1b[31m\\x1b[1m\\x1b[4mLorem ipsum dolor sit amet, \'\n                \'consectetur adipiscing elit. Cras fermentum maximus \'\n                \'auctor. Cras a varius ligula. Phasellus ut ipsum eu \'\n                \'erat consequat posuere.\\x1b[0m Pellentesque habitant \'\n                \'morbi tristique senectus et netus et malesuada fames ac \'\n                \'turpis egestas. Maecenas ultricies lacus id massa \'\n                \'interdum dignissim. Curabitur \\x1b[38;2;55;172;230m \'\n                \'efficitur ante sit amet nibh consectetur, consequat \'\n                \'rutrum nunc\\x1b[0m egestas. Duis mattis arcu eget orci \'\n                \'euismod, sit amet vulputate ante scelerisque. Aliquam \'\n                \'ultrices, turpis id gravida vestibulum, tortor ipsum \'\n                \'consequat mauris, eu cursus nisi felis at felis. \'\n                \'Quisque blandit lacus nec mattis suscipit. Proin sed \'\n                \'tortor ante.  Praesent fermentum orci id dolor \'\n                \'\\x1b[38;5;208meuismod, quis auctor nisl sodales.\\x1b[0m\'\n            )\n            wrapper = AnsiTextWrapper(width=40)\n            wrapped_text = wrapper.fill(text)\n            print(wrapped_text)\n\n        The output:\n\n            .. image:: ../static/AnsiTextWrapper_example_result.png\n               :scale: 75%\n\n    '
        dict_1 = {str_4: str_3, str_2: var_1}
        simple_namespace_1 = module_2.SimpleNamespace(**dict_1)
        var_2 = module_1.to_namedtuple(simple_namespace_1)
        var_3 = module_1.to_namedtuple(simple_namespace_1)
        var_4 = None
        var_5 = module_1.to_namedtuple(var_4)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b"zT\x00\xad\xba\xb9\x0fi'z\xa3-\xc1"
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        list_0 = [dict_0]
        bool_0 = True
        str_0 = 'Fm'
        dict_1 = {str_0: dict_0}
        tuple_0 = (list_0, bool_0, dict_1)
        var_0 = module_1.to_namedtuple(tuple_0)
    except BaseException:
        pass