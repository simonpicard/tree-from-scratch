import unittest

from BinaryTree import BinaryTree

# How to use unittest: http://docs.python.org/py3k/library/unittest.html?highlight=unittest#unittest
# setUp, tearDown
# When a setUp() method is defined, the test runner will run that method prior to each test. Likewise, if a tearDown() method is defined, the test runner will invoke that method after each test. In the example, setUp() was used to create a fresh sequence for each test.

# assertEqual(), assertTrue(), assertRaises()
# The crux of each test is a call to assertEqual() to check for an expected result; assertTrue() to verify a condition; or assertRaises() to verify that an expected exception gets raised. These methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt1 = BinaryTree("+", BinaryTree("2"), BinaryTree("5"))
        self.bt2 = BinaryTree("*", self.bt1, self.bt1)
        self.bt3 = BinaryTree("/", self.bt2, self.bt2)

    # def tearDown(self):

    def test__initAndRepr__(self):
        self.assertEqual(self.bt1.getRootVal(), "+")
        self.assertEqual(self.bt1.getLeftChild().getRootVal(), "2")
        self.assertEqual(self.bt1.getRightChild().getRootVal(), "5")

        self.assertEqual(self.bt2.getRootVal(), "*")
        self.assertEqual(self.bt2.getLeftChild().getRootVal(), "+")
        self.assertEqual(self.bt2.getRightChild().getRootVal(), "+")

    def test__repr__(self):
        self.assertEqual(self.bt1.__repr__(), "2+5")
        self.assertEqual(self.bt2.__repr__(), "2+5*2+5")

    def test__inorderToString__(self):
        self.assertEqual(self.bt1.inorderToString("(", ")"), "(2+5)")
        self.assertEqual(self.bt2.inorderToString("(", ")"), "((2+5)*(2+5))")
        self.assertEqual(
            self.bt3.inorderToString("(", ")"), "(((2+5)*(2+5))/((2+5)*(2+5)))"
        )


if __name__ == "__main__":
    unittest.main()
