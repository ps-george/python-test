import unittest
from myproject import Hello

class ExampleTestCase(unittest.TestCase):
    greeter = Hello()

    def test_pass(self):
        self.assertEqual('hi', self.greeter.say_hi())
        self.assertEqual('hello', self.greeter.say_hello())
        self.assertNotEqual('hi', self.greeter.say_hello())


    def test_raise(self):
        self.assertRaises(Exception, lambda: self.greeter.oh_dear())

    def test_fail(self):
        self.assertEqual('hi', self.greeter.say_hello())

if __name__=="__main__.py":
    unittest.main()
