# Automatically generated by Pynguin.
import ansible.plugins.lookup.template as module_0

def test_case_0():
    try:
        bytes_0 = b'\x96\x06-\xba8\x03NE\xf8\x8d\xf3\xe0T\xda>\xc6j\xeb\xe9'
        str_0 = 'chassis-version'
        str_1 = '%:`04Q9-}v\x0c]b{Qzm'
        lookup_module_0 = module_0.LookupModule(str_1)
        var_0 = lookup_module_0.run(bytes_0, str_0)
    except BaseException:
        pass