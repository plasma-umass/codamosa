# Automatically generated by Pynguin.
import tornado.locale as module_0
import gettext as module_1

def test_case_0():
    pass

def test_case_1():
    locale_0 = module_0.get()

def test_case_2():
    str_0 = '&PEz'
    module_0.set_default_locale(str_0)

def test_case_3():
    iterable_0 = module_0.get_supported_locales()

def test_case_4():
    str_0 = 'R:OL"w\x0cqg5bpyY`'
    str_1 = 'Lock'
    list_0 = [str_0, str_1]
    locale_0 = module_0.get(*list_0)

def test_case_5():
    str_0 = '~s'
    str_1 = '(y"0>Nft6.p1YE3A'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = None
    list_0 = [str_1, str_0, str_2]
    locale_0 = module_0.get(*list_0)

def test_case_6():
    str_0 = 'I'
    str_1 = "Abstract implementation of OAuth 2.0.\n\n    See `FacebookGraphMixin` or `GoogleOAuth2Mixin` below for example\n    implementations.\n\n    Class attributes:\n\n    * ``_OAUTH_AUTHORIZE_URL``: The service's authorization url.\n    * ``_OAUTH_ACCESS_TOKEN_URL``:  The service's access token url.\n    "
    list_0 = [str_0, str_0, str_0, str_1]
    locale_0 = module_0.get(*list_0)

def test_case_7():
    str_0 = None
    module_0.load_translations(str_0, str_0)
    locale_0 = module_0.get()

def test_case_8():
    int_0 = -2717
    locale_0 = module_0.get()
    str_0 = locale_0.friendly_number(int_0)

def test_case_9():
    str_0 = None
    str_1 = ':uT~c7((ye8LG'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = gettext_locale_0.translate(str_0)

def test_case_10():
    str_0 = ',c[6\rH!OV\t&^'
    dict_0 = {}
    str_1 = 'knL\rl%FHY\r|'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
    str_2 = gettext_locale_0.pgettext(str_0, str_0, str_0, dict_0)

def test_case_11():
    str_0 = 'Z0-;xaGpr}/H\x0bA96\x0bWYi'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = gettext_locale_0.pgettext(str_0, str_0)

def test_case_12():
    str_0 = '<qZAF7YI&fi['
    float_0 = 0.3
    str_1 = '6MV=0`9@E%~'
    dict_0 = {}
    c_s_v_locale_0 = module_0.CSVLocale(str_1, dict_0)
    str_2 = c_s_v_locale_0.translate(str_0, str_0, float_0)
    str_3 = 'D9\\4M'
    module_0.set_default_locale(str_3)

def test_case_13():
    int_0 = 1053
    bool_0 = True
    str_0 = 'Oi{Yxuh#'
    str_1 = '_pzkhw}x35p\\p/0\t['
    list_0 = [str_0, str_1]
    locale_0 = module_0.get(*list_0)
    str_2 = locale_0.format_date(int_0, int_0, bool_0)

def test_case_14():
    str_0 = 'R:OL"w\x0cqg5bpyY`'
    str_1 = 'Lock'
    locale_0 = module_0.get()
    str_2 = locale_0.list(str_0)
    list_0 = [str_0, str_1]
    locale_1 = module_0.get(*list_0)

def test_case_15():
    str_0 = '~I>,'
    iterable_0 = module_0.get_supported_locales()
    float_0 = -478.771165
    bool_0 = False
    module_0.set_default_locale(str_0)
    str_1 = ''
    str_2 = '?;xaxow,%j^^zcf}h\t'
    str_3 = '"3z\x0c!TY`]N"YG:A]UXgQ'
    str_4 = 'Called by libcurl when it wants to change the file descriptors\n        it cares about.\n        '
    dict_0 = {str_4: str_2}
    null_translations_0 = module_1.NullTranslations(dict_0)
    gettext_locale_0 = module_0.GettextLocale(str_3, null_translations_0)
    str_5 = gettext_locale_0.pgettext(str_1, str_2)
    list_0 = [str_3]
    locale_0 = module_0.get(*list_0)
    str_6 = locale_0.format_date(float_0, bool_0)
    dict_1 = {str_2: str_6}
    str_7 = 'DlW\x0cA#Ev-Nb)Q'
    dict_2 = {str_1: dict_1, str_7: dict_1, str_1: dict_1}
    c_s_v_locale_0 = module_0.CSVLocale(str_6, dict_2)
    int_0 = -39
    int_1 = -956
    str_8 = locale_0.list(str_1)
    str_9 = locale_0.friendly_number(int_1)
    str_10 = locale_0.friendly_number(int_0)
    str_11 = locale_0.list(str_6)
    str_12 = c_s_v_locale_0.translate(str_1, str_0, int_1)

