# Automatically generated by Pynguin.
import sanic.mixins.middleware as module_0

def test_case_0():
    pass

def test_case_1():
    middleware_mixin_0 = module_0.MiddlewareMixin()

def test_case_2():
    int_0 = -3471
    list_0 = [int_0, int_0]
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.middleware(list_0)

def test_case_3():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_0.on_request()

def test_case_4():
    middleware_mixin_0 = module_0.MiddlewareMixin()
    middleware_mixin_1 = module_0.MiddlewareMixin()
    var_0 = middleware_mixin_1.on_response(middleware_mixin_0)