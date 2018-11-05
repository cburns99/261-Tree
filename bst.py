class BinarySearchTree:
	def __init__(self, value = None):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None

	def get_left(self):
		return self.right

	def get_right(self):
		return self.left

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
   	
	def find(self, item):  
		if self.value is None:
			return None
		elif self.value is item: 
			return self.value
		elif self.value > item: 
			return self.right.find(item)
		elif self.value < value:
			return self.left.find(item)

	def post_order(self,):
   		if self:
   			post_order(self.left)
   			post_order(self.right)
   			print(self.value)

	def pre_order(self):
		if self:
			pre_order(self)

