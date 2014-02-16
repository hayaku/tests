# -*- coding: utf-8 -*-
import unittest

from hayaku_probe import get_all_properties
from hayaku_dict_driver import merge_dict

class GetAllProperties(unittest.TestCase):
    def test_not_empty(self):
        self.assertTrue(get_all_properties())

class MergeDict(unittest.TestCase):
    """ https://github.com/hayaku/hayaku/issues/139 """
    def test_simple_merge1(self):
        l = {'abc':123}
        r = {}
        self.assertTrue(merge_dict(l, r), {'abc':123})

    def test_simple_merge2(self):
        l = {}
        r = {'abc':123}
        self.assertEqual(merge_dict(l, r), {'abc':123})

    def test_nomerge(self):
        l = {}
        r = {}
        self.assertEqual(merge_dict(l, r), {})

    def test_replace_default0(self):
        l = {'width':{'default':123}}
        r = {'width':{'default':321}}
        self.assertEqual(merge_dict(l, r), {'width':{'default':321}})

    def test_replace_default1(self):
        l = {'width':{}}
        r = {'width':{'default':321}}
        self.assertEqual(merge_dict(l, r), {'width':{'default':321}})

    def test_replace_prefixes0(self):
        l = {'width':{'prefixes':[1,2,3]}}
        r = {'width':{'prefixes':[3,2,1]}}
        self.assertEqual(merge_dict(l, r), {'width':{'prefixes':[3,2,1]}})

    def test_replace_prefixes1(self):
        l = {'width':{}}
        r = {'width':{'prefixes':[3,2,1]}}
        self.assertEqual(merge_dict(l, r), {'width':{'prefixes':[3,2,1]}})

    def test_remove_value0(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'remove-values':[3]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[1,2]}})

    def test_remove_value1(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'remove-values':[5]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[1,2,3]}})

    def test_remove_value1(self):
        l = {'width':{'values':[1,2,3,1]}}
        r = {'width':{'remove-values':[1]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[2,3]}})

    def test_add_values0(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':[1]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[1,2,3]}})

    def test_add_values0_0(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':[0]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[0,1,2,3]}})

    def test_add_values1(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':['...',1]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[2,3,1]}})

    def test_add_values1_0(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':['...',4]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[1,2,3,4]}})

    def test_add_values2(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':[1,'...',1]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[1,2,3]}})

    def test_add_values2_0(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':[0,'...',4]}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[0,1,2,3,4]}})

    def test_add_values3(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':[1,'...']}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[1,2,3]}})

    def test_add_values3_0(self):
        l = {'width':{'values':[1,2,3]}}
        r = {'width':{'values':[0,'...']}}
        self.assertEqual(merge_dict(l, r), {'width':{'values':[0,1,2,3]}})

class CssDictTests(unittest.TestCase):

    @unittest.skip('broken')
    def test_0(self):
        pd = parse_dict(FILE_DATA)
        self.assertEqual(expand_values(pd, pd.keys())['caption-side'], set(['top', 'bottom']))

    @unittest.skip('broken')
    def test_1(self):
        pd = parse_dict(FILE_DATA)
        self.assertEqual(expand_values(pd, pd.keys())['width'], set([
            'auto', '<dimension>', "['100%']",
            '<number>', '<length>', '<percentage>',
            '.em', '.ex', '.vw', '.vh', '.vm', '.ch', '.rem',
            '.px', '.cm', '.mm', '.in', '.pt', '.pc', '.%',
            ]))


if __name__ == '__main__':
    unittest.main()
