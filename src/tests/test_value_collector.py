import unittest
from src.snappyImages.value_collector import *

class ValueCollectorTest(unittest.TestCase):
    def setUp(self):
        self.addCleanup(self.unpatch)
        value_collector_init()

    def unpatch(self):
        pass

    def test_batch_before_any_reads(self):
        self.assertEqual("[]", value_collector_get_batch())

    def test_batch_after_one_read(self):
        value_collector_put_value('11AAFF')
        self.assertEqual('[11AAFF]', value_collector_get_batch())

    def test_batch_after_two_reads(self):
        value_collector_put_value('11AAFF')
        value_collector_put_value('22BBEE')
        self.assertEqual('[11AAFF 22BBEE]', value_collector_get_batch())

    def test_batch_after_batch_size_exceeded(self):
        value_collector_put_value('11AAFF')
        value_collector_put_value('22BBEE')
        value_collector_put_value('33BBEE')
        value_collector_put_value('44BBEE')
        value_collector_put_value('55BBEE')
        value_collector_put_value('66BBEE')
        self.assertEqual('[22BBEE 33BBEE 44BBEE 55BBEE 66BBEE]', value_collector_get_batch())

