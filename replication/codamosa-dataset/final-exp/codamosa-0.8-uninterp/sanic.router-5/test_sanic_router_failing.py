# Automatically generated by Pynguin.
import sanic.router as module_0
import sanic_routing.router as module_1

def test_case_0():
    try:
        int_0 = -832
        bool_0 = False
        router_0 = module_0.Router(int_0, bool_0)
        var_0 = router_0.finalize()
    except BaseException:
        pass

def test_case_1():
    try:
        router_0 = module_0.Router()
        str_0 = '/a>O/lb>/<c>'
        str_1 = [str_0, router_0]
        list_0 = []
        callable_0 = None
        var_0 = router_0.add(str_0, list_0, callable_0, str_1, str_0)
        bool_0 = False
        base_router_0 = module_1.BaseRouter(str_1, bool_0)
    except BaseException:
        pass