====================================================
ansible-core 2.12 "Dazed and Confused" Release Notes
====================================================

.. contents:: Topics


v2.12.1
=======

Release Summary
---------------

| Release Date: 2021-12-06
| `Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`__


Minor Changes
-------------

- jinja2_native - keep same behavior on Python 3.10.

Bugfixes
--------

- Ansible.ModuleUtils.LinkUtil - Ignore the ``LIB`` environment variable when loading the ``LinkUtil`` code
- ansible-test - Automatic target requirements installation is now based on the target environment instead of the controller environment.
- ansible-test - Fix Python real prefix detection when running in a ``venv`` virtual environment.
- ansible-test - Fix installation and usage of ``pyyaml`` requirement for the ``import`` sanity test for collections.
- ansible-test - Fix traceback in ``import`` sanity test on Python 2.7 when ``pip`` is not available.
- ansible-test - Relocate constants to eliminate symlink.
- ansible-test - Target integration test requirements are now correctly installed for target environments running on the controller.
- ansible-test - Update the ``default`` containers to version 4.1.1, which includes the updated ``import`` sanity test requirements.
- ansible-test - Use the legacy collection loader for ``import`` sanity tests on target-only Python versions.
- set_fact/include_vars correctly handle delegation assignments within loops
- setup - detect docker container with check for ./dockerenv or ./dockinit (https://github.com/ansible/ansible/pull/74349).
- validate_argument_spec - Skip suboption validation if the top level option is an invalid type (https://github.com/ansible/ansible/issues/75612).

v2.12.0
=======

Release Summary
---------------

| Release Date: 2021-11-05
| `Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`__


Major Changes
-------------

- Python Controller Requirement - Python 3.8 or newer is required for the control node (the machine that runs Ansible) (https://github.com/ansible/ansible/pull/74013)
- ansible-test - All "cloud" plugins which use containers can now be used with all POSIX and Windows hosts. Previously the plugins did not work with Windows at all, and support for hosts created with the ``--remote`` option was inconsistent.
- ansible-test - Collections can now specify controller and target specific integration test requirements and constraints. If provided, they take precedence over the previously available requirements and constraints files.
- ansible-test - Integration tests run with the ``integration`` command can now be executed on two separate hosts instead of always running on the controller. The target host can be one provided by ``ansible-test`` or by the user, as long as it is accessible using SSH.
- ansible-test - Most container features are now supported under Podman. Previously a symbolic link for ``docker`` pointing to ``podman`` was required.
- ansible-test - New ``--controller`` and ``--target`` / ``--target-python`` options have been added to allow more control over test environments.
- ansible-test - Python 3.8 - 3.10 are now required to run ``ansible-test``, thus matching the Ansible controller Python requirements. Older Python versions (2.6 - 2.7 and 3.5 - 3.10) can still be the target for relevant tests.
- ansible-test - SSH port forwarding and redirection is now used exclusively to make container ports available on non-container hosts. When testing on POSIX systems this requires SSH login as root. Previously SSH port forwarding was combined with firewall rules or other port redirection methods, with some platforms being unsupported.
- ansible-test - Sanity tests always run in isolated Python virtual environments specific to the requirements of each test. The environments are cached.
- ansible-test - Sanity tests are now separated into two categories, controller and target. All tests except ``import`` and ``compile`` are controller tests. The controller tests always run using the same Python version used to run ``ansible-test``. The target tests use the Python version(s) specified by the user, or all available Python versions.
- ansible-test - Sanity tests now use fully pinned requirements that are independent of each other and other test types.
- ansible-test - Tests run with the ``centos6`` and ``default`` test containers now use a PyPI proxy container to access PyPI when Python 2.6 is used. This allows tests running under Python 2.6 to continue functioning even though PyPI is discontinuing support for non-SNI capable clients.
- ansible-test - The ``future-import-boilerplate`` and ``metaclass-boilerplate`` sanity tests are limited to remote-only code. Additionally, they are skipped for collections which declare no support for Python 2.x.
- ansible-test - The ``import`` and ``compile`` sanity tests limit remote-only Python version checks to remote-only code.
- ansible-test - Unit tests for controller-only code now require Python 3.8 or later.
- ansible-test - Version neutral sanity tests now require Python 3.8 or later.
- junit callback - The ``junit_xml`` and ``ordereddict`` Python modules are no longer required to use the ``junit`` callback plugin.

Minor Changes
-------------

- Add ``end_batch`` meta task.
- Allow connection and become passwords to be set by file/executable script. Also document this was already the case for vault.
- CLI - Remove ``__requires__`` attribute for ``pkg_resources``
- Collections can define action_groups in ``meta/runtime.yml``.
- Introduce a config option to enable/disable emitting warning about Jinja2 version being old for ``jinja2_native``. The option is on by default, only in CI it is off.
- Make the code structure of ansible-doc's generic snippet feature more maintainable.
- On RHEL 9, CentOS Stream 9 etc., use /usr/bin/python3 as the default interpreter; /usr/libexec/platform-python is just a backwards-compatibility symbolic link there.
- PowerShell - Added support for optional module_util imports by scanning for ``-Optional`` at the end of the import declaration
- Python 2.6 Target Support - Deprecate Python 2.6 for targets, requiring Python 2.7 or newer. ``ansible-core==2.13`` will drop support for Python 2.6. (https://github.com/ansible/ansible/pull/74165)
- Task - Add a resolved_action attribute for Task objects to get the final resolved plugin.
- Templar - remove ``_fail_on_lookup_errors`` and ``_fail_on_filter_errors`` instance variables that were never used. (https://github.com/ansible/ansible/pull/73785)
- The AnsiballZ Python wrapper now changes the working directory to ``~`` or ``/`` if the current one is not accessible. This allows become to drop privileges on macOS when using pipelining.
- Update test container ansible-core-test-container to version 3.6.0
- Update test container ansible-core-test-container to version 3.7.0
- Update test container default-test-container to version 3.6.0
- Update test container default-test-container to version 3.7.0
- Update vendored copy of ``six`` to 1.16.0 to eliminate warnings for deprecated python loader methods in Python 3.10+ (https://github.com/ansible/ansible/issues/74659)
- Update vendored copy of distro to 1.6.0
- Vendor ``distutils.version`` due to it's deprecation in Python 3.10 and impending removal in Python 3.12 (https://github.com/ansible/ansible/issues/74599)
- YAML parsing - Create common utils for loading and dumping YAML that prefer the C extensions if available
- ``include_role`` - Allow use of ``omit`` in the ``from_*`` arguments (https://github.com/ansible/ansible/issues/66349)
- ``uri``/``get_url`` - Expose ``unredirected_headers`` to modules to allow user control
- `ansible.plugins.callback.CallbackBase.host_label()` has been factored out as a static method (https://github.com/ansible/ansible/pull/73814).
- action_groups can include actions from other groups by using the special ``metadata`` dictionary field.
- add a quick short circuit when checking if a string is a template to improve performance on large strings (https://github.com/ansible/ansible/issues/74336)
- add host label to retry print statements
- added new function to module utils to choose best possible locale.
- adds the ``undef`` keyword to the templating environment. This allows for directly creating Undefined values in templates. It is most useful for providing a hint for variables which must be overridden.
- ansbile-doc now also shows snippets for inventory and lookup, adding to existing modules.
- ansible adhoc, clarified the help to some options, also added some comments to code.
- ansible-cli - remove unnecessary trailing space in ``ansible --version`` (https://github.com/ansible/ansible/issues/74875).
- ansible-config can now list and dump for specific documentable plugins by specifying them in the command line
- ansible-config has new 'init' option to create, highly commented, example configurations as ini (ansible.cfg), environment variables (shell) or Ansible variable files (YAML)
- ansible-config now supports displaying plugin configuration info.
- ansible-doc - ``version_added`` in ``attributes`` now comes with ``version_added_collection`` (https://github.com/ansible/ansible/pull/74602).
- ansible-doc - show ``version_added`` for the plugin/module itself in text output, and improve ``version_added`` formatting (https://github.com/ansible/ansible/pull/73602).
- ansible-doc now supports 'attributes' for plugins as per proposal.
- ansible-doc pretty cli options output.
- ansible-doc, improve handling of rstisms, try to make the display more meaningfull for the terminal users.
- ansible-galaxy - Allow specification of client_id override value for Keycloak Token (https://github.com/ansible/ansible/issues/75593).
- ansible-galaxy - Allow validate_certs to be configured for individual Galaxy servers (https://github.com/ansible/ansible/issues/75677).
- ansible-galaxy - Installing a collection from a git repository without specifying a version (or using the version ``HEAD``) will clone the repository using --depth=1.
- ansible-galaxy - Non-HTTP exceptions from Galaxy servers are now a warning and only fatal if the collection to download|install|verify is not available from any of the servers (https://github.com/ansible/ansible/issues/75443).
- ansible-test - A new ``base`` test container is available. It is similar to the ``default`` test container, but contains no pre-installed Python packages other than ``pip`` and its dependencies.
- ansible-test - Add RHEL 8.4 as a remote.
- ansible-test - Add ``--prime-venvs`` option to create virtual environments without running tests.
- ansible-test - Add constraint for ``decorator`` for Python versions prior to 3.5.
- ansible-test - Add support for Windows Server 2022.
- ansible-test - Add support for an ansible-test configuration file in collections under ``tests/config.yml``.
- ansible-test - Add support for testing with Python 3.10.
- ansible-test - Added a ``--prime-containers`` option to support downloading containers without running tests.
- ansible-test - Adding DigitalOcean cloud support to ansible-test (https://github.com/ansible/ansible/pull/74222).
- ansible-test - All "cloud" plugins have been refactored for more consistency. For those that use docker containers, management of the containers has been standardized.
- ansible-test - All "cloud" plugins now use fixed hostnames and ports in tests. Previously some tests used IP addresses and/or randomly assigned ports.
- ansible-test - Changes made to the ``hosts`` file on test systems are now done using an Ansible playbook for both POSIX and Windows systems. Changes are applied before a test target runs and are reverted after the test target finishes.
- ansible-test - Clean up code in the cloud plugins.
- ansible-test - Collections can declare their remote-only code (modules/module_utils and related tests) as controller-only.
- ansible-test - Collections can limit the Python versions used for testing their remote-only code (modules/module_utils and related tests).
- ansible-test - Command line help has been updated to hide the ``--remote`` option (and related options) when the user lacks an API key to use the feature.
- ansible-test - Constraints provided by ``ansible-test`` for Python package installs have been reduced.
- ansible-test - Default settings are now applied to unknown versions of known ``--remote`` platforms.
- ansible-test - Distribution specific test containers have been updated to version 3.0.0.
- ansible-test - Environment checking (``pip``, ``python``, ``~/.ssh/known_hosts``, etc.) is no longer performed when running integration tests.
- ansible-test - Environment variables exposed by "cloud" plugins are now available to the controller for role based tests. Previously only script based tests had access to the exposed environment variables.
- ansible-test - Fedora 32 and 33 (``fedora32`` and ``fedora33``) containers have been updated and now allow for ssh in more container environments.
- ansible-test - Fedora 34 (``fedora34``) container has been added.
- ansible-test - Installation of ``cryptography`` no longer occurs when it is already installed. This avoids downgrading existing OS packages.
- ansible-test - Minor code cleanup.
- ansible-test - More efficient string splitting.
- ansible-test - Most scripts used internally by ``ansible-test`` no longer have a shebang or the executable bit set.
- ansible-test - Move code from ``_data`` directory to ``_util`` directory.
- ansible-test - Relocate change classification code.
- ansible-test - Remove CI provider support for Shippable, now that the service has been discontinued.
- ansible-test - Remove check for legacy ``core`` and ``extras`` directories.
- ansible-test - Remove deprecated container ``fedora32``.
- ansible-test - Remove deprecated remote platforms ``freebsd/11.4`` and ``rhel/8.3```.
- ansible-test - Removed the warning filter for ``PyYAML`` in the ``import`` sanity test.
- ansible-test - Removed unused pip constraints. Collections may need to add their own constraints if they depended on any which were removed.
- ansible-test - Reorganize code for individual commands.
- ansible-test - Reorganize integration test implementation by command.
- ansible-test - Rewrite the ``compile`` sanity test to improve error handling and support Python 3.10.
- ansible-test - Sanity test warnings relating to Python version support have been improved.
- ansible-test - Set minimum version constraints for ``pytest``.
- ansible-test - Split out shell command implementation.
- ansible-test - The "injector" scripts are now generated at runtime to avoid issues with symlinks and shebangs.
- ansible-test - The HTTP Tester can now be used without the ``--docker`` or `--remote`` options. It still requires use of the ``docker`` command to run the container.
- ansible-test - The HTTP Tester has been converted to a "cloud" plugin and can now be requested using the ``cloud/httptester`` alias. The original ``needs/httptester`` alias is still supported for backwards compatibility.
- ansible-test - The ``--docker-keep-git`` option (used only for testing ansible-core) has been renamed to ``--keep-git``.
- ansible-test - The ``--python`` option can be used without another delegation option such as the ``--venv`` or ``--docker`` options.
- ansible-test - The ``ansible-test coverage`` commands ``combine``, ``report``, ``html`` and ``xml`` now support delegation.
- ansible-test - The ``default`` test container has been updated to version 3.4.0 and now uses Python 3.9 by default instead of Python 3.6.
- ansible-test - The ``docker run`` option ``--link`` is no longer used to connect test containers. As a result, changes are made to the ``/etc/hosts`` file as needed on all test containers. Previously containers which were used with the ``--link`` option did not require changes to the ``/etc/hosts`` file.
- ansible-test - The ``import`` sanity test now requires that Ansible modules guard instantiation of ``AnsibleModule`` with a ``if __name__ == '__main__'`` conditional, or equivalent logic.
- ansible-test - The ``import`` sanity test now requires that non-modules do not instantiate ``AnsibleModule`` on import.
- ansible-test - The ``validate-modules`` sanity test codes ``ansible-deprecated-module`` and ``collection-deprecated-module`` have been added.
- ansible-test - The ``validate-modules`` sanity test codes ``last-line-main-call``, ``missing-if-name-main`` and ``missing-main-call`` have been removed.
- ansible-test - The ``validate-modules`` sanity test no longer enforces the ``missing-if-name-main``, ``last-line-main-call`` or ``missing-main-call`` checks on non-deleted Ansible modules. Modules are still required to instantiate ``AnsibleModule`` when ``__name__ == '__main__'``.
- ansible-test - Unit tests are now run in separate contexts (``controller``, ``modules``, ``module_utils``), each using separate invocations of ``pytest``.
- ansible-test - Unit tests other than ``modules`` and ``module_utils`` are now run only on Python versions supported by the controller (Python 3.8+).
- ansible-test - Update ``typed-ast`` constraint to version 1.4.3 for compatibility with Python 3.10.
- ansible-test - Update distribution test containers from version 2.0.1 to 2.0.2.
- ansible-test - Update the Ansible Core and Ansible Collection default test containers to 3.2.0 and 3.2.2 respectively.
- ansible-test - Update the ``base`` and ``default`` containers from Python 3.10.0rc2 to 3.10.0.
- ansible-test - Update the ``import`` sanity test to avoid a new warning in Python 3.10.
- ansible-test - Update the ``runtime-metadata`` sanity test to handle a new warning on Python 3.10.
- ansible-test - Updated the ``default`` containers to version 4.0.1.
- ansible-test - Updated the help message for failed tests in the ``azure`` test plugin.
- ansible-test - Upgrade ``pylint`` to version 2.9.3 and update its dependencies to the latest versions as well.
- ansible-test - Using an unknown ``--docker`` or ``--remote`` environment now requires specifying a Python version.
- ansible-test - add freebsd/13.0 as a remote option.
- ansible-test - aws creates and exposes a new tiny_prefix variable to provide a shorter prefix for the AWS tests.
- ansible-test - display recent ``ssh`` debug logs after connection failures (https://github.com/ansible/ansible/pull/75374)
- ansible-test - validate-modules now properly checks ``attributes`` for plugins (https://github.com/ansible/ansible/pull/74602).
- ansible-test - virtualenv-isolated.sh is no longer provided. Prefer virtualenv.sh in its place.
- ansible-test validate-modules - enforce that ``_info`` and ``_facts`` modules set ``supports_check_mode=True`` (https://github.com/ansible/ansible/pull/75324).
- ansible-vault - remove support for ``PyCrypto`` (https://github.com/ansible/ansible/issues/72646)
- apt - added an ``allow_downgrade`` option to enable safe downgrade of packages without using ``force`` which doesn't verify signatures (https://github.com/ansible/ansible/issues/29451, https://github.com/ansible/ansible/pull/74852).
- apt, added a 'lock_timeout' to be more resilient when encountering the apt db already locked and handle it w/o haveing to rerun task.
- async tasks - the use of the task-level ``ANSIBLE_ASYNC_DIR`` variable within ``environment:`` is no longer valid. Use the shell configuration variable ``async_dir`` instead.
- async_wrapper, better reporting on timeout, slight refactor on reporting itself.
- basic module_util - Clean up ``selinux`` compat import.
- blockinfile - Remove unused code for Ansible 1.x.
- cache base - More efficient string splitting.
- callback API - implemented ``v2_runner_on_async_ok`` and ``v2_runner_on_async_failed`` callbacks (https://github.com/ansible/ansible/pull/74953).
- cli scripts - remove trailing blank space in help after newline when outputting.
- collection - match skip message as per role installation.
- command - update the user warning message to point out command name (https://github.com/ansible/ansible/pull/74475).
- config lookup now can handle plugin settings.
- config, default site for ansible-core is now under /ansbile-core/.
- connection base - Avoid using deprecated ``@abstractproperty`` decorator.
- constructed - a new options ``trailing_separator`` and ``default_value`` to deal with key's value empty on keyed group.
- cron - ``name`` is now a required parameter always
- cron - ``reboot`` parameter has been dropped in favor of ``special_time: reboot``
- cron, removed previously deprecated 'reboot' and now requires either 'name' as unique identifier.
- default callback plugin - displays output for ``v2_runner_on_async_ok`` and ``v2_runner_on_async_failed`` callbacks.
- deprecate ``_remote_checksum()`` and remove all internal uses (https://github.com/ansible/ansible/pull/74848)
- dnf - Add ``cacheonly`` option (https://github.com/ansible/ansible/issues/69397).
- dnf - allow for ``download_only`` to be run without root privileges (https://github.com/ansible/ansible/issues/75530)
- encrypt - add new parameter ``ident`` to specify version of BCrypt algorithm to be used (https://github.com/ansible/ansible/issues/74571).
- fact cache - Remove deprecated backwards compatibility shim for the FactCache `update` method to accept multiple arguments.
- fact cache - Remove the deprecated location for FactCache. Import FactCache from `ansible.vars.fact_cache` instead.
- facts - add fiber channel facts for HP-UX (https://github.com/ansible/ansible/pull/57406)
- galaxy - support role artifact download from API response ``download_url`` location (https://github.com/ansible/ansible/issues/73103).
- get_distribution - ``lib.ansible.module_utils.common.sys_info.get_distribution`` now returns distribution information for all platforms not just Linux (https://github.com/ansible/ansible/issues/17587)
- get_distribution_version - ``lib.ansible.module_utils.common.sys_info.get_distribution_version`` now returns the version for all platfroms not just Linux (https://github.com/ansible/ansible/issues/17587)
- git - Add ``accept_newhostkey`` option (https://github.com/ansible/ansible/issues/69846).
- hostname - add support RedOS (https://github.com/ansible/ansible/issues/74779).
- import_role - Template tasks_from, vars_from, defaults_from, and handlers_from with --extra-vars (https://github.com/ansible/ansible/issues/69097).
- include_vars - add ``hash_behaviour`` option (https://github.com/ansible/ansible/pull/72944).
- ini - added new parameter ``allow_no_value`` to ini lookup plugin (https://github.com/ansible/ansible/issues/50594).
- ini lookup - add case sensitive option (https://github.com/ansible/ansible/issues/74601)
- interpreter discovery - allow the default list of ``INTERPRETER_PYTHON_FALLBACK`` to be changed using a variable
- interpreter discovery - prefer Python 3 over Python 2
- inventory plugins - Remove the deprecated cache interface. Set top level keys in the inventory plugin's `_cache` attribute (a dictionary) instead.
- jinja2_native - short-circuit ``ast.literal_eval`` for non-string values
- module_utils distro - when a 'distro' package/module is in PYTHONPATH but isn't the real 'distro' package/module that we expect, gracefully fall back to our own bundled distro.
- modules - add Anolis distro in hostname.py. project website https://openanolis.org/
- move all builtin modules to use the best possible locale function instead of hardcoding 'C'.
- password - add new parameter ``ident`` to specify version of BCrypt algorithm to be used (https://github.com/ansible/ansible/issues/74571).
- password - add new parameter ``seed`` in lookup plugin (https://github.com/ansible/ansible/pull/69775).
- password_hash uses passlib default if option isn't set
- playbook - Error if a playbook is an empty list instead of just skipping
- playbook - Error if using ``include`` instead of ``import_playbook``
- replaced examples/ansible.cfg with instructions on how to generate an up to date copy.
- service - add description how service module works internally (https://github.com/ansible/ansible/issues/74507).
- service_facts now handles more states/statuses from systemd and in a more reliable way (failed, not-found, masked).
- setup - add ``epoch_int`` option to date_time facts (https://github.com/ansible/ansible/pull/73822).
- ssh - added pkcs11 support by adding the pkcs11_provider option in the ssh connection module. (https://www.github.com/ansible/ansible/pull/32829)
- ssh connection, can not configure ssh_transfer_method with a variable.
- ssh connection, ssh_transfer_method is now configurable via variable.
- subelements lookup - Use generator in instance type check.
- tempfile - Remove unnecessary conditional for creating a temporary directory.
- template - Add comment attributes (``comment_start_string`` and ``comment_end_string``)
- unicode utils - Fix ``__all__`` which was incorrectly declared as a string instead of a tuple.
- user - Add ``umask`` option (https://github.com/ansible/ansible/issues/40359).
- user module - Remove unused code.
- validation testcases for check_* APIs (https://github.com/ansible/ansible/issues/55994).
- winrm - Allow explicit environment variables to be passed through to the ``kinit`` call for Kerberos authentication
- yaml dumper - YAML representer for AnsibleUndefined (https://github.com/ansible/ansible/issues/75072).
- yum - Add ``cacheonly`` option (https://github.com/ansible/ansible/issues/69397).

Breaking Changes / Porting Guide
--------------------------------

- Action, module, and group names in module_defaults must be static values. Their values can still be templates.
- Fully qualified 'ansible.legacy' plugin names are not included implicitly in action_groups.
- Unresolvable groups, action plugins, and modules in module_defaults are an error.
- ansible-test - Automatic installation of requirements for "cloud" test plugins no longer occurs. The affected test plugins are ``aws``, ``azure``, ``cs``, ``hcloud``, ``nios``, ``opennebula``, ``openshift`` and ``vcenter``. Collections should instead use one of the supported integration test requirements files, such as the ``tests/integration/requirements.txt`` file.
- ansible-test - The HTTP Tester is no longer available with the ``ansible-test shell`` command. Only the ``integration`` and ``windows-integration`` commands provide HTTP Tester.
- ansible-test - The ``--disable-httptester`` option is no longer available. The HTTP Tester is no longer optional for tests that specify it.
- ansible-test - The ``--httptester`` option is no longer available. To override the container used for HTTP Tester tests, set the ``ANSIBLE_HTTP_TEST_CONTAINER`` environment variable instead.
- ansible-test - Unit tests for ``modules`` and ``module_utils`` are now limited to importing only ``ansible.module_utils`` from the ``ansible`` module.
- conditionals - ``when`` conditionals no longer automatically parse string booleans such as ``"true"`` and ``"false"`` into actual booleans. Any non-empty string is now considered true. The ``CONDITIONAL_BARE_VARS`` configuration variable no longer has any effect.
- hostname - Drops any remaining support for Python 2.4 by using ``with open()`` to simplify exception handling code which leaked file handles in several spots
- hostname - On FreeBSD, the string ``temporarystub`` no longer gets written to the hostname file in the get methods (and in check_mode). As a result, the default hostname will now appear as ``''`` (empty string) instead of ``temporarystub`` for consistency with other strategies. This means the ``before`` result will be different.
- hostname - On OpenRC systems and Solaris, the ``before`` value will now be ``''`` (empty string) if the permanent hostname file does not exist, for consistency with other strategies.
- intersect, difference, symmetric_difference, union filters - the default behavior is now to be case-sensitive (https://github.com/ansible/ansible/issues/74255)
- unique filter - the default behavior is now to fail if Jinja2's filter fails and explicit ``case_sensitive=False`` as the Ansible's fallback is case-sensitive (https://github.com/ansible/ansible/pull/74256)

Deprecated Features
-------------------

- ansible-test - The ``--docker-no-pull`` option is deprecated and has no effect.
- ansible-test - The ``--no-pip-check`` option is deprecated and has no effect.
- include action is deprecated in favor of include_tasks, import_tasks and import_playbook.
- module_utils' FileLock is scheduled to be removed, it is not used due to its unreliable nature.

Removed Features (previously deprecated)
----------------------------------------

- The built-in module_util ``ansible.module_utils.common.removed`` was previously deprecated and has been removed.
- connections, removed password check stubs that had been moved to become plugins.
- task, inline parameters being auto coerced into variables has been removed.

Security Fixes
--------------

- Do not include params in exception when a call to ``set_options`` fails. Additionally, block the exception that is returned from being displayed to stdout. (CVE-2021-3620)
- templating engine fix for not preserving usnafe status when trying to preserve newlines. CVE-2021-3583

Bugfixes
--------

- Add RockyLinux to fact gathering (https://github.com/ansible/ansible/pull/74530).
- Add unicode support to ``ansible-inventory`` CLI (https://github.com/ansible/ansible/issues/57378)
- Add yaml representer for VarsWithSources (https://github.com/ansible/ansible/pull/68525).
- Added page describing terminal plugins to docsite
- AnsibleModule.set_mode_if_different - don't check file existence when check_mode is activated (https://github.com/ansible/ansible/issues/61185).
- Apply ``display_failed_stderr`` callback option on loop item results. (https://github.com/ansible/ansible/issues/74864)
- Binary GnuPG keys downloaded via URLs by the 'ansible.builtin.apt_key' module were corrupted so 'gpg' could not import them (https://github.com/ansible/ansible/issues/74424).
- Ensure end_play ends play, not batch (https://github.com/ansible/ansible/issues/73971)
- Ensure we get full path for extra vars into cliargs to avoid realpath issues after initial load.
- Fix ``keys()`` implementation of ``BaseFileCacheModule`` to strip the prefix from the key and only return keys that share the same prefix as the cache.
- Fix ``when`` evaluation on Native Jinja and Python 3.10.
- Fix templating task action with host-specific vars (https://github.com/ansible/ansible/issues/75568)
- Fully qualified 'ansible.legacy' and 'ansible.builtin' plugin names work in conjunction with module_defaults.
- Give a warning instead of an error if a handler name contains undefined variables and has no listen topics (https://github.com/ansible/ansible/issues/58841).
- Improve resilience of ``ansible-galaxy collection`` by increasing the page size to make fewer requests overall and retrying queries with a jittered exponential backoff when rate limiting HTTP codes (520 and 429) occur. (https://github.com/ansible/ansible/issues/74191)
- Jinja2 globals should be accessible even when importing a template without the context (https://github.com/ansible/ansible/issues/75371)
- PlayContext - Remove deprecated ``make_become_cmd`` (https://github.com/ansible/ansible/issues/74136)
- PowerShell - Ignore the ``LIB`` environment variable when compiling C# Ansible code
- Prevent ``ansible_failed_task`` from further templating (https://github.com/ansible/ansible/issues/74036)
- Remove 'default' from ssh plugin as we want to rely on default from ssh itself or ssh/config.
- Replace usage of private dnf.Base() attribute by future dnf API
- Save unreachable hosts between plays by adding them to the PlayIterator's _play._removed_hosts (https://github.com/ansible/ansible/issues/66945).
- Solaris - correct version check in svcadm_supports_sync (https://github.com/ansible/ansible/pull/73860).
- Task depth - Prevent exception when the task depth exceeds Pythons recursion depth (https://github.com/ansible/ansible/issues/73996)
- Templating - Ensure we catch exceptions when calling ``.filters()`` or ``.tests()`` on their respective plugins and properly error, instead of aborting which results in no filters being added to the jinja2 environment (https://github.com/ansible/ansible/pull/74127)
- The ``apt_key`` module did not properly handle GnuPG errors (https://github.com/ansible/ansible/issues/74477)
- The error message about the failure to import a ```gpg`` key by the ``apt_key`` module was incorrect (https://github.com/ansible/ansible/issues/74423).
- Update network user guide to explain use of cli_parse and validate plugins.
- Variable Manager - Only check if ``play.hosts`` is a template when the play hasn't been finalized (https://github.com/ansible/ansible/issues/73926)
- WorkerProcess - Python 3.5 fix for workaround for stdout deadlock in multiprocessing shutdown to avoid process hangs. (https://github.com/ansible/ansible/issues/74149)
- ``AnsibleModule.run_command`` - Address thread safety issues, concerning mutating the environment, current working directory, and umask. (https://github.com/ansible/ansible/issues/74783)
- ``failed_when``/``changed_when`` - Catch templating errors to prevent masking of module output (https://github.com/ansible/ansible/issues/37187)
- ``heuristic_log_sanitize`` - Return the full string if there is no password (https://github.com/ansible/ansible/issues/75542)
- ``pip`` now uses the ``pip`` Python module installed for the Ansible module's Python interpreter, if available, unless ``executable`` or ``virtualenv`` were specified.
- advanced_host_list inventory plugin - Fixed variable referenced before assignment when hostname/range could not be parsed.
- ansiballz - avoid treating path to site_packages as regex; escape it. This prevents a crash when ansible is installed to, or running from, an oddly named directory like ``ansi[ble``
- ansible-doc - in text output, do not show empty ``version_added_collection`` values (https://github.com/ansible/ansible/pull/74999).
- ansible-doc can now dump kewyords with --metadata-dump (still just for internal use)
- ansible-doc, fix output for internal metadata dump option
- ansible-doc, make inventory plugin selection for snippets generic and not a hardcoded list
- ansible-galaxy - Fix a bug with build_ignore when installing collections from source (https://github.com/ansible/ansible/issues/75528).
- ansible-galaxy - Fix handling HTTP exceptions from Galaxy servers. Continue to the next server in the list until the collection is found.
- ansible-galaxy - Improve error message from dependency resolution when a candidate has inconsistent requirements (https://github.com/ansible/ansible/issues/75139).
- ansible-inventory - handle an exception while parsing inventory in toml format (https://github.com/ansible/ansible/issues/74404).
- ansible-playbook, more robust handling of --list-hosts and undefined vars in hosts keyword.
- ansible-pull - update documentation for ``--directory`` option to clarify path must be absolute.
- ansible-pull, restore other options to use as repo other than git.
- ansible-test - Add constraint for ``pyspnego>=0.1.6`` for Python 3.10 - https://github.com/ansible/ansible/pull/74612
- ansible-test - Avoid publishing the port used by the ``pypi-test-container`` since it is only accessed by other containers. This avoids issues when trying to run tests in parallel on a single host.
- ansible-test - Failure to download test results from a remote host no longer hide test failures. If a download failure occurs after tests fail, a warning will be issued instead.
- ansible-test - Fix docker container IP address detection. The ``bridge`` network is no longer assumed to be the default.
- ansible-test - Fix path to inventory file for ``windows-integration`` and ``network-integration`` commands for collections.
- ansible-test - Fix traceback when generating coverage reports and no coverage directory exists.
- ansible-test - Random port selection is no longer handled by ``ansible-test``, avoiding possible port conflicts. Previously ``ansible-test`` would, under some circumstances, use one host's available ports to determine those of another host.
- ansible-test - Running tests in a single test run with multiple "cloud" plugins no longer results in port conflicts. Previously two or more containers with overlapping ports could not be used in the same test run.
- ansible-test - Tab completion after options like ``--docker`` which accept an optional argument will no longer provide incorrect completions.
- ansible-test - The ``--python`` and ``--venv`` options are no longer ignored by some commands, such as ``coverage``.
- ansible-test - The ``docker inspect`` command is now used to check for existing images instead of the ``docker images`` command. This resolves an issue where a ``docker pull`` would be unnecessarily executed for an image referenced by checksum.
- ansible-test - Update distribution test containers to version 3.1.0.
- ansible-test - Use ``--strict`` for ``pytest`` on Python 2.6 since ``--strict-markers`` is not available.
- ansible-test - Use documented API to retrieve build information from Azure Pipelines.
- ansible-test - Use pwsh to generate correct coverage line counts for stub files to get a more accurate coverage result
- ansible-test - Use the correct variable to reference the client's SSH key when generating inventory.
- ansible-test - add packaging python module to ``ansible-doc`` sanity test requirements.
- ansible-test - allow the same listening port on all container interfaces
- ansible-test - ensure the correct unit test target is given when the ``__init__.py`` file is modified inside the connection plugins directory
- ansible-test - make the ``a/`` and ``b/`` prefixes an optional match since these can be turned off with the ``diff.noprefix`` setting in ``git``
- ansible-test - restrict ``packaging`` to ``< 21.0`` for Python ``< 3.6`` (https://github.com/ansible/ansible/pull/75186).
- ansible-test pslint - Fix error when encountering validation results that are highly nested - https://github.com/ansible/ansible/issues/74151
- ansible-test validate-modules - EXAMPLES will no longer be marked as invalid YAML when it uses Ansible-specific YAML tags (https://github.com/ansible/ansible/pull/74384).
- ansible-test validate-modules - correctly validate positional parameters to ``AnsibleModules`` (https://github.com/ansible/ansible/pull/75332).
- ansible.builtin.cron - Keep non-empty crontabs, when removing cron jobs (https://github.com/ansible/ansible/pull/74497).
- ansible.utils.encrypt now handles missing or unusable 'crypt' library.
- ansible_test - add constraint for ``MarkupSafe`` (https://github.com/ansible/ansible/pull/74666)
- apt_key - set --recv argument as last one in apt-key command when using env var HTTP_PROXY (https://github.com/ansible/ansible/issues/74946)
- arg_spec - remove unused imports
- async_status, ensure we always get documented returns
- async_status, resurrected module to deprecate for those that were invoking it directly.
- basic - skip over module parameters which are used in ``journal.send`` API call (https://github.com/ansible/ansible/issues/71343).
- become - fix a regression on Solaris where chmod can return 5 which we interpret as auth failure and stop trying become tmpdir permission fallbacks
- become - work around setfacl not existing on modern Solaris (and possibly failing on some filesystems even when it does exist)
- callbacks, restore displaying delegation to host as host label.
- cli defaults for ssh args set to None as '' was bypassing normal default.
- command - remove unreachable code path when trying to convert the value for ``chdir`` to bytes (https://github.com/ansible/ansible/pull/75036)
- command module, clarify order of remove/creates checks.
- command module, correctly handles chdir to symlinks.
- command module, move to standarized messages in 'msg' vs abusing 'stdout'.
- command module, now all options work in ad-hoc execution.
- command module, now always returns what we documented as 'returns always'.
- config - use ``callbacks_enabled`` instead ``callback_enabled`` in a deprecated message (https://github.com/ansible/ansible/issues/70028).
- config lookup, can also handle collection plugins now
- config, ensure 'quoted' lists from ini or env do not take the quotes literally as part of the list item.
- connection ssh, no ssh_args cli option, so removed doc entry.
- constants, internal _deprecated function always requires version.
- correct doc links for become on warnings over world readable settings.
- correctly use world readable setting since old constant is not 'settable' anymore.
- dnf - align the return value of the list argument with the ``yum`` module (https://github.com/ansible/ansible/issues/75483)
- dnf - properly capture transaction error (https://github.com/ansible/ansible/issues/72651)
- dnf - refactor code to use `dnf whatprovides` API (https://github.com/ansible/ansible/issues/73503).
- dnf - support non-english environments (https://github.com/ansible/ansible/issues/75021)
- dnf module - Use all components of a package name to determine if it's installed (https://github.com/ansible/ansible/issues/75311).
- do not trigger interpreter discovery in the forced_local module path as they should use the ansible playbook python unless otherwise configured.
- facts - detect homebrew installed at /opt/homebrew/bin/brew
- facts, service_mgr, handle issues if ps command fails or returns empty.
- filter plugins - patch new versions of Jinja2 to prevent warnings/errors on renamed filter decorators (https://github.com/ansible/ansible/issues/74667)
- find - fix a bug where ``size`` argument was ignored for regular files with ``file_type`` of ``any``.
- find action, correctly convert path to text when warning about skiping.
- find does not ignore errors from os.walk anymore and issues warnings as expected.
- gather_facts, improved message on timeout.
- gather_facts, package, service - fix using module_defaults for the modules in addition to the action plugins. (https://github.com/ansible/ansible/issues/72918)
- get_bin_path, clarify with quotes what the missing required executable is.
- get_url - Fixed checksum validation for binary files (leading asterisk) in checksum files (https://github.com/ansible/ansible/pull/74502).
- getent, fix return data for when there are multiple results for the same key
- git - Fix git path used when .git file is present (https://github.com/ansible/ansible/issues/75608).
- host_group_vars vars plugin fixed ini entry, section and key were reversed.
- hostname - Add Rocky Linux support
- hostname - No longer modifies system files in get_* methods and therefore when consulted in check_mode (https://github.com/ansible/ansible/issues/66432)
- include - Remove deprecated ``static`` argument for ``include`` (https://github.com/ansible/ansible/issues/74135)
- includes - Remove the deprecated ability to specify ``tags`` as ``vars`` on includes (https://github.com/ansible/ansible/issues/74144)
- ini lookup - better error on mixed/bad parameters
- ini lookup - handle errors for duplicate keys and missing sections (https://github.com/ansible/ansible/issues/74601)
- interpreter discovery - Debian 8 and lower will avoid unsupported Python3 version in interpreter discovery
- interpreter discovery is now handling special (ansible_network_os) cases in less noisy ways.
- interpreter_discovery - hide warning 'No python interpreters...' when ANSIBLE_PYTHON_INTERPRETER=auto_silent (https://github.com/ansible/ansible/issues/74274).
- module_common - handle exception when multiple workers try to create the cache directory
- module_defaults - Fix action defaults for legacy actions/modules (https://github.com/ansible/ansible/issues/75279).
- module_utils - detect symlinked init systems, even if unable to read /proc/1/comm (https://github.com/ansible/ansible/issues/74866).
- netconf - catch and handle exception to prevent stack trace when running in FIPS mode
- network module_utils - fix bug where ``to_bits()`` returned the ``str`` type instead of a useful value.
- paramiko_ssh - mark connection as connected when ``_connect()`` is called (https://github.com/ansible/ansible/issues/74081)
- password - Handle passlib wrapped algos bsd_nthash, django_argon2, django_bcrypt, ldap_bcrypt, ldap_bsdi_crypt, ldap_des_crypt, ldap_hex_md5, ldap_hex_sha1, ldap_md5_crypt, ldap_pbkdf2_sha1, ldap_pbkdf2_sha256, ldap_pbkdf2_sha512, ldap_sha1_crypt, ldap_sha256_crypt, ldap_sha512_crypt, roundup_plaintext (https://github.com/ansible/ansible/pull/75527).
- pause - ensure control characters are always set to an appropriate value (https://github.com/ansible/ansible/issues/73264)
- pkg_mgr.py - Lower the priority of rpm-ostree detection to avoid false positives on systems not using it as the main package manager (https://github.com/ansible/ansible/issues/74578)
- play - validate the ``hosts`` entry in a play (https://github.com/ansible/ansible/issues/65386)
- playbook loaded from collection subdir now does not ignore subdirs.
- plugin config now allows list type options to have multiple valid choices (#74225).
- psrp - Always cleanup the last run pipeline if a second pipeline is invoked to avoid violating any resource limits.
- psrp - Fix error when resetting a connection that was initialised but not connected - (https://github.com/ansible/ansible/issues/74092).
- psrp - Try to clean up any server-side resources when resetting a connection.
- recursive_diff - handle condition when parameters are not dict (https://github.com/ansible/ansible/issues/56249).
- register - Ensure that ``register`` used on ``set_fact`` or ``include_vars`` does not automatically wrap the facts as unsafe. (https://github.com/ansible/ansible/issues/21088)
- rekey_on_member - handle undefined positional arguments better.
- remote tmpdir permissions - fix type error in macOS chmod ACL fallback (https://github.com/ansible/ansible/pull/74613).
- replace - better handling of file operation exceptions (https://github.com/ansible/ansible/pull/74686).
- roles - allow for role arg specs in new meta file (https://github.com/ansible/ansible/issues/74525).
- roles - fix unexpected ``AttributeError`` when an empty ``argument_specs.yml`` is present (https://github.com/ansible/ansible/pull/75604).
- roles - make sure argspec validation task is tagged with ``always`` (https://github.com/ansible/ansible/pull/74994).
- roles - make sure argspec validation task templates suboptions (https://github.com/ansible/ansible/issues/75070).
- schema validation now uses dynamic range of versions for valid deprecation entries vs hardcoded out of date list.
- script inventory plugin - Remove deprecated caching support (https://github.com/ansible/ansible/issues/74143)
- sequence - fix error message so that unrecognized options to the plugin display correctly as a list and normalize error messages.
- service - compare version without LooseVersion API (https://github.com/ansible/ansible/issues/74488).
- set ssh host_key_checking defaults to True, restoring original behaviour (https://github.com/ansible/ansible/issues/75168)
- setup module should now not truncate hpux interface names.
- setup module, fix filter to adjust for missing ``ansible_`` prefix on query.
- setup, while gathering linux hardware facts be more resilient to errors and try to return more info.
- slurp - Fix error messages for unreadable files and directories(https://github.com/ansible/ansible/issues/67340).
- slurp - handle error when ``path`` is a directory and not a file (https://github.com/ansible/ansible/pull/74930).
- slurp - improve the logic in the error handling and remove ``os.stat()`` call (https://github.com/ansible/ansible/pull/75038)
- ssh connection now correctly handle ssh_transfer_method and scp_if_ssh interactions.
- ssh connection, fix interaction between trasnfer settings options.
- ssh connection, use self.host which has the most up2date info instead of pc.remote_addr
- ssh_connection - rename ``retries`` to ``reconnection_retries`` to avoid conflicts with task vars (https://github.com/ansible/ansible/issues/75142).
- ssh_connection - set the default for ``reconnection_retries`` back to ``0`` (https://github.com/ansible/ansible/issues/75142).
- subversion - fix stack trace when getting information about the repository (https://github.com/ansible/ansible/issues/36498)
- system_service - use a context manager for file handling.
- task_executor, Actions using AnsibleActionFail/Skip will now propagate 'results' if given
- task_executor/ssh_connection - use the ``retries`` value from ``ssh_connection`` settings, not the default from the ``Task`` field attributes (https://github.com/ansible/ansible/issues/75142).
- template - ensure Jinja2 overrides from template header are used (https://github.com/ansible/ansible/issues/75275)
- unarchive - allow extracting archives that contain files which size exceeds free system memory (https://github.com/ansible/ansible/issues/73985).
- unarchive - fail when zipinfo binary is not found in executable paths (https://github.com/ansible/ansible/issues/39029).
- unarchive - move failure for missing binary to ``can_handle_archive()`` rather than ``__init__()``
- uri - Fix traceback and provide error message when trying to use non-string or mapping for ``form-multipart`` body - https://github.com/ansible/ansible/issues/74276
- urls - Fix logic in matching ``unredirected_headers`` to perform case insensitive matching
- validate_argument_spec, correct variable precedence and merge method and add missing examples
- variable manager, avoid sourcing delegated variables when no inventory hostname is present. This affects scenarios like syntax check and imports.
- version test - improve error message when an empty version is provided
- yum - Fixed typo in failure message (https://github.com/ansible/ansible/pull/72964).
- yum - When upgrading, every architecture of a package is now included in the module results, instead of just one (https://github.com/ansible/ansible/issues/73284).
- yum - fix ``yumstate`` return value when wildcards are used in the ``list`` argument (https://github.com/ansible/ansible/issues/74557)
- yum - fix parsing of multiple subsequent empty lines from ``yum check-update`` output (https://github.com/ansible/ansible/issues/70949)
- yum - yum action plugin changes to support 'use' as an alias of 'use_backend' (https://github.com/ansible/ansible/issues/70774).

Known Issues
------------

- ansible-test - Tab completion anywhere other than the end of the command with the new composite options will provide incorrect results. See https://github.com/kislyuk/argcomplete/issues/351 for additional details.
