# Automatically generated by Pynguin.
import ansible.module_utils.facts.system.distribution as module_0

def test_case_0():
    try:
        distribution_0 = None
        distribution_files_0 = module_0.DistributionFiles(distribution_0)
        var_0 = module_0.get_uname(distribution_files_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x81cX\x17\x91\x0f\x8e/\x93'
        set_0 = {bytes_0, bytes_0, bytes_0}
        distribution_fact_collector_0 = module_0.DistributionFactCollector(set_0)
        str_0 = '\x0b\rpO'
        distribution_0 = module_0.Distribution(str_0)
        float_0 = 0.2
        distribution_fact_collector_1 = module_0.DistributionFactCollector()
        var_0 = distribution_fact_collector_1.collect()
        list_0 = []
        distribution_files_0 = module_0.DistributionFiles(list_0)
        str_1 = '2]R6{H@m-a9uElX'
        bytes_1 = b'\xd4\x1e\xfe\xb1[\xa1\x97\x12\x84\x89\x918\x86R\xafM\xc5\xe9\x06'
        str_2 = ''
        distribution_files_1 = module_0.DistributionFiles(str_2)
        var_1 = distribution_files_1.parse_distribution_file_Alpine(distribution_files_0, distribution_files_0, str_1, bytes_1)
        distribution_files_2 = module_0.DistributionFiles(distribution_fact_collector_1)
        var_2 = distribution_files_2.parse_distribution_file_OpenWrt(bytes_0, distribution_fact_collector_0, float_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        distribution_files_0 = module_0.DistributionFiles(list_0)
        var_0 = distribution_files_0.process_dist_files()
        tuple_0 = None
        bool_0 = False
        bytes_0 = b'\xb7\x0e\xf73\xa5%_\x8b|j\x9c\xb3\x83\xf9#'
        str_0 = '47'
        var_1 = distribution_files_0.parse_distribution_file_NA(tuple_0, bool_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'wLVvx)VW1*2L\n9xq\r{D'
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        int_0 = 234
        float_0 = -1794.621
        dict_0 = {str_0: int_0, int_0: float_0, str_0: distribution_fact_collector_0}
        tuple_0 = ()
        distribution_files_0 = module_0.DistributionFiles(tuple_0)
        var_0 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, distribution_fact_collector_0, int_0, dict_0)
        str_1 = '%/b}uQBm4$g,tSeBXa'
        distribution_0 = module_0.Distribution(str_1)
        var_1 = distribution_0.get_distribution_OpenBSD()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '7LKL\\:~,gc~'
        distribution_0 = module_0.Distribution(str_0)
        var_0 = distribution_0.get_distribution_SunOS()
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        distribution_files_0 = module_0.DistributionFiles(list_0)
        var_0 = distribution_files_0.process_dist_files()
        distribution_0 = None
        distribution_1 = module_0.Distribution(distribution_0)
        var_1 = distribution_1.get_distribution_AIX()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dBsP'
        distribution_0 = module_0.Distribution(str_0)
        var_0 = distribution_0.get_distribution_HPUX()
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        distribution_0 = module_0.Distribution(list_0)
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        bytes_0 = b'b+\xf2&\xafM\xbc\xf4\xac\x95\x00\x1d\xcb\xe0'
        var_0 = distribution_fact_collector_0.collect(bytes_0)
        set_0 = {distribution_fact_collector_0, distribution_fact_collector_0}
        str_0 = 'rmdir'
        distribution_files_0 = module_0.DistributionFiles(str_0)
        var_1 = distribution_files_0.parse_distribution_file_Debian(distribution_fact_collector_0, set_0, bytes_0, bytes_0)
        var_2 = distribution_0.get_distribution_Darwin()
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        distribution_0 = module_0.Distribution(bool_0)
        distribution_1 = module_0.Distribution(distribution_0)
        var_0 = distribution_1.get_distribution_OpenBSD()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/opt/hpvm/bin/hpvminfo'
        distribution_0 = module_0.Distribution(str_0)
        var_0 = distribution_0.get_distribution_DragonFly()
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -527
        bytes_0 = None
        distribution_fact_collector_0 = module_0.DistributionFactCollector(bytes_0)
        distribution_0 = module_0.Distribution(distribution_fact_collector_0)
        str_0 = ')Z9U'
        tuple_0 = (str_0,)
        tuple_1 = (int_0, distribution_0, tuple_0)
        distribution_1 = module_0.Distribution(tuple_1)
        distribution_2 = module_0.Distribution(distribution_1)
        var_0 = distribution_2.get_distribution_NetBSD()
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = []
        bool_0 = None
        distribution_0 = module_0.Distribution(list_0)
        var_0 = module_0.get_uname(bool_0, distribution_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = 1782.6399
        set_0 = {float_0, float_0}
        str_0 = '5MFv,?}j'
        float_1 = 432.36
        list_0 = [float_0, set_0, float_1]
        str_1 = 'http_proxy'
        int_0 = 279
        distribution_files_0 = module_0.DistributionFiles(int_0)
        var_0 = distribution_files_0.parse_distribution_file_OpenWrt(set_0, str_0, list_0, str_1)
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        tuple_0 = ()
        var_1 = distribution_fact_collector_0.collect(tuple_0, float_0)
        distribution_fact_collector_1 = module_0.DistributionFactCollector(distribution_fact_collector_0)
        str_2 = ' recalculate inventory '
        tuple_1 = (str_2,)
        distribution_0 = module_0.Distribution(tuple_1)
        var_2 = distribution_0.get_distribution_SunOS()
    except BaseException:
        pass