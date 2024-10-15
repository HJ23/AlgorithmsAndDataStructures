class Node:

	
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0
	def add(self,value):
		if(self.head is None):
			self.length += 1
			self.head = Node(value)
			return
		pointer = self.head
		while(pointer.next!=None):
			pointer = pointer.next
		pointer.next = Node(value)
		self.length += 1
	def delete(self,index):
		assert self.length>index, "Index is out of range!"
		if(index==0):
			self.length -= 1
			self.head = self.head.next
			return
		pre_pointer = None
		pointer = self.head
		for x in range(index):
			tmp = pointer
			pointer = pointer.next
			pre_pointer = tmp
		pre_pointer.next=pointer.next
		self.length -= 1
	def insert(self,index,value):
		assert self.length>index-1, "Index is out of range!"
		if(index==0):
			tmp = self.head
			self.head = Node(value)
			self.head.next = tmp
			self.length += 1 
			return 
		pre_pointer = None
		pointer = self.head
		for x in range(index):
			tmp = pointer
			pointer = pointer.next
			pre_pointer = tmp
		new_node = Node(value)
		new_node.next = pointer
		pre_pointer.next = new_node
		self.length += 1
	def __str__(self):
		ret = ""
		pointer = self.head
		while(pointer):
			ret+=str(pointer.value)
			pointer = pointer.next
			ret+="->" if(pointer) else ""
		return ret

	def reverse(self):
		pointer = self.head
		pre_pointer = None
		while(pointer):
			tmp = pointer.next
			pointer.next = pre_pointer
			pre_pointer = pointer
			pointer = tmp
		self.head = pre_pointer

if __name__ == "__main__":
	ll = LinkedList()
	ll.add(12)
	ll.add(13)
	ll.add(45)
	ll.add(567)
	ll.add(111)
	print(ll)
	ll.delete(4)
	print(ll)
	ll.insert(0,266)
	print(ll)
	ll.delete(0)
	ll.delete(0)
	ll.delete(0)
	ll.delete(1)
	ll.delete(0)
	print(ll)
	ll.add(1)
	ll.add(2)
	ll.add(3)
	print(ll)
	ll.reverse()
	print(ll)
