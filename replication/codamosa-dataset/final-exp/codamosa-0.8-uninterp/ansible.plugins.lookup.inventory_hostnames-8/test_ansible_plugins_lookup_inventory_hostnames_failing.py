# Automatically generated by Pynguin.
import ansible.plugins.lookup.inventory_hostnames as module_0

def test_case_0():
    try:
        bytes_0 = b'\x03'
        str_0 = "2AY,.%=;l/^'$sSvm3"
        int_0 = -1381
        lookup_module_0 = module_0.LookupModule(int_0)
        var_0 = lookup_module_0.run(bytes_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'groups'
        str_1 = {str_0: str_0, str_0: str_0, str_0: str_0}
        str_2 = {str_0: str_0, str_0: str_1, str_0: str_0, str_0: str_1}
        var_0 = lookup_module_0.run(str_2, str_2)
    except BaseException:
        pass