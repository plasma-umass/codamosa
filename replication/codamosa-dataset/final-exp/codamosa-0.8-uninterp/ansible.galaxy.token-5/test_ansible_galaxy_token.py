# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    pass

def test_case_1():
    galaxy_token_0 = module_0.GalaxyToken()
    bool_0 = True
    keycloak_token_0 = module_0.KeycloakToken(galaxy_token_0, bool_0)
    var_0 = galaxy_token_0.headers()
    dict_0 = {keycloak_token_0: bool_0, bool_0: keycloak_token_0}
    list_0 = [bool_0]
    keycloak_token_1 = module_0.KeycloakToken(dict_0, list_0)
    no_token_sentinel_0 = module_0.NoTokenSentinel()

def test_case_2():
    galaxy_token_0 = module_0.GalaxyToken()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_4():
    basic_auth_token_0 = None
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.set(basic_auth_token_0)

def test_case_5():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.save()

def test_case_6():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_7():
    str_0 = 'apt-key'
    basic_auth_token_0 = module_0.BasicAuthToken(str_0)
    var_0 = basic_auth_token_0.get()

def test_case_8():
    str_0 = '/(D\x0b]QH:PE'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    basic_auth_token_0 = module_0.BasicAuthToken(dict_0)
    basic_auth_token_1 = module_0.BasicAuthToken(basic_auth_token_0)
    var_0 = basic_auth_token_1.headers()
    galaxy_token_0 = module_0.GalaxyToken()
    var_1 = galaxy_token_0.get()

def test_case_9():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()

def test_case_10():
    bool_0 = False
    float_0 = -172.31886
    basic_auth_token_0 = module_0.BasicAuthToken(bool_0, float_0)
    var_0 = basic_auth_token_0.get()