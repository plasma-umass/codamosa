# Automatically generated by Pynguin.
import ansible.parsing.yaml.objects as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_0)
    var_0 = ansible_vault_encrypted_unicode_0.rstrip()

def test_case_2():
    str_0 = '?GCib\\'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.__eq__(str_0)

def test_case_3():
    bytes_0 = b'\xa9K[z\x99\x11\xe8'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
    var_0 = ansible_vault_encrypted_unicode_0.__reversed__()

def test_case_4():
    bytes_0 = b'\x89\xf1'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
    var_0 = ansible_vault_encrypted_unicode_1.is_encrypted()

def test_case_5():
    bytes_0 = b'\xda\x94T\x10\xe0\xf4<\xb5'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
    var_0 = ansible_vault_encrypted_unicode_0.__hash__()

def test_case_6():
    int_0 = -2238
    str_0 = "[(), '', '', ()]\n"
    list_0 = [str_0]
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(list_0)
    var_0 = ansible_vault_encrypted_unicode_0.__radd__(int_0)

def test_case_7():
    bytes_0 = b'P\rF/\xd3ha\xf9\xc4Pq'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
    var_0 = ansible_vault_encrypted_unicode_0.capitalize()

def test_case_8():
    ansible_mapping_0 = module_0.AnsibleMapping()
    list_0 = [ansible_mapping_0]
    list_1 = [list_0]
    str_0 = 'UnX\t@T'
    int_0 = -677
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
    var_0 = ansible_vault_encrypted_unicode_0.format_map(str_0)
    bool_0 = True
    list_2 = [list_1, list_1, list_0, bool_0]
    ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)
    ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_1)
    var_1 = ansible_vault_encrypted_unicode_2.__eq__(list_2)

