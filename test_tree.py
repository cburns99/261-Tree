
import unittest

class TestTree(unittest.TestCase):
	def test_faliure(self):
		self.fail("intentional failure.")

if __name__=='__main__':
	unittest.main()