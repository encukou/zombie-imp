"""`test_imp.py` and `test_zombie_imp.py` should match"""


import unittest
from pathlib import Path
import difflib
import collections
from contextlib import ExitStack


class FilesMatchTests(unittest.TestCase):
    def test_tests_same(self):
        with ExitStack() as cm:
            t_imp = cm.enter_context(Path(__file__).parent.joinpath('test_imp.py').open())
            t_z_imp = cm.enter_context(Path(__file__).parent.joinpath('test_zombie_imp.py').open())

            diff_lines = list(difflib.unified_diff(list(t_imp), list(t_z_imp)))
            prefix_counts = collections.Counter(line[:1] for line in diff_lines)
            try:
                self.assertEqual(prefix_counts['+'], 2)
                self.assertEqual(prefix_counts['-'], 2)
            except:
                print(''.join(diff_lines))
                print(prefix_counts)
                raise
