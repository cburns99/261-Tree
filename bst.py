#Cameron Burns
#Trees 
#11/5
class BinarySearchTree:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, insertee):
   		if self.value is None: 
   			self.value = insertee 
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

	def pre_order(self):
		pre_order_list = [self.value]
		if self.left:
			pre_order_list.extend(self.left.pre_order())
		if self.right:
			pre_order_list.extend(self.right.pre_order())
		return pre_order_list

	