def test_case_9():
    str_0 = '\n---\nmodule: get_url\nshort_description: Downloads files from HTTP, HTTPS, or FTP to node\ndescription:\n     - Downloads files from HTTP, HTTPS, or FTP to the remote server. The remote\n       server I(must) have direct access to the remote resource.\n     - By default, if an environment variable C(<protocol>_proxy) is set on\n       the target host, requests will be sent through that proxy. This\n       behaviour can be overridden by setting a variable for this task\n       (see R(setting the environment,playbooks_environment)),\n       or by using the use_proxy option.\n     - HTTP redirects can redirect from HTTP to HTTPS so you should be sure that\n       your proxy environment for both protocols is correct.\n     - From Ansible 2.4 when run with C(--check), it will do a HEAD request to validate the URL but\n       will not download the entire file or verify it against hashes.\n     - For Windows targets, use the M(ansible.windows.win_get_url) module instead.\nversion_added: \'0.6\'\noptions:\n  url:\n    description:\n      - HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path\n    type: str\n    required: true\n  dest:\n    description:\n      - Absolute path of where to download the file to.\n      - If C(dest) is a directory, either the server provided filename or, if\n        none provided, the base name of the URL on the remote server will be\n        used. If a directory, C(force) has no effect.\n      - If C(dest) is a directory, the file will always be downloaded\n        (regardless of the C(force) option), but replaced only if the contents changed..\n    type: path\n    required: true\n  tmp_dest:\n    description:\n      - Absolute path of where temporary file is downloaded to.\n      - When run on Ansible 2.5 or greater, path defaults to ansible\'s remote_tmp setting\n      - When run on Ansible prior to 2.5, it defaults to C(TMPDIR), C(TEMP) or C(TMP) env variables or a platform specific value.\n      - U(https://docs.python.org/3/library/tempfile.html#tempfile.tempdir)\n    type: path\n    version_added: \'2.1\'\n  force:\n    description:\n      - If C(yes) and C(dest) is not a directory, will download the file every\n        time and replace the file if the contents change. If C(no), the file\n        will only be downloaded if the destination does not exist. Generally\n        should be C(yes) only for small local files.\n      - Prior to 0.6, this module behaved as if C(yes) was the default.\n      - Alias C(thirsty) has been deprecated and will be removed in 2.13.\n    type: bool\n    default: no\n    aliases: [ thirsty ]\n    version_added: \'0.7\'\n  backup:\n    description:\n      - Create a backup file including the timestamp information so you can get\n        the original file back if you somehow clobbered it incorrectly.\n    type: bool\n    default: no\n    version_added: \'2.1\'\n  sha256sum:\n    description:\n      - If a SHA-256 checksum is passed to this parameter, the digest of the\n        destination file will be calculated after it is downloaded to ensure\n        its integrity and verify that the transfer completed successfully.\n        This option is deprecated and will be removed in version 2.14. Use\n        option C(checksum) instead.\n    default: \'\'\n    type: str\n    version_added: "1.3"\n  checksum:\n    description:\n      - \'If a checksum is passed to this parameter, the digest of the\n        destination file will be calculated after it is downloaded to ensure\n        its integrity and verify that the transfer completed successfully.\n        Format: <algorithm>:<checksum|url>, e.g. checksum="sha256:D98291AC[...]B6DC7B97",\n        checksum="sha256:http://example.com/path/sha256sum.txt"\'\n      - If you worry about portability, only the sha1 algorithm is available\n        on all platforms and python versions.\n      - The third party hashlib library can be installed for access to additional algorithms.\n      - Additionally, if a checksum is passed to this parameter, and the file exist under\n        the C(dest) location, the I(destination_checksum) would be calculated, and if\n        checksum equals I(destination_checksum), the file download would be skipped\n        (unless C(force) is true). If the checksum does not equal I(destination_checksum),\n        the destination file is deleted.\n    type: str\n    default: \'\'\n    version_added: "2.0"\n  use_proxy:\n    description:\n      - if C(no), it will not use a proxy, even if one is defined in\n        an environment variable on the target hosts.\n    type: bool\n    default: yes\n  validate_certs:\n    description:\n      - If C(no), SSL certificates will not be validated.\n      - This should only be used on personally controlled sites using self-signed certificates.\n    type: bool\n    default: yes\n  timeout:\n    description:\n      - Timeout in seconds for URL request.\n    type: int\n    default: 10\n    version_added: \'1.8\'\n  headers:\n    description:\n        - Add custom HTTP headers to a request in hash/dict format.\n        - The hash/dict format was added in Ansible 2.6.\n        - Previous versions used a C("key:value,key:value") string format.\n        - The C("key:value,key:value") string format is deprecated and has been removed in version 2.10.\n    type: dict\n    version_added: \'2.0\'\n  url_username:\n    description:\n      - The username for use in HTTP basic authentication.\n      - This parameter can be used without C(url_password) for sites that allow empty passwords.\n      - Since version 2.8 you can also use the C(username) alias for this option.\n    type: str\n    aliases: [\'username\']\n    version_added: \'1.6\'\n  url_password:\n    description:\n        - The password for use in HTTP basic authentication.\n        - If the C(url_username) parameter is not specified, the C(url_password) parameter will not be used.\n        - Since version 2.8 you can also use the \'password\' alias for this option.\n    type: str\n    aliases: [\'password\']\n    version_added: \'1.6\'\n  force_basic_auth:\n    description:\n      - Force the sending of the Basic authentication header upon initial request.\n      - httplib2, the library used by the uri module only sends authentication information when a webservice\n        responds to an initial request with a 401 status. Since some basic auth services do not properly\n        send a 401, logins will fail.\n    type: bool\n    default: no\n    version_added: \'2.0\'\n  client_cert:\n    description:\n      - PEM formatted certificate chain file to be used for SSL client authentication.\n      - This file can also include the key as well, and if the key is included, C(client_key) is not required.\n    type: path\n    version_added: \'2.4\'\n  client_key:\n    description:\n      - PEM formatted file that contains your private key to be used for SSL client authentication.\n      - If C(client_cert) contains both the certificate and key, this option is not required.\n    type: path\n    version_added: \'2.4\'\n  http_agent:\n    description:\n      - Header to identify as, generally appears in web server logs.\n    type: str\n    default: ansible-httpget\n  unredirected_headers:\n    description:\n      - A list of header names that will not be sent on subsequent redirected requests. This list is case\n        insensitive. By default all headers will be redirected. In some cases it may be beneficial to list\n        headers such as C(Authorization) here to avoid potential credential exposure.\n    default: []\n    type: list\n    elements: str\n    version_added: \'2.12\'\n  use_gssapi:\n    description:\n      - Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate\n        authentication.\n      - Requires the Python library L(gssapi,https://github.com/pythongssapi/python-gssapi) to be installed.\n      - Credentials for GSSAPI can be specified with I(url_username)/I(url_password) or with the GSSAPI env var\n        C(KRB5CCNAME) that specified a custom Kerberos credential cache.\n      - NTLM authentication is C(not) supported even if the GSSAPI mech for NTLM has been installed.\n    type: bool\n    default: no\n    version_added: \'2.11\'\n# informational: requirements for nodes\nextends_documentation_fragment:\n    - files\n    - action_common_attributes\nattributes:\n    check_mode:\n        support: full\n    diff_mode:\n        support: none\n    platform:\n        platforms: posix\nnotes:\n     - For Windows targets, use the M(ansible.windows.win_get_url) module instead.\nseealso:\n- module: ansible.builtin.uri\n- module: ansible.windows.win_get_url\nauthor:\n- Jan-Piet Mens (@jpmens)\n'
    dict_0 = {str_0: str_0, str_0: str_0}
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_0)
    var_0 = ansible_vault_encrypted_unicode_1.isalpha()
    ansible_mapping_0 = module_0.AnsibleMapping()
    ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
    var_1 = ansible_vault_encrypted_unicode_2.__repr__()
    bool_0 = True
    str_1 = '\n    A task is a language feature that represents a call to a module, with given arguments and other parameters.\n    A handler is a subclass of a task.\n\n    Usage:\n\n       Task.load(datastructure) -> Task\n       Task.something(...)\n    '
    list_0 = [str_1, str_1, str_1]
    ansible_vault_encrypted_unicode_3 = module_0.AnsibleVaultEncryptedUnicode(list_0)
    var_2 = ansible_vault_encrypted_unicode_3.splitlines(bool_0)

