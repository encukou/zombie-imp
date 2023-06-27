import unittest
import warnings
from pathlib import Path
try:
    from test.support.import_helper import CleanImport
except ImportError:
    from test.support import CleanImport
import sys
try:
    from test.support.warnings_helper import check_warnings
except ImportError:
    from test.support import check_warnings

from  zombie_imp import pkgutil


class ImportlibMigrationTests(unittest.TestCase):
    # With full PEP 302 support in the standard import machinery, the
    # PEP 302 emulation in this module is in the process of being
    # deprecated in favour of importlib proper

    def check_deprecated(self):
        return check_warnings(
            ("This emulation is deprecated and slated for removal in "
             "Python 3.12; use 'importlib' instead",
             DeprecationWarning))

    def test_importer_deprecated(self):
        with self.check_deprecated():
            pkgutil.ImpImporter("")

    def test_loader_deprecated(self):
        with self.check_deprecated():
            pkgutil.ImpLoader("", "", "", "")
