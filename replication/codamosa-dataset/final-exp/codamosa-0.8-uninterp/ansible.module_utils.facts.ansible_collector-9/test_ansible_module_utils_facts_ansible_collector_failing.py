# Automatically generated by Pynguin.
import ansible.module_utils.facts.ansible_collector as module_0

def test_case_0():
    try:
        str_0 = '*'
        bytes_0 = b'\xf1\xa2\xf7l\x13\xd2\xe2M\xaf'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        var_0 = collector_meta_data_collector_0.collect()
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(bytes_0)
        dict_0 = {ansible_fact_collector_0: ansible_fact_collector_0, ansible_fact_collector_0: bytes_0}
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(dict_0)
        var_1 = ansible_fact_collector_1.collect(str_0)
        str_1 = '[q0TzPO'
        float_0 = -1358.3148
        ansible_fact_collector_2 = module_0.AnsibleFactCollector()
        set_0 = {ansible_fact_collector_2, float_0, ansible_fact_collector_1, str_0}
        var_2 = module_0.get_ansible_collector(str_1, float_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        list_0 = [ansible_fact_collector_0, ansible_fact_collector_0, ansible_fact_collector_0]
        int_0 = -175
        int_1 = 4168
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(ansible_fact_collector_0, int_1)
        set_0 = {int_0, int_0, collector_meta_data_collector_0}
        var_0 = module_0.get_ansible_collector(list_0, int_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        list_0 = [int_0, int_0, int_0, int_0]
        int_1 = 784
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(int_1)
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(ansible_fact_collector_0)
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(list_0, ansible_fact_collector_0, collector_meta_data_collector_0)
        var_0 = ansible_fact_collector_1.collect()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        float_0 = -1334.18659
        tuple_0 = ()
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        bytes_0 = b'B\x9d'
        list_0 = [float_0, bool_0, bytes_0, tuple_0]
        str_0 = ' P`uA\n'
        var_0 = module_0.get_ansible_collector(bytes_0, list_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        str_0 = 'O'
        list_0 = [str_0]
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(bool_0, bool_0, str_0, list_0)
        var_0 = collector_meta_data_collector_0.collect()
        dict_0 = {}
        bytes_0 = b'\xe6A'
        tuple_0 = (bytes_0, bool_0)
        bool_1 = None
        str_1 = 'k:}}lm'
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_1)
        var_1 = collector_meta_data_collector_0.collect(tuple_0, bool_1)
        var_2 = collector_meta_data_collector_0.collect(dict_0)
        ansible_fact_collector_1 = module_0.AnsibleFactCollector()
        var_3 = ansible_fact_collector_1.collect()
        var_4 = ansible_fact_collector_1.collect()
        str_2 = None
        bool_2 = True
        tuple_1 = (bool_2,)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(str_2, tuple_1)
        list_1 = [str_2, tuple_1, tuple_1]
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(str_2, list_1)
        bytes_1 = b'z>'
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(list_0, bytes_1)
        var_5 = ansible_fact_collector_1.collect()
        dict_1 = {}
        var_6 = ansible_fact_collector_1.collect(dict_1)
        int_0 = 12
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(int_0, ansible_fact_collector_2)
        bytes_2 = b'\xd5\xb8\x00\x8a\xa7bV(\xb1\x87\x84\xd7\xf4\x06"K\x9b\xe0='
        float_0 = None
        var_7 = ansible_fact_collector_1.collect()
        collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(ansible_fact_collector_1, collector_meta_data_collector_0, dict_1)
        bytes_3 = b'\xeb)\xbf\xd3\x84\xdd\xa0'
        var_8 = module_0.get_ansible_collector(bytes_2, ansible_fact_collector_1, float_0, bytes_3, list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 411.2922
        bytes_0 = b'ZE\x02\x95'
        var_0 = module_0.get_ansible_collector(float_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Vj[]erlp;1_Ok.'
        dict_0 = {}
        set_0 = {str_0}
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(set_0)
        var_0 = ansible_fact_collector_0.collect(dict_0)
        int_0 = 128
        dict_1 = {int_0: int_0, int_0: int_0}
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(dict_1)
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(ansible_fact_collector_1)
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(ansible_fact_collector_0)
        var_1 = ansible_fact_collector_2.collect(collector_meta_data_collector_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -1446.09
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = [dict_0, dict_0]
        str_0 = ''
        var_0 = module_0.get_ansible_collector(str_0)
        str_1 = '*'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_0, list_0, float_0)
        str_2 = '77Ew&D\x0cF+#FgtTHe>27='
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_2)
        var_1 = ansible_fact_collector_0.collect()
        set_0 = {float_0, str_1, str_1}
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(set_0)
        var_2 = ansible_fact_collector_1.collect()
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(dict_0, list_0, str_1)
        bool_0 = False
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(bool_0)
        var_3 = ansible_fact_collector_2.collect()
        tuple_0 = (list_0,)
        float_1 = 100.0
        set_1 = {ansible_fact_collector_0}
        var_4 = module_0.get_ansible_collector(tuple_0, float_1, set_1)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -1446.09
        dict_0 = {}
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(dict_0)
        dict_1 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = [dict_1, dict_1]
        str_0 = ''
        var_0 = module_0.get_ansible_collector(str_0)
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_0, list_0, float_0)
        str_1 = "b}MMYl'qtN"
        set_0 = {float_0, str_1, str_1}
        ansible_fact_collector_1 = module_0.AnsibleFactCollector(set_0)
        var_1 = ansible_fact_collector_1.collect()
        ansible_fact_collector_2 = module_0.AnsibleFactCollector(dict_1, list_0, str_1)
        bool_0 = False
        ansible_fact_collector_3 = module_0.AnsibleFactCollector(bool_0)
        var_2 = ansible_fact_collector_2.collect()
        bytes_0 = b'\x08\xfe\x0cp\x06\xe0Fe\xc9\xd30\x9fZ'
        ansible_fact_collector_4 = module_0.AnsibleFactCollector(dict_1, bytes_0)
        ansible_fact_collector_5 = module_0.AnsibleFactCollector()
        collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(ansible_fact_collector_3)
        var_3 = ansible_fact_collector_2.collect()
        var_4 = ansible_fact_collector_5.collect(ansible_fact_collector_4)
        bytes_1 = b'\xbf(}\x0b\x85'
        ansible_fact_collector_6 = module_0.AnsibleFactCollector(bytes_1)
        str_2 = "KcE'"
        collector_meta_data_collector_3 = module_0.CollectorMetaDataCollector(str_2)
        ansible_fact_collector_7 = module_0.AnsibleFactCollector()
        var_5 = collector_meta_data_collector_3.collect(ansible_fact_collector_6)
        var_6 = collector_meta_data_collector_1.collect(float_0)
        var_7 = ansible_fact_collector_6.collect(float_0)
        var_8 = collector_meta_data_collector_3.collect()
        var_9 = collector_meta_data_collector_3.collect(collector_meta_data_collector_3)
        int_0 = None
        int_1 = 443
        bytes_2 = b'K\xf02?E\xe5:R\x93\x05f'
        var_10 = module_0.get_ansible_collector(list_0, int_1, dict_0, int_0, list_0, bytes_2)
    except BaseException:
        pass