def test_case_10():
    str_0 = 'rz)A:`k9t*Zqg\r'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.isalnum()

def test_case_11():
    dict_0 = {}
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(dict_0)
    var_0 = ansible_vault_encrypted_unicode_0.isdecimal()

def test_case_12():
    str_0 = '~7Do`\x0c)oSbB'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.isdigit()

def test_case_13():
    bytes_0 = b'E\xdc\x1e\x1bTwh\x07\x95s\xbc'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
    var_0 = ansible_vault_encrypted_unicode_0.isnumeric()

def test_case_14():
    ansible_base_y_a_m_l_object_0 = module_0.AnsibleBaseYAMLObject()
    ansible_sequence_0 = module_0.AnsibleSequence()
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_sequence_0)
    var_0 = ansible_vault_encrypted_unicode_0.casefold()
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_base_y_a_m_l_object_0)
    set_0 = {ansible_vault_encrypted_unicode_1}
    var_1 = ansible_vault_encrypted_unicode_1.__eq__(set_0)
    ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_unicode_1)
    var_2 = ansible_vault_encrypted_unicode_2.isidentifier()
    var_3 = ansible_vault_encrypted_unicode_2.__len__()
    var_4 = ansible_vault_encrypted_unicode_0.isspace()
    str_0 = 'alert'
    var_5 = ansible_vault_encrypted_unicode_1.title()
    ansible_unicode_0 = module_0.AnsibleUnicode()
    var_6 = ansible_vault_encrypted_unicode_1.__ne__(str_0)
    var_7 = ansible_vault_encrypted_unicode_2.expandtabs()

def test_case_15():
    ansible_unicode_0 = module_0.AnsibleUnicode()
    float_0 = 1.0
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
    var_0 = ansible_vault_encrypted_unicode_0.istitle()
    str_0 = '%s is %s but %s of the following are missing: %s'
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_1 = ansible_vault_encrypted_unicode_0.title()
    var_2 = ansible_vault_encrypted_unicode_1.rsplit()
    var_3 = ansible_vault_encrypted_unicode_1.rstrip()
    var_4 = ansible_vault_encrypted_unicode_1.__ne__(ansible_unicode_0)

def test_case_16():
    str_0 = 'myasso'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.replace(ansible_vault_encrypted_unicode_0, ansible_vault_encrypted_unicode_0)

def test_case_17():
    int_0 = -2560
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
    var_0 = ansible_vault_encrypted_unicode_0.splitlines()

