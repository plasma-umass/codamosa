# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    try:
        keycloak_token_0 = module_0.KeycloakToken()
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_1():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.set(galaxy_token_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        basic_auth_token_0 = module_0.BasicAuthToken(bool_0)
        var_0 = basic_auth_token_0.get()
        var_1 = basic_auth_token_0.headers()
        galaxy_token_0 = module_0.GalaxyToken()
        var_2 = galaxy_token_0.get()
        var_3 = galaxy_token_0.set(galaxy_token_0)
    except BaseException:
        pass

def test_case_3():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.headers()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'foo'
        str_1 = 'http://example.org'
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1)
        var_0 = keycloak_token_0.get()
    except BaseException:
        pass