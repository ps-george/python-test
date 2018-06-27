import unittest
from myproject.hello import Hello

class ExampleTestCase(unittest.TestCase):
    greeter = Hello()

    def test_pass(self):
        self.assertEqual('hi', self.greeter.say_hi())
        self.assertEqual('hello', self.greeter.say_hello())
        self.assertNotEqual('hi', self.greeter.say_hello())


    def test_raise(self):
        self.assertRaises(Exception, lambda: self.greeter.oh_dear())

    def test_fail(self):
        # Uncomment this line to see what happens when a test fails.
        # self.assertEqual('hi', self.greeter.say_hello())
        pass

if __name__=="__main__":
    unittest.main()
