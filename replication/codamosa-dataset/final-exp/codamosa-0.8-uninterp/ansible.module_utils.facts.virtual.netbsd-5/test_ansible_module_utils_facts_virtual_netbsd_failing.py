# Automatically generated by Pynguin.
import ansible.module_utils.facts.virtual.netbsd as module_0

def test_case_0():
    try:
        bytes_0 = b'ts@\x0f\xd7'
        net_b_s_d_virtual_0 = module_0.NetBSDVirtual(bytes_0)
        var_0 = net_b_s_d_virtual_0.get_virtual_facts()
    except BaseException:
        pass