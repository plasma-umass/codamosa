# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_finder as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()

def test_case_2():
    int_0 = 200000
    bytes_0 = b'\xb6\xe9$\xfd\x83\xee!gV'
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(int_0, bytes_0)

def test_case_3():
    int_0 = 200000
    bytes_0 = b'\xb6\xe9$\xfd\x83\xee!gV'
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(int_0, bytes_0)
    var_0 = ansible_path_hook_finder_0.__repr__()

def test_case_4():
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    bytes_0 = b'\xe8\xfe\xb9b\xbf\x82\x82O\x03o\x11\xbe\xb8K\xc5\xb2d\xdf&\xd4'
    var_0 = ansible_collection_finder_0.set_playbook_paths(bytes_0)

def test_case_5():
    str_0 = 'tests/units/utils/collection_loader/collections'
    str_1 = [str_0]
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder(str_1)

def test_case_6():
    str_0 = ''
    int_0 = -2220
    ansible_path_hook_finder_0 = module_0._AnsiblePathHookFinder(str_0, int_0)
    str_1 = ':8'
    var_0 = ansible_path_hook_finder_0.find_module(str_1)
    bool_0 = True
    var_1 = ansible_path_hook_finder_0.iter_modules(bool_0)

def test_case_7():
    str_0 = 'ns'
    ansible_collection_finder_0 = module_0._AnsibleCollectionFinder()
    var_0 = ansible_collection_finder_0.find_module(str_0)
    str_1 = 'Hl'
    var_1 = ansible_collection_finder_0.set_playbook_paths(str_1)

def test_case_8():
    str_0 = 'ansible_collections.alvaroaleman.product.plugins.modules.product.alvaroaleman_product'
    ansible_collection_pkg_loader_base_0 = module_0._AnsibleCollectionPkgLoaderBase(str_0, str_0)
    var_0 = ansible_collection_pkg_loader_base_0.get_code(str_0)