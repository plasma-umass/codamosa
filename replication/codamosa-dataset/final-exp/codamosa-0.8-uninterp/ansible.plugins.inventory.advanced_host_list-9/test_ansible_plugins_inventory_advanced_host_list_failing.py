# Automatically generated by Pynguin.
import ansible.plugins.inventory.advanced_host_list as module_0

def test_case_0():
    try:
        list_0 = None
        inventory_module_0 = None
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.parse(inventory_module_0, inventory_module_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = []
        str_0 = '123.123.123.123'
        var_1 = inventory_module_0.parse(inventory_module_0, var_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = []
        str_0 = 'P}\\A8!b)^qFuX+v[4'
        var_1 = inventory_module_0.parse(inventory_module_0, var_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = []
        str_0 = 'I\rt1krK(Cn],rZaI.,'
        var_1 = inventory_module_0.verify_file(str_0)
        str_1 = 'svirify'
        var_2 = inventory_module_0.parse(inventory_module_0, var_0, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = []
        str_0 = '\n# The return information includes all the HTTP headers in lower-case.\ncontent:\n  description: The response body content.\n  returned: status not in status_code or return_content is true\n  type: str\n  sample: "{}"\ncookies:\n  description: The cookie values placed in cookie jar.\n  returned: on success\n  type: dict\n  sample: {"SESSIONID": "[SESSIONID]"}\n  version_added: "2.4"\ncookies_string:\n  description: The value for future request Cookie headers.\n  returned: on success\n  type: str\n  sample: "SESSIONID=[SESSIONID]"\n  version_added: "2.6"\nelapsed:\n  description: The number of seconds that elapsed while performing the download.\n  returned: on success\n  type: int\n  sample: 23\nmsg:\n  description: The HTTP message from the request.\n  returned: always\n  type: str\n  sample: OK (unknown bytes)\npath:\n  description: destination file/path\n  returned: dest is defined\n  type: str\n  sample: /path/to/file.txt\nredirected:\n  description: Whether the request was redirected.\n  returned: on success\n  type: bool\n  sample: false\nstatus:\n  description: The HTTP status code from the request.\n  returned: always\n  type: int\n  sample: 200\nurl:\n  description: The actual URL used for the request.\n  returned: always\n  type: str\n  sample: https://www.ansible.com/\n'
        var_1 = inventory_module_0.parse(inventory_module_0, var_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = []
        str_0 = ',cei@-ay'
        var_1 = inventory_module_0.parse(inventory_module_0, var_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = '0n'
        var_0 = inventory_module_0.verify_file(str_0)
        float_0 = -417.0
        inventory_module_1 = module_0.InventoryModule()
        list_0 = None
        str_1 = ''
        var_1 = inventory_module_0.parse(float_0, list_0, str_1)
        str_2 = '8K"'
        bytes_0 = b'KsK\x8f'
        var_2 = inventory_module_0.parse(str_2, inventory_module_0, bytes_0)
    except BaseException:
        pass