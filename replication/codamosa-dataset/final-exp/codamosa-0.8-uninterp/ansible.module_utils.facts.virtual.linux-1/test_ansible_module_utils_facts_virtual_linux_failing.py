# Automatically generated by Pynguin.
import ansible.module_utils.facts.virtual.linux as module_0

def test_case_0():
    try:
        int_0 = 2722
        linux_virtual_0 = module_0.LinuxVirtual(int_0)
        var_0 = linux_virtual_0.get_virtual_facts()
    except BaseException:
        pass