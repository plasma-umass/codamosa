# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    try:
        list_0 = []
        base_0 = module_0.Base(*list_0)
        str_0 = base_0.domain()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "7mV6Jj'p>\nbbRz|!"
        str_1 = None
        base_0 = module_0.get_hvcs()
        bool_0 = base_0.check_build_status(str_0, str_1, str_0)
        gitlab_0 = module_0.Gitlab()
        optional_0 = gitlab_0.token()
        optional_1 = gitlab_0.token()
        base_1 = module_0.get_hvcs()
        base_2 = module_0.Base()
        str_2 = base_2.api_url()
    except BaseException:
        pass

def test_case_2():
    try:
        base_0 = module_0.Base()
        optional_0 = base_0.token()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'o>4#=ezk!='
        str_1 = '4[Qy,FoRz{rDP`OGMW37'
        github_0 = module_0.Github()
        str_2 = github_0.domain()
        github_1 = module_0.Github()
        bool_0 = github_1.check_build_status(str_0, str_0, str_1)
        str_3 = github_1.domain()
        session_0 = github_1.session()
        str_4 = 'oRJ1^aV~P_"Wzw2)'
        base_0 = module_0.Base()
        bool_1 = base_0.check_build_status(str_1, str_4, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        optional_0 = module_0.get_token()
        float_0 = 4126.8805
        token_auth_0 = module_0.TokenAuth(float_0)
        github_0 = None
        str_0 = 'e-uoZPPb9eT+x7Et$\x0c['
        str_1 = '#YY'
        str_2 = None
        bool_0 = module_0.post_changelog(str_1, str_0, str_2, str_0)
        gitlab_0 = module_0.Gitlab()
        tuple_0 = (github_0, str_0, gitlab_0)
        var_0 = token_auth_0.__call__(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        base_0 = module_0.get_hvcs()
        str_1 = '^YjPa-^O8~7:Z!^%B'
        gitlab_0 = module_0.Gitlab()
        bool_0 = gitlab_0.check_build_status(str_1, str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dist'
        str_1 = 'wC\\L`-+Wur!n]=@""o'
        bool_0 = module_0.upload_to_release(str_0, str_0, str_0, str_1)
        optional_0 = module_0.get_domain()
        str_2 = 'bump'
        github_0 = module_0.Github()
        session_0 = github_0.session()
        list_0 = [optional_0, str_2]
        token_auth_0 = module_0.TokenAuth(list_0)
        var_0 = token_auth_0.__call__(session_0)
        gitlab_0 = module_0.Gitlab()
        token_auth_1 = module_0.TokenAuth(gitlab_0)
        optional_1 = gitlab_0.token()
        dict_0 = {str_2: str_2}
        base_0 = module_0.Base(**dict_0)
    except BaseException:
        pass