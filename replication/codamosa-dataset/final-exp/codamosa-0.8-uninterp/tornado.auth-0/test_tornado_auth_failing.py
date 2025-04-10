# Automatically generated by Pynguin.
import tornado.auth as module_0

def test_case_0():
    try:
        auth_error_0 = module_0.AuthError()
        open_id_mixin_0 = module_0.OpenIdMixin()
        async_h_t_t_p_client_0 = open_id_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        o_auth_mixin_0 = module_0.OAuthMixin(*list_0)
        twitter_mixin_0 = module_0.TwitterMixin()
        str_0 = "Parameters:\n\n        * ``pattern``: Regular expression to be matched. Any capturing\n          groups in the regex will be passed in to the handler's\n          get/post/etc methods as arguments (by keyword if named, by\n          position if unnamed. Named and unnamed capturing groups\n          may not be mixed in the same rule).\n\n        * ``handler``: `~.web.RequestHandler` subclass to be invoked.\n\n        * ``kwargs`` (optional): A dictionary of additional arguments\n          to be passed to the handler's constructor.\n\n        * ``name`` (optional): A name for this handler.  Used by\n          `~.web.Application.reverse_url`.\n\n        "
        str_1 = 'bK4db91d'
        str_2 = 'Translation methods for generating localized strings.\n\nTo load a locale and generate a translated string::\n\n    user_locale = tornado.locale.get("es_LA")\n    print(user_locale.translate("Sign out"))\n\n`tornado.locale.get()` returns the closest matching locale, not necessarily the\nspecific locale you requested. You can support pluralization with\nadditional arguments to `~Locale.translate()`, e.g.::\n\n    people = [...]\n    message = user_locale.translate(\n        "%(list)s is online", "%(list)s are online", len(people))\n    print(message % {"list": user_locale.list(people)})\n\nThe first string is chosen if ``len(people) == 1``, otherwise the second\nstring is chosen.\n\nApplications should call one of `load_translations` (which uses a simple\nCSV format) or `load_gettext_translations` (which uses the ``.mo`` format\nsupported by `gettext` and related tools).  If neither method is called,\nthe `Locale.translate` method will simply return the original string.\n'
        list_1 = [str_1]
        dict_0 = {str_0: twitter_mixin_0, str_1: str_1, str_2: list_1}
        any_0 = twitter_mixin_0.twitter_request(str_0, dict_0, dict_0)
        o_auth_mixin_1 = module_0.OAuthMixin()
        async_h_t_t_p_client_0 = o_auth_mixin_1.get_auth_http_client()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'H\'x=auu3"Ht?Ri[j'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'H\'x=auu3"Ht?Ri[j'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        o_auth2_mixin_0 = module_0.OAuth2Mixin(**dict_0)
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_5():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect()
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = None
        open_id_mixin_0 = module_0.OpenIdMixin()
        dict_1 = open_id_mixin_0.get_authenticated_user()
        str_0 = 'q'
        open_id_mixin_1 = module_0.OpenIdMixin()
        str_1 = '7mz'
        str_2 = 't- )'
        dict_2 = {}
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin(**dict_2)
        any_0 = facebook_graph_mixin_0.facebook_request(str_0)
        optional_0 = facebook_graph_mixin_0.get_authenticated_user(str_1, str_2, str_1, str_2)
        list_0 = [dict_0]
        str_3 = '!!-0=c'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(dict_0, list_0, str_3)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '@wm'
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'H\'x=auu3"Ht?Ri[j'
        list_0 = []
        o_auth2_mixin_0 = module_0.OAuth2Mixin(*list_0)
        bytes_0 = b'\x91\x08\xcf*\xc89G\x03p98i]\xae\x1b'
        o_auth_mixin_0 = module_0.OAuthMixin()
        str_1 = ')N}OOLR8j>x\x0bN'
        dict_0 = {str_0: bytes_0, str_0: o_auth_mixin_0, str_0: str_1}
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, str_0, dict_0, str_1)
    except BaseException:
        pass