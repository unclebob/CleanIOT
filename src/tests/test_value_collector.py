import unittest


class ValueCollectorTest(unittest.TestCase):
    def setUp(self):
        self.addCleanup(self.unpatch)
        init_batch()

    def unpatch(self):
        pass

    def test_batch_before_any_reads(self):
        self.assertEqual("[]", get_batch_values())

    def test_batch_after_one_read(self):
        put_value_in_batch('11AAFF')
        self.assertEqual('[11AAFF]', get_batch_values())

    def test_batch_after_two_reads(self):
        put_value_in_batch('11AAFF')
        put_value_in_batch('22BBEE')
        self.assertEqual('[11AAFF 22BBEE]', get_batch_values())

    def test_batch_after_five_reads(self):
        put_value_in_batch('11AAFF')
        put_value_in_batch('22BBEE')
        self.assertEqual('[11AAFF 22BBEE]', get_batch_values())

values = ''

def init_batch():
    global values
    values = ''


def put_value_in_batch(value):
    global values
    if values == '':
        values = value
    else:
        values = values + " " + value

def get_batch_values():
    return '[' + values + ']'
