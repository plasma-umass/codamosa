# Automatically generated by Pynguin.
import mimesis.builtins.en as module_0

def test_case_0():
    try:
        u_s_a_spec_provider_0 = module_0.USASpecProvider()
        str_0 = u_s_a_spec_provider_0.ssn()
        str_1 = u_s_a_spec_provider_0.tracking_number(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        u_s_a_spec_provider_0 = module_0.USASpecProvider()
        str_0 = u_s_a_spec_provider_0.ssn()
        str_1 = u_s_a_spec_provider_0.ssn()
        str_2 = '*0>"t!PpSP'
        var_0 = u_s_a_spec_provider_0.personality()
        var_1 = u_s_a_spec_provider_0.personality()
        str_3 = u_s_a_spec_provider_0.tracking_number()
        var_2 = u_s_a_spec_provider_0.personality(str_2)
        str_4 = "Fq7w79a3=:EkfaVzO'lO"
        str_5 = 'IS$T2'
        var_3 = u_s_a_spec_provider_0.personality(str_5)
        str_6 = '!.,`nNGb!g+)0&7\x0c.=p'
        str_7 = u_s_a_spec_provider_0.ssn()
        var_4 = u_s_a_spec_provider_0.personality(str_6)
        u_s_a_spec_provider_1 = module_0.USASpecProvider(str_2)
        str_8 = u_s_a_spec_provider_0.ssn()
        str_9 = u_s_a_spec_provider_1.tracking_number(str_4)
    except BaseException:
        pass