# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    pass

def test_case_1():
    keycloak_token_0 = module_0.KeycloakToken()

def test_case_2():
    galaxy_token_0 = module_0.GalaxyToken()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_4():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_5():
    bool_0 = False
    basic_auth_token_0 = module_0.BasicAuthToken(bool_0)
    var_0 = basic_auth_token_0.get()

def test_case_6():
    keycloak_token_0 = None
    list_0 = [keycloak_token_0, keycloak_token_0, keycloak_token_0]
    basic_auth_token_0 = module_0.BasicAuthToken(list_0)
    var_0 = basic_auth_token_0.headers()

def test_case_7():
    no_token_sentinel_0 = module_0.NoTokenSentinel()
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.set(no_token_sentinel_0)
    str_0 = ' create an options parser for bin/ansible '
    galaxy_token_1 = module_0.GalaxyToken(str_0)
    var_1 = galaxy_token_1.save()
    var_2 = galaxy_token_1.save()
    var_3 = galaxy_token_1.get()

def test_case_8():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()