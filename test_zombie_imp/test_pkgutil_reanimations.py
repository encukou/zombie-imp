import unittest
import warnings
from pathlib import Path
from test.support.import_helper import CleanImport
import sys

from test.support.warnings_helper import check_warnings

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

    def test_get_loader_avoids_emulation(self):
        with check_warnings() as w:
            self.assertIsNotNone(pkgutil.get_loader("sys"))
            self.assertIsNotNone(pkgutil.get_loader("os"))
            self.assertIsNotNone(pkgutil.get_loader("test.support"))
            self.assertEqual(len(w.warnings), 0)

    @unittest.skipIf(__name__ == '__main__', 'not compatible with __main__')
    def test_get_loader_handles_missing_loader_attribute(self):
        global __loader__
        this_loader = __loader__
        del __loader__
        try:
            with check_warnings() as w:
                self.assertIsNotNone(pkgutil.get_loader(__name__))
                self.assertEqual(len(w.warnings), 0)
        finally:
            __loader__ = this_loader

    def test_get_loader_handles_missing_spec_attribute(self):
        name = 'spam'
        mod = type(sys)(name)
        del mod.__spec__
        with CleanImport(name):
            sys.modules[name] = mod
            loader = pkgutil.get_loader(name)
        self.assertIsNone(loader)

    def test_get_loader_handles_spec_attribute_none(self):
        name = 'spam'
        mod = type(sys)(name)
        mod.__spec__ = None
        with CleanImport(name):
            sys.modules[name] = mod
            loader = pkgutil.get_loader(name)
        self.assertIsNone(loader)

    def test_get_loader_None_in_sys_modules(self):
        name = 'totally bogus'
        sys.modules[name] = None
        try:
            loader = pkgutil.get_loader(name)
        finally:
            del sys.modules[name]
        self.assertIsNone(loader)

    def test_find_loader_missing_module(self):
        name = 'totally bogus'
        loader = pkgutil.find_loader(name)
        self.assertIsNone(loader)

    def test_find_loader_avoids_emulation(self):
        with check_warnings() as w:
            self.assertIsNotNone(pkgutil.find_loader("sys"))
            self.assertIsNotNone(pkgutil.find_loader("os"))
            self.assertIsNotNone(pkgutil.find_loader("test.support"))
            self.assertEqual(len(w.warnings), 0)

    def test_get_importer_avoids_emulation(self):
        # We use an illegal path so *none* of the path hooks should fire
        with check_warnings() as w:
            self.assertIsNone(pkgutil.get_importer("*??"))
            self.assertEqual(len(w.warnings), 0)

    def test_issue44061(self):
        try:
            pkgutil.get_importer(Path("/home"))
        except AttributeError:
            self.fail("Unexpected AttributeError when calling get_importer")

    def test_iter_importers_avoids_emulation(self):
        with check_warnings() as w:
            for importer in pkgutil.iter_importers(): pass
            self.assertEqual(len(w.warnings), 0)

