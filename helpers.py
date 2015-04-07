# One way testing is unittest:
from unittest import TestCase

# But I prefer to use expect insted of assert:
from expects import *

# For mocking I use mock:
try:
    from mock import patch, Mock
except ImportError:
    from unittest.mock import patch, Mock

# Mocking opening a file
try:
    import __builtin__
    OPEN_NAME = '__builtin__.open'
except ImportError:
    OPEN_NAME = 'builtins.open'

def create_open_mock(testcase, content):
    open_patcher = patch(OPEN_NAME)
    testcase.addCleanup(open_patcher.stop)
    testcase.open_mock = open_patcher.start()
    testcase.open_mock.return_value.__enter__ = lambda s: s
    testcase.open_mock.return_value.__exit__ = Mock()
    testcase.open_mock.return_value.read.return_value = content