def test_case_16():
    iterable_0 = module_0.get_supported_locales()
    float_0 = -478.771165
    bool_0 = False
    str_0 = 'TV8zwK!7eU'
    module_0.set_default_locale(str_0)
    str_1 = '\x0b'
    str_2 = '?;xaxow,%j^^zcf}h\t'
    list_0 = [str_0]
    locale_0 = module_0.get(*list_0)
    str_3 = locale_0.format_date(float_0, bool_0)
    dict_0 = {str_2: str_3}
    str_4 = 'Twitter OAuth authentication.\n\n    To authenticate with Twitter, register your application with\n    Twitter at http://twitter.com/apps. Then copy your Consumer Key\n    and Consumer Secret to the application\n    `~tornado.web.Application.settings` ``twitter_consumer_key`` and\n    ``twitter_consumer_secret``. Use this mixin on the handler for the\n    URL you registered as your application\'s callback URL.\n\n    When your application is set up, you can use this mixin like this\n    to authenticate the user with Twitter and get access to their stream:\n\n    .. testcode::\n\n        clas TwitterLoginHandler(tornado.web.RequestHandler,\n                                  tornado.auth.TwitterMixin):\n            async def get(self):\n                if self.get_argument("oauth_roken", None):\n                    user = await self.get_authenticated_user()\n                    # Save the user using e.g. set_secure_cookie()\n                else:\n                    await self.authorize_redirect()\n\n    .. testoutput::\n       :hide:\n\n    The user object returned by `~OAuthMixin.get_authenticated_user`\n    includes the attributes ``username``, ``name``, ``access_token``,\n    and all of the custom Twitter user attributes described at\n    https://dev.twitter.com/docs/api/1.1/get/users/show\n    '
    dict_1 = {str_1: dict_0, str_4: dict_0, str_1: dict_0}
    c_s_v_locale_0 = module_0.CSVLocale(str_3, dict_1)
    int_0 = -2717
    locale_1 = module_0.get()
    str_5 = locale_0.translate(str_0, str_4, int_0)

def test_case_17():
    str_0 = None
    module_0.load_translations(str_0, str_0)

def test_case_18():
    str_0 = ',c[6\rHq0!OVq&^'
    null_translations_0 = module_1.NullTranslations()
    gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
    str_1 = '~I>,'
    iterable_0 = module_0.get_supported_locales()
    iterable_1 = module_0.get_supported_locales()
    float_0 = -478.771165
    str_2 = '&^Mosn|`*Z2(;uN|/In)'
    int_0 = -480
    str_3 = 'Turkish'
    dict_0 = {}
    c_s_v_locale_0 = module_0.CSVLocale(str_3, dict_0)
    str_4 = c_s_v_locale_0.translate(str_2, str_1, int_0)
    bool_0 = False
    str_5 = '|\r~#7e9@)/'
    list_0 = [str_5]
    str_6 = 'opBnid.ns.oauth'
    gettext_locale_1 = module_0.GettextLocale(str_6, null_translations_0)
    locale_0 = module_0.get(*list_0)
    str_7 = locale_0.format_date(float_0, bool_0)
    str_8 = locale_0.list(str_5)
    str_9 = locale_0.pgettext(str_1, str_7)
    int_1 = -2140
    bool_1 = False
    bool_2 = True
    str_10 = locale_0.format_date(float_0, int_1, bool_0, bool_1, bool_2)
    int_2 = None
    int_3 = 24
    str_11 = locale_0.friendly_number(int_3)
    str_12 = None
    module_0.load_translations(str_12)
    int_4 = None
    str_13 = locale_0.friendly_number(int_4)
    str_14 = gettext_locale_0.pgettext(str_7, str_7, int_2)