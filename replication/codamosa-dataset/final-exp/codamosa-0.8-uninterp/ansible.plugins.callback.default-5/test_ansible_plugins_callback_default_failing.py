# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0
import ansible.playbook.task_include as module_1

def test_case_0():
    try:
        callback_module_0 = module_0.CallbackModule()
        dict_0 = {}
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_notify(callback_module_0, dict_0)
        callback_module_2 = module_0.CallbackModule()
        var_1 = callback_module_1.set_options()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Failed to remove role %s: %s'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '/m>-%Nv6n*MK*E'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callback_module_0 = module_0.CallbackModule()
        float_0 = 853.51
        var_0 = callback_module_0.v2_runner_on_skipped(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xcf\x18\xdd\x00\xccv\x9a\xfdlim\xde\xf2\xed\x16\xa8\x10'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_unreachable(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_matched()
        callback_module_1 = module_0.CallbackModule()
        float_0 = 50.108531
        tuple_0 = (callback_module_1, float_0)
        var_1 = callback_module_1.v2_playbook_on_stats(tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
        float_0 = -994.0479855361398
        bool_0 = False
        var_1 = callback_module_0.v2_playbook_on_notify(float_0, bool_0)
        bytes_0 = None
        var_2 = callback_module_0.v2_playbook_on_start(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        callback_module_0 = module_0.CallbackModule()
        list_0 = [callback_module_0, callback_module_0, callback_module_0, callback_module_0]
        bool_0 = False
        var_0 = callback_module_0.v2_playbook_on_task_start(list_0, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(callback_module_0)
    except BaseException:
        pass

def test_case_9():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = ''
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        tuple_0 = None
        bytes_0 = b'\x051\xbaS<&\xa3\x82\xaa\x0e\xd1L'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_start(tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        callback_module_0 = module_0.CallbackModule()
        bytes_0 = None
        tuple_0 = (bytes_0,)
        var_0 = callback_module_0.v2_playbook_on_notify(tuple_0, tuple_0)
        float_0 = 0.0
        var_1 = callback_module_0.v2_runner_item_on_failed(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        callback_module_0 = module_0.CallbackModule()
        dict_0 = {}
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_notify(callback_module_0, dict_0)
        callback_module_2 = module_0.CallbackModule()
        var_1 = callback_module_2.v2_runner_item_on_skipped(bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = -1883
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        callback_module_0 = module_0.CallbackModule()
        bytes_0 = b'\x85\x9da\x98'
        var_0 = callback_module_0.v2_playbook_on_start(bytes_0)
    except BaseException:
        pass

def test_case_15():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_matched()
        str_0 = 'h-Xss\x0b8.g.'
        tuple_0 = (str_0,)
        var_1 = callback_module_0.v2_runner_retry(tuple_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 2669
        callback_module_0 = module_0.CallbackModule()
        set_0 = {int_0, int_0, int_0, int_0}
        float_0 = -1046.2
        bool_0 = False
        var_0 = callback_module_0.v2_playbook_on_notify(float_0, bool_0)
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_0.v2_runner_on_async_poll(set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = -1675.46
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_failed(float_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 2350
        list_0 = [int_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_item_on_ok(list_0)
    except BaseException:
        pass

def test_case_19():
    try:
        callback_module_0 = module_0.CallbackModule()
        dict_0 = {}
        var_0 = callback_module_0.v2_runner_on_async_ok(dict_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '>c j;fvjv%\x0b@'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_on_file_diff(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        task_include_0 = module_1.TaskInclude()
        var_0 = task_include_0.get_dep_chain()
        callback_module_0 = module_0.CallbackModule()
        var_1 = callback_module_0.v2_playbook_on_play_start(task_include_0)
        list_0 = [task_include_0]
        tuple_0 = (list_0,)
        var_2 = callback_module_0.v2_playbook_on_notify(callback_module_0, tuple_0)
        bytes_0 = b'7\xbb\xeb^\xb6\xe2\xd3\xc5\xf3R\x92\x03\xd0\xd5'
        var_3 = callback_module_0.v2_playbook_on_task_start(task_include_0, bytes_0)
    except BaseException:
        pass