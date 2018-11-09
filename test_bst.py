
import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

	def test_instantiation(self):
		try:
			BinarySearchTree()
		except NameError:
			self.fail("could not instantiate")

	def test_new_insert_method(self):
		insertee = 10
		bst = BinarySearchTree()
		bst.insert(insertee)
		self.assertEqual(insertee, bst.value)
			
	def test_instantiation_with_value(self):
		fake_vlue = "fake"
		bst = BinarySearchTree(fake_vlue)
		self.assertEqual(fake_vlue, bst.value)

	def test_insert_smaller(self):
		bst = BinarySearchTree()
		insertee = 10
		insertee2 = 1
		bst.insert(insertee)
		bst.insert(insertee2)
		self.assertEqual(insertee2, bst.left.value)

	def test_insert_larger(self):
		bst = BinarySearchTree()
		insertee = 10
		insertee2 = 20
		bst.insert(insertee)
		bst.insert(insertee2)
		self.assertEqual(insertee2,bst.right.value)


	def test_find(self):
		item = 5
		bst = BinarySearchTree(item)
		return_item = bst.find(item)
		self.assertEqual(item, return_item)

	def test_postorder(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.insert(2)
		bst.insert(3)
		test_list = [3,2,1]
		test = bst.post_order()
		self.assertEqual(test, test_list)

	def test_inorder(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.insert(2)
		bst.insert(3)
		test_list = [3,2,1]
		test = bst.in_order()
		self.assertEqual(test, test_list)
	
	def test_preorder(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.insert(2)
		bst.insert(3)
		test_list = [1, 2, 3]
		test = bst.pre_order()
		self.assertEqual(test_list, test)

if __name__=='__main__':
	unittest.main()