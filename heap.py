class Node:
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None

class Heap:
	def __init__(self):
		self.root = None
		self.count = 0
	def add(self,val):
		if(self.root is None):
			self.root = Node(val)
			return
		queue = [self.root]
		while(queue.__len__()):
			current = queue.pop(0)
			if(current.left is None):
				current.left = Node(val)
				break
			if(current.right is None):
				current.right = Node(val)
				break
			if(not current.left is None ):
				queue.append(current.left)
			if(not current.right is None):
				queue.append(current.right)
		self.count+=1
		self.adjust()
	def adjust(self):
		for _ in range(self.count):
			queue = [self.root]
			while(queue.__len__()):
				current = queue.pop(0)
				if(not current.left is None):
					if(current.val < current.left.val):
						tmp = current.val
						current.val = current.left.val
						current.left.val = tmp
						break
					queue.append(current.left)
				if(not current.right is None):
					if( current.val < current.right.val):
						tmp= current.val
						current.val = current.right.val
						current.right.val = tmp
						break
					queue.append(current.right)

	def __str__(self):
		ret = ""
		queue = [self.root]
		while(queue.__len__()):
			tmp = queue.pop(0)
			if(tmp is None):
				continue
			ret = ret + "->" + str(tmp.val)
			if(not tmp.left is None):
				queue.append(tmp.left)
			if(not tmp.right is None):
				queue.append(tmp.right)
		return ret


obj = Heap()
obj.add(12)
obj.add(32)
obj.add(1)
obj.add(45)
print(obj)
