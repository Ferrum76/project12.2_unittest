import unittest
from utils import dicts

class TestCollections(unittest.TestCase):

    def test_get(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(dicts.get_val(data, "vcs"), "mercurial")
        self.assertEqual(dicts.get_val(data, "vcs", "git"), "mercurial")
        self.assertEqual(dicts.get_val({}, "vcs"), "git")
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), "bazaar")

        