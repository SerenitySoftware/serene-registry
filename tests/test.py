#!/usr/bin/python

import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-6]) # -6 gets rid of "/tests"
from SereneRegistry import registry
import unittest

class SereneRegistryTests(unittest.TestCase):
    """Unit testing of the SereneRegistry.registry class"""

    def setUp(self):
        registry.storage = {}

    def tearDown(self):
        registry.storage = {}

    def test_set(self):

        registry.set('test', 'foo')

        self.assertEqual('foo', registry.storage['test'])

    def test_test(self):

        registry.set('test', 'foo')

        self.assertTrue(registry.test('test'))
        self.assertFalse(registry.test('bar'))

    def test_get(self):

        registry.set('test', 'foo')

        self.assertEqual('foo', registry.get('test'))
        self.assertIsNone(registry.get('bar'))

    def test_flush(self):

        registry.set('test', 'foo')

        self.assertEqual('foo', registry.get('test'))
        self.assertNotEqual(0, len(registry.storage))

        registry.flush()

        self.assertEqual(0, len(registry.storage))


if __name__ == '__main__':
    unittest.main()