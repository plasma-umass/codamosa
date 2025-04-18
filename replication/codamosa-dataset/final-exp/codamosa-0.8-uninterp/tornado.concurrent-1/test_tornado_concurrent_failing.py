# Automatically generated by Pynguin.
import concurrent.futures._base as module_0
import tornado.concurrent as module_1
import _asyncio as module_2

def test_case_0():
    try:
        future_0 = module_0.Future()
        bool_0 = module_1.is_future(future_0)
        future_1 = module_2.Future()
    except BaseException:
        pass

def test_case_1():
    try:
        base_exception_0 = None
        list_0 = [base_exception_0, base_exception_0]
        dict_0 = {}
        dummy_executor_0 = module_1.DummyExecutor(**dict_0)
        future_0 = dummy_executor_0.submit(base_exception_0, *list_0)
        none_type_0 = None
        none_type_1 = None
        tuple_0 = (none_type_0, base_exception_0, none_type_1)
        module_1.future_set_exc_info(future_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callable_0 = module_1.run_on_executor()
        bool_0 = module_1.is_future(callable_0)
        future_0 = module_0.Future()
        int_0 = 783
        module_1.future_add_done_callback(future_0, int_0)
        dummy_executor_0 = module_1.DummyExecutor()
        future_1 = None
        module_1.chain_future(future_1, future_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Flexible routing implementation.\n\nTornado routes HTTP requests to appropriate handlers using `Router`\nclass implementations. The `tornado.web.Application` class is a\n`Router` implementation and may be used directly, or the classes in\nthis module may be used for additional flexibility. The `RuleRouter`\nclass can match on more criteria than `.Application`, or the `Router`\ninterface can be subclassed for maximum customization.\n\n`Router` interface extends `~.httputil.HTTPServerConnectionDelegate`\nto provide additional routing capabilities. This also means that any\n`Router` implementation can be used directly as a ``request_callback``\nfor `~.httpserver.HTTPServer` constructor.\n\n`Router` subclass must implement a ``find_handler`` method to provide\na suitable `~.httputil.HTTPMessageDelegate` instance to handle the\nrequest:\n\n.. code-block:: python\n\n    class CutomRouter(Router):\n        def find_handler(self, request, **kwargs):\n            # some routing logic providing a suitable HTTPMessageDelegate instance\n            return MessageDelegate(request.connection)\n\n    class MessageDelegate(HTTPMessageDelegate):\n        def __init__(self, connection):\n            self.connection = connection\n\n        def finish(self):\n            self.connection.write_headers(\n                ResponseStartLine("HTTP/1.1", 200, "OK"),\n                HTTPHeaders({"Content-Length": "2"}),\n                b"OK")\n            self.connection.finish()\n\n    router = CustomRouter()\n    server = HTTPServer(router)\n\nThe main responsibility of `Router` implementation is to provide a\nmapping from a request to `~.httputil.HTTPMessageDelegate` instance\nthat will handle this request. In the example above we can see that\nrouting is possible even without instantiating an `~.web.Application`.\n\nFor routing to `~.web.RequestHandler` implementations we need an\n`~.web.Application` instance. `~.web.Application.get_handler_delegate`\nprovides a convenient way to create `~.httputil.HTTPMessageDelegate`\nfor a given request and `~.web.RequestHandler`.\n\nHere is a simple example of how we can we route to\n`~.web.RequestHandler` subclasses by HTTP method:\n\n.. code-block:: python\n\n    resources = {}\n\n    class GetResource(RequestHandler):\n        def get(self, path):\n            if path not in resources:\n                raise HTTPError(404)\n\n            self.finish(resources[path])\n\n    class PostResource(RequestHandler):\n        def post(self, path):\n            resources[path] = self.request.body\n\n    class HTTPMethodRouter(Router):\n        def __init__(self, app):\n            self.app = app\n\n        def find_handler(self, request, **kwargs):\n            handler = GetResource if request.method == "GET" else PostResource\n            return self.app.get_handler_delegate(request, handler, path_args=[request.path])\n\n    router = HTTPMethodRouter(Application())\n    server = HTTPServer(router)\n\n`ReversibleRouter` interface adds the ability to distinguish between\nthe routes and reverse them to the original urls using route\'s name\nand additional arguments. `~.web.Application` is itself an\nimplementation of `ReversibleRouter` class.\n\n`RuleRouter` and `ReversibleRuleRouter` are implementations of\n`Router` and `ReversibleRouter` interfaces and can be used for\ncreating rule-based routing configurations.\n\nRules are instances of `Rule` class. They contain a `Matcher`, which\nprovides the logic for determining whether the rule is a match for a\nparticular request and a target, which can be one of the following.\n\n1) An instance of `~.httputil.HTTPServerConnectionDelegate`:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(PathMatches("/handler"), ConnectionDelegate()),\n        # ... more rules\n    ])\n\n    class ConnectionDelegate(HTTPServerConnectionDelegate):\n        def start_request(self, server_conn, request_conn):\n            return MessageDelegate(request_conn)\n\n2) A callable accepting a single argument of `~.httputil.HTTPServerRequest` type:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(PathMatches("/callable"), request_callable)\n    ])\n\n    def request_callable(request):\n        request.write(b"HTTP/1.1 200 OK\\r\\nContent-Length: 2\\r\\n\\r\\nOK")\n        request.finish()\n\n3) Another `Router` instance:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(PathMatches("/router.*"), CustomRouter())\n    ])\n\nOf course a nested `RuleRouter` or a `~.web.Application` is allowed:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(HostMatches("example.com"), RuleRouter([\n            Rule(PathMatches("/app1/.*"), Application([(r"/app1/handler", Handler)])),\n        ]))\n    ])\n\n    server = HTTPServer(router)\n\nIn the example below `RuleRouter` is used to route between applications:\n\n.. code-block:: python\n\n    app1 = Application([\n        (r"/app1/handler", Handler1),\n        # other handlers ...\n    ])\n\n    app2 = Application([\n        (r"/app2/handler", Handler2),\n        # other handlers ...\n    ])\n\n    router = RuleRouter([\n        Rule(PathMatches("/app1.*"), app1),\n        Rule(PathMatches("/app2.*"), app2)\n    ])\n\n    server = HTTPServer(router)\n\nFor more information on application-level routing see docs for `~.web.Application`.\n\n.. versionadded:: 4.5\n\n'
        list_0 = [str_0, str_0]
        callable_0 = module_1.run_on_executor(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '8bwsW([i\n<t\x0b34y0O1wf'
        list_0 = [str_0]
        dict_0 = {str_0: str_0}
        callable_0 = module_1.run_on_executor(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Flexible routing implementation.\n\nTornado routes HTTP requests to appropriate handlers using `Router`\nclass implementations. The `tornado.web.Application` class is a\n`Router` implementation and may be used directly, or the classes in\nthis module may be used for additional flexibility. The `RuleRouter`\nclass can match on more criteria than `.Application`, or the `Router`\ninterface can be subclassed for maximum customization.\n\n`Router` interface extends `~.httputil.HTTPServerConnectionDelegate`\nto provide additional routing capabilities. This also means that any\n`Router` implementation can be used directly as a ``request_callback``\nfor `~.httpserver.HTTPServer` constructor.\n\n`Router` subclass must implement a ``find_handler`` method to provide\na suitable `~.httputil.HTTPMessageDelegate` instance to handle the\nrequest:\n\n.. code-block:: python\n\n    class CutomRouter(Router):\n        def find_handler(self, request, **kwargs):\n            # some routing logic providing a suitable HTTPMessageDelegate instance\n            return MessageDelegate(request.connection)\n\n    class MessageDelegate(HTTPMessageDelegate):\n        def __init__(self, connection):\n            self.connection = connection\n\n        def finish(self):\n            self.connection.write_headers(\n                ResponseStartLine("HTTP/1.1", 200, "OK"),\n                HTTPHeaders({"Content-Length": "2"}),\n                b"OK")\n            self.connection.finish()\n\n    router = CustomRouter()\n    server = HTTPServer(router)\n\nThe main responsibility of `Router` implementation is to provide a\nmapping from a request to `~.httputil.HTTPMessageDelegate` instance\nthat will handle this request. In the example above we can see that\nrouting is possible even without instantiating an `~.web.Application`.\n\nFor routing to `~.web.RequestHandler` implementations we need an\n`~.web.Application` instance. `~.web.Application.get_handler_delegate`\nprovides a convenient way to create `~.httputil.HTTPMessageDelegate`\nfor a given request and `~.web.RequestHandler`.\n\nHere is a simple example of how we can we route to\n`~.web.RequestHandler` subclasses by HTTP method:\n\n.. code-block:: python\n\n    resources = {}\n\n    class GetResource(RequestHandler):\n        def get(self, path):\n            if path not in resources:\n                raise HTTPError(404)\n\n            self.finish(resources[path])\n\n    class PostResource(RequestHandler):\n        def post(self, path):\n            resources[path] = self.request.body\n\n    class HTTPMethodRouter(Router):\n        def __init__(self, app):\n            self.app = app\n\n        def find_handler(self, request, **kwargs):\n            handler = GetResource if request.method == "GET" else PostResource\n            return self.app.get_handler_delegate(request, handler, path_args=[request.path])\n\n    router = HTTPMethodRouter(Application())\n    server = HTTPServer(router)\n\n`ReversibleRouter` interface adds the ability to distinguish between\nthe routes and reverse them to the original urls using route\'s name\nand additional arguments. `~.web.Application` is itself an\nimplementation of `ReversibleRouter` class.\n\n`RuleRouter` and `ReversibleRuleRouter` are implementations of\n`Router` and `ReversibleRouter` interfaces and can be used for\ncreating rule-based routing configurations.\n\nRules are instances of `Rule` class. They contain a `Matcher`, which\nprovides the logic for determining whether the rule is a match for a\nparticular request and a target, which can be one of the following.\n\n1) An instance of `~.httputil.HTTPServerConnectionDelegate`:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(PathMatches("/handler"), ConnectionDelegate()),\n        # ... more rules\n    ])\n\n    class ConnectionDelegate(HTTPServerConnectionDelegate):\n        def start_request(self, server_conn, request_conn):\n            return MessageDelegate(request_conn)\n\n2) A callable accepting a single argument of `~.httputil.HTTPServerRequest` type:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(PathMatches("/callable"), request_callable)\n    ])\n\n    def request_callable(request):\n        request.write(b"HTTP/1.1 200 OK\\r\\nContent-Length: 2\\r\\n\\r\\nOK")\n        request.finish()\n\n3) Another `Router` instance:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(PathMatches("/router.*"), CustomRouter())\n    ])\n\nOf course a nested `RuleRouter` or a `~.web.Application` is allowed:\n\n.. code-block:: python\n\n    router = RuleRouter([\n        Rule(HostMatches("example.com"), RuleRouter([\n            Rule(PathMatches("/app1/.*"), Application([(r"/app1/handler", Handler)])),\n        ]))\n    ])\n\n    server = HTTPServer(router)\n\nIn the example below `RuleRouter` is used to route between applications:\n\n.. code-block:: python\n\n    app1 = Application([\n        (r"/app1/handler", Handler1),\n        # other handlers ...\n    ])\n\n    app2 = Application([\n        (r"/app2/handler", Handler2),\n        # other handlers ...\n    ])\n\n    router = RuleRouter([\n        Rule(PathMatches("/app1.*"), app1),\n        Rule(PathMatches("/app2.*"), app2)\n    ])\n\n    server = HTTPServer(router)\n\nFor more information on application-level routing see docs for `~.web.Application`.\n\n.. versionadded:: 4.5\n\n'
        list_0 = [str_0]
        callable_0 = module_1.run_on_executor(*list_0)
        dict_0 = {}
        callable_1 = module_1.run_on_executor(**dict_0)
        future_0 = module_2.Future()
    except BaseException:
        pass

def test_case_6():
    try:
        future_0 = None
        module_1.chain_future(future_0, future_0)
    except BaseException:
        pass

def test_case_7():
    try:
        future_0 = module_0.Future()
        base_exception_0 = None
        callable_0 = None
        bool_0 = module_1.is_future(base_exception_0)
        module_1.future_set_exception_unless_cancelled(future_0, base_exception_0)
        module_1.future_add_done_callback(future_0, callable_0)
    except BaseException:
        pass