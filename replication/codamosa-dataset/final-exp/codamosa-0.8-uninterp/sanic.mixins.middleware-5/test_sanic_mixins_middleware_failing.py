# Automatically generated by Pynguin.
import sanic.mixins.middleware as module_0

def test_case_0():
    try:
        middleware_mixin_0 = module_0.MiddlewareMixin()
        var_0 = lambda r: r
        var_1 = middleware_mixin_0.middleware(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        middleware_mixin_0 = module_0.MiddlewareMixin()
        middleware_mixin_1 = module_0.MiddlewareMixin()
        var_0 = middleware_mixin_1.on_response()
        middleware_mixin_2 = module_0.MiddlewareMixin()
        var_1 = middleware_mixin_0.on_response(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        middleware_mixin_0 = module_0.MiddlewareMixin()
        int_0 = 174
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        var_0 = middleware_mixin_0.middleware(int_0, dict_0)
        var_1 = middleware_mixin_0.on_response()
        var_2 = middleware_mixin_0.on_request(var_0)
    except BaseException:
        pass