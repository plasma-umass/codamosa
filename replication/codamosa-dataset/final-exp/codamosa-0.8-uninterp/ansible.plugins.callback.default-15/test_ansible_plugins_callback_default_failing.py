# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0
import ansible.playbook.task_include as module_1

def test_case_0():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        int_0 = 1401
        var_0 = callback_module_1.set_options(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'n\xe0\x05\x94\xe7\xfa\x01<\xfbFHx_{$\x0b'
        str_0 = 'zzmJ'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(bytes_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        bytes_0 = b'"'
        var_0 = callback_module_0.v2_runner_on_skipped(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callback_module_0 = module_0.CallbackModule()
        bytes_0 = b'-5kyw\xe5\xc6'
        var_0 = callback_module_0.v2_runner_on_unreachable(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_0.v2_playbook_on_no_hosts_matched()
        var_2 = callback_module_1.v2_playbook_on_cleanup_task_start(callback_module_1)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = set()
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_task_start(bool_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/1%['
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\x0c/5oSh:=i<'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_play_start(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_on_file_diff(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 0
        bytes_0 = b'\xc9J\xd9\xe5\x95\xec8\xe1\xdfsu2,\xd7'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_notify(int_0, bytes_0)
        callback_module_1 = module_0.CallbackModule()
        str_0 = 'M\t'
        var_1 = callback_module_1.v2_runner_item_on_ok(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '@$1\tp>_*mX'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_item_on_failed(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        callback_module_0 = module_0.CallbackModule()
        float_0 = 601.0
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_item_on_skipped(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        callback_module_0 = module_0.CallbackModule()
        bytes_0 = b'\x1cx\x97\xe9\x8c\x01\xae(\xf4\x7f7w\x18\xd0(\\'
        var_0 = callback_module_0.v2_playbook_on_stats(bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_start(callback_module_0)
    except BaseException:
        pass

def test_case_15():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = -2583
        var_0 = callback_module_0.v2_runner_retry(int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = -2924.875583
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_poll(float_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'N;dU\x0b/(rM(G.y'
        str_1 = 'PSRP FETCH %s to %s (offset=%d'
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_notify(str_1, bool_0)
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_1.v2_runner_on_async_ok(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        tuple_0 = ()
        list_0 = []
        tuple_1 = (tuple_0, list_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_failed(tuple_1)
    except BaseException:
        pass

def test_case_19():
    try:
        callback_module_0 = None
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_ok(callback_module_0)
    except BaseException:
        pass

def test_case_20():
    try:
        callback_module_0 = module_0.CallbackModule()
        bytes_0 = b'mr\xb2\xfb\xdfQ\xe9\xa0!\x7f1\xe9s!\x9bZHa'
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(bytes_0)
    except BaseException:
        pass

def test_case_21():
    try:
        callback_module_0 = module_0.CallbackModule()
        list_0 = [callback_module_0, callback_module_0]
        str_0 = '3R,=Z"V$w&)`;ql_'
        var_0 = callback_module_0.v2_runner_on_start(list_0, str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        callback_module_0 = module_0.CallbackModule()
        dict_0 = {}
        str_0 = 'C]/R:\r3rExU1{q{-%'
        var_0 = callback_module_0.v2_playbook_on_notify(dict_0, str_0)
        int_0 = 1
        task_include_0 = module_1.TaskInclude(int_0)
        var_1 = callback_module_0.v2_playbook_on_handler_task_start(task_include_0)
    except BaseException:
        pass