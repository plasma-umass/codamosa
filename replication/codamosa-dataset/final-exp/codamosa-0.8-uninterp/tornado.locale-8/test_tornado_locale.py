# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1
import datetime as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'SEB|i'
    list_0 = [str_0]
    locale_0 = module_0.get(*list_0)

def test_case_2():
    str_0 = 'nV?7'
    module_0.set_default_locale(str_0)

def test_case_3():
    str_0 = None
    module_0.load_translations(str_0)

def test_case_4():
    str_0 = '.'
    module_0.load_gettext_translations(str_0, str_0)

def test_case_5():
    int_0 = 1
    bool_0 = True
    iterable_0 = module_0.get_supported_locales()
    list_0 = []
    locale_0 = module_0.get(*list_0)
    str_0 = locale_0.format_date(int_0, bool_0)

def test_case_6():
    str_0 = ' DHv~Qp,HFnyp(z'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)

def test_case_7():
    locale_0 = module_0.get()
    int_0 = 827
    str_0 = locale_0.format_date(int_0)

def test_case_8():
    int_0 = 1
    locale_0 = module_0.get()
    str_0 = locale_0.friendly_number(int_0)

def test_case_9():
    str_0 = '.-gTn@-vug4z'
    str_1 = '-<A]a@\r*\t5$&aDpx'
    str_2 = 'fcq\rQHd@lR?l3KeID0P\r'
    timedelta_0 = module_2.timedelta()
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_3 = gettext_locale_0.pgettext(str_1, str_2, str_1, timedelta_0)
    float_0 = -832.0
    str_4 = '9hC>H> FV\t$?'
    dict_0 = {}
    c_s_v_locale_0 = module_0.CSVLocale(str_4, dict_0)
    str_5 = c_s_v_locale_0.pgettext(str_0, str_0, str_0, float_0)

def test_case_10():
    str_0 = 'en_US'
    int_0 = 1
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = gettext_locale_0.pgettext(str_0, str_0, str_0, int_0)
    locale_0 = module_0.get()
    str_2 = locale_0.friendly_number(int_0)

def test_case_11():
    str_0 = '-<A]a@\r*\t5$&aDpx'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = gettext_locale_0.pgettext(str_0, str_0)

def test_case_12():
    str_0 = 'Closes the `IOLoop`, freeing any resources used.\n\n        If ``all_fds`` is true, all file descriptors registered on the\n        IOLoop will be closed (not just the ones created by the\n        `IOLoop` itself).\n\n        Many applications will only use a single `IOLoop` that runs for the\n        entire lifetime of the process.  In that case closing the `IOLoop`\n        is not necessary since everything will be cleaned up when the\n        process exits.  `IOLoop.close` is provided mainly for scenarios\n        such as unit tests, which create and destroy a large number of\n        ``IOLoops``.\n\n        An `IOLoop` must be completely stopped before it can be closed.  This\n        means that `IOLoop.stop()` must be called *and* `IOLoop.start()` must\n        be allowed to return before attempting to call `IOLoop.close()`.\n        Therefore the call to `close` will usually appear just after\n        the call to `start` rather than near the call to `stop`.\n\n        .. versionchanged:: 3.1\n           If the `IOLoop` implementation supports non-integer objects\n           for "file descriptors", those objects will have their\n           ``close`` method when ``all_fds`` is true.\n        '
    list_0 = []
    locale_0 = module_0.get(*list_0)
    str_1 = locale_0.list(str_0)

def test_case_13():
    int_0 = 1086
    str_0 = 'FRf6W/W&Ch<U_2o4Li]y'
    str_1 = 'openid.ns'
    str_2 = '-<A]a@\r*\t5$&aDpx'
    list_0 = [str_0, str_1, str_2]
    locale_0 = module_0.get(*list_0)
    str_3 = locale_0.friendly_number(int_0)

def test_case_14():
    float_0 = -3901.44
    int_0 = 2719
    bool_0 = True
    bool_1 = True
    str_0 = 'mP1&#HNL<#^`/kS>'
    str_1 = ''
    list_0 = [str_0, str_1, str_1, str_0]
    locale_0 = module_0.get(*list_0)
    str_2 = locale_0.format_date(float_0, int_0, bool_0, bool_1)

def test_case_15():
    str_0 = 'en'
    int_0 = 1
    timedelta_0 = module_2.timedelta()
    timedelta_1 = module_2.timedelta()
    str_1 = '@$7nq2(?b'
    str_2 = 'DIN(zLb&fcj(KXm`\x0b'
    str_3 = 'txP'
    str_4 = None
    str_5 = 'Base class for HTTP request handlers.\n\n    Subclasses must define at least one of the methods defined in the\n    "Entry points" section below.\n\n    Applications should not construct `RequestHandler` objects\n    directly and subclasses should not override ``__init__`` (override\n    `~RequestHandler.initialize` instead).\n\n    '
    str_6 = '-<A]a@\r*\t5$&aDpx'
    str_7 = 'Q}c)'
    str_8 = '^\rO\t'
    dict_0 = {str_3: str_4, str_0: str_5, str_6: str_7, str_4: str_8}
    dict_1 = {str_2: dict_0, str_8: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)
    str_9 = c_s_v_locale_0.pgettext(str_1, str_0)
    str_10 = ''
    str_11 = '-xCka!*p>ms9W"%L\n7HI'
    dict_2 = {}
    c_s_v_locale_1 = module_0.CSVLocale(str_11, dict_2)
    str_12 = c_s_v_locale_1.pgettext(str_0, str_10, str_0, int_0)
    int_1 = 776
    locale_0 = module_0.get()
    str_13 = locale_0.friendly_number(int_1)
    str_14 = '1qyB"Yd+OoABklLZ\t'
    str_15 = c_s_v_locale_1.pgettext(str_10, str_14)
    locale_1 = module_0.get()
    str_16 = locale_1.pgettext(str_0, str_11)

def test_case_16():
    int_0 = 14
    var_0 = int_0 * int_0
    var_1 = int_0 - int_0
    str_0 = 'zh_CN'
    module_0.set_default_locale(str_0)
    locale_0 = module_0.get()
    str_1 = locale_0.format_date(int_0)

def test_case_17():
    null_translations_0 = module_1.NullTranslations()
    str_0 = 'H<7Qn,E3<jYyj75&)'
    str_1 = '_rsL<5?T\rCK\'9B"p}OH\t'
    list_0 = [str_1]
    int_0 = -1828
    bool_0 = True
    locale_0 = module_0.get()
    str_2 = locale_0.friendly_number(int_0)
    var_0 = null_translations_0.pgettext(locale_0, locale_0)
    locale_1 = module_0.get(*list_0)
    locale_2 = module_0.get()
    str_3 = locale_2.format_date(int_0, bool_0)
    str_4 = None
    module_0.load_translations(str_4)
    null_translations_1 = module_1.NullTranslations()
    str_5 = 'yq}z|uq8h)s'
    gettext_locale_0 = module_0.GettextLocale(str_5, null_translations_1)
    null_translations_2 = module_1.NullTranslations()
    str_6 = locale_1.list(list_0)
    dict_0 = {}
    c_s_v_locale_0 = module_0.CSVLocale(str_3, dict_0)
    null_translations_3 = module_1.NullTranslations()
    str_7 = '.'
    module_0.load_translations(str_7)
    iterable_0 = module_0.get_supported_locales()
    module_0.load_gettext_translations(str_7, str_0)