def test_case_18():
    float_0 = 380.0
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
    var_0 = ansible_vault_encrypted_unicode_0.upper()

def test_case_19():
    dict_0 = {}
    str_0 = 'RP~r[3B5r'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.islower()
    var_1 = ansible_vault_encrypted_unicode_0.upper()
    str_1 = 'eLLMh=='
    var_2 = ansible_vault_encrypted_unicode_0.__contains__(str_1)
    var_3 = ansible_vault_encrypted_unicode_0.isalpha()
    ansible_unicode_0 = module_0.AnsibleUnicode(**dict_0)
    int_0 = 532
    ansible_sequence_0 = module_0.AnsibleSequence(**dict_0)
    var_4 = ansible_vault_encrypted_unicode_0.is_encrypted()
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(ansible_sequence_0)
    var_5 = ansible_vault_encrypted_unicode_1.zfill(int_0)

def test_case_20():
    str_0 = 'mypassword'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    str_1 = 'nopassword'
    var_0 = ansible_vault_encrypted_unicode_0.replace(str_0, str_1)
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(str_1)
    var_1 = ansible_vault_encrypted_unicode_0.replace(ansible_vault_encrypted_unicode_1, ansible_vault_encrypted_unicode_2)

def test_case_21():
    bytes_0 = b'\x83Bu)\xce\x15\xaf\x90'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bytes_0)
    var_0 = ansible_vault_encrypted_unicode_0.strip()

def test_case_22():
    str_0 = ''
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.__ne__(str_0)

def test_case_23():
    int_0 = 2147
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
    var_0 = ansible_vault_encrypted_unicode_0.__len__()

def test_case_24():
    int_0 = -3125
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(int_0)
    var_0 = ansible_vault_encrypted_unicode_0.isidentifier()

def test_case_25():
    str_0 = "]Y,~>4V'ug\rO<=P"
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.lower()

def test_case_26():
    str_0 = '<ansible.parsing.yaml.objects.AnsibleBaseYAMLObject object at 0x7f7bb08a0400>'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.lstrip()

def test_case_27():
    float_0 = 4122.15
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(float_0)
    var_0 = ansible_vault_encrypted_unicode_0.casefold()

def test_case_28():
    ansible_sequence_0 = module_0.AnsibleSequence()
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_sequence_0)
    var_0 = ansible_vault_encrypted_unicode_0.isascii()

def test_case_29():
    bool_0 = True
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(bool_0)
    var_0 = ansible_vault_encrypted_unicode_0.format()

def test_case_30():
    str_0 = 'abc'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    str_1 = 'X'
    var_0 = ansible_vault_encrypted_unicode_0 + str_1
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_1 = str_1 + ansible_vault_encrypted_unicode_1

def test_case_31():
    str_0 = '$ANSIBLE_VAULT;1.1;AES256\n37333136623933356665393463396365316532386536633162326639626262363663323066653834\n38306632653939376136343036663533333236393931346235653763386161323133653436346135\n363063623237623865663638353734303734\n'
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.is_encrypted()

def test_case_32():
    ansible_unicode_0 = module_0.AnsibleUnicode()
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_unicode_0)
    var_0 = ansible_vault_encrypted_unicode_0.__unicode__()

def test_case_33():
    ansible_mapping_0 = module_0.AnsibleMapping()
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(ansible_mapping_0)
    var_0 = ansible_vault_encrypted_unicode_0.islower()

def test_case_34():
    str_0 = ''
    ansible_vault_encrypted_unicode_0 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_0 = ansible_vault_encrypted_unicode_0.find(str_0)
    str_1 = 'A'
    var_1 = ansible_vault_encrypted_unicode_0.find(str_1)
    ansible_vault_encrypted_unicode_1 = module_0.AnsibleVaultEncryptedUnicode(str_1)
    var_2 = ansible_vault_encrypted_unicode_1.find(str_0)
    var_3 = ansible_vault_encrypted_unicode_1.find(str_1)
    ansible_vault_encrypted_unicode_2 = module_0.AnsibleVaultEncryptedUnicode(str_0)
    var_4 = ansible_vault_encrypted_unicode_1.find(ansible_vault_encrypted_unicode_2)