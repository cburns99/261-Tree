class BinarySearchTree:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, insertee):
   		if self is None: 
   			self = insertee 
   		else: 
   			if self.value < insertee.value: 
   				if self.right is None: 
   					self.right = insertee 
   				else: 
   					insert(self.right, insertee) 
   			else:
   				if self.left is None:
   					self.left = insertee
   				else: 
   					insert(self.left, insertee) 

