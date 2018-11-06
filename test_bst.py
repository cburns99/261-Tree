
import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

	def test_instantiation(self):
		try:
			BinarySearchTree()
		except NameError:
			self.fail("could not instantiate")
			
	def test_instantiation_with_value(self):
		fake_vlue = "fake"
		bst = BinarySearchTree(fake_vlue)
		self.assertEqual(fake_vlue, bst.value)

	def test_insert_smaller(self):
		bst = BinarySearchTree(10)
		insertee = BinarySearchTree(1)
		bst.insert(insertee)
		self.assertEqual(insertee, bst.left)

	def test_insert_larger(self):
		bst = BinarySearchTree(10)
		insertee = BinarySearchTree(20)
		bst.insert(insertee)
		self.assertEqual(insertee,bst.right)
   
	def test_find(self):
		item = 5
		bst = BinarySearchTree(item)
		return_item = bst.find(item)
		self.assertEqual(item, return_item)

	def test_preorder(self):
		bst = BinarySearchTree()
		bst.insert(1)
		test_list = [1]
		test = bst.pre_order()
		self.assertEqual(test, test_list)

if __name__=='__main__':
	unittest.main()