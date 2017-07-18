import unittest

class ExampleTest(unittest.TestCase):

  def setUp(self):
    self.addCleanup(self.unpatch)

  def unpatch(self):
    pass

  def test_init(self):
    self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()