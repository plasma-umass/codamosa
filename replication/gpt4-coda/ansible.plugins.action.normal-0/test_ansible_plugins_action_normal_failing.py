# Automatically generated by Pynguin.
import ansible.plugins.action.normal as module_0

def test_case_0():
    try:
        float_0 = 1356.0
        tuple_0 = (float_0,)
        bytes_0 = b'\xdeH\x005i~'
        list_0 = [tuple_0, bytes_0]
        bytes_1 = b'p\x8b"\n{]\n\x86_l\xbb\x18rno[Z\xfb\xa8'
        action_module_0 = module_0.ActionModule(tuple_0, bytes_0, list_0, bytes_0, bytes_1, list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass