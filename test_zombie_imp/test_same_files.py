"""`test_imp.py` and `test_zombie_imp.py` should match"""


import unittest
from pathlib import Path
import difflib
import collections


class FilesMatchTests(unittest.TestCase):
    def test_tests_same(self):
        with (Path(__file__).parent.joinpath('test_imp.py').open() as t_imp,
            Path(__file__).parent.joinpath('test_zombie_imp.py').open() as t_z_imp,
        ):
            diff_lines = list(difflib.unified_diff(list(t_imp), list(t_z_imp)))
            prefix_counts = collections.Counter(line[:1] for line in diff_lines)
            try:
                self.assertEqual(prefix_counts['+'], 2)
                self.assertEqual(prefix_counts['-'], 2)
            except:
                print(''.join(diff_lines))
                print(prefix_counts)
                raise
