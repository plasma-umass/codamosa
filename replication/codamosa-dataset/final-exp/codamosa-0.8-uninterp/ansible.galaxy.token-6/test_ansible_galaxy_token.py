# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    pass

def test_case_1():
    no_token_sentinel_0 = module_0.NoTokenSentinel()
    int_0 = 1552
    tuple_0 = (int_0,)
    basic_auth_token_0 = module_0.BasicAuthToken(no_token_sentinel_0, tuple_0)
    var_0 = basic_auth_token_0.get()

def test_case_2():
    keycloak_token_0 = module_0.KeycloakToken()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()

def test_case_4():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()

def test_case_5():
    str_0 = 'zip_longest'
    galaxy_token_0 = module_0.GalaxyToken(str_0)
    var_0 = galaxy_token_0.get()

def test_case_6():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.save()

def test_case_7():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_8():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_9():
    int_0 = 2629
    basic_auth_token_0 = module_0.BasicAuthToken(int_0)
    var_0 = basic_auth_token_0.headers()

def test_case_10():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()