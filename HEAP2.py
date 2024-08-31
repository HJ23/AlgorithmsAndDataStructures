class MIN_HEAP:
	def __init__(self):
		self.heap = []
		self.size = 0
	def get_left(self,position):
		return position*2+1
	def get_parent(self,position):
		return (position-1)//2
	def get_right(self,position):
		return position*2+2
	def has_left(self,position):
		return self.get_left(position) < self.size
	def swap(self,pos1,pos2):
		self.heap[pos1],self.heap[pos2] = self.heap[pos2],self.heap[pos1]
	def heapify_up(self,position):
		if(self.get_parent(position)>=0):
			if(self.heap[self.get_parent(position)] > self.heap[position] ):
				self.swap(position,self.get_parent(position))
				self.heapify_up(self.get_parent(position))
	def heapify_down(self,position):
		if(self.has_left(position)):
			smallest = self.heap[self.get_left(position)]
			index = self.get_left(position)
			if(self.get_right(position)<self.size and smallest>self.heap[self.get_right(position)]):
				index = self.get_right(position)
				smallest= self.heap[self.get_right(position)]

			if(self.heap[position]<smallest):
				return
			self.swap(position,index)
			self.heapify_down(index)


	def add(self,element):
		self.heap.append(element)
		self.size += 1
		self.heapify_up(self.size-1)
	def pop(self):
		if(self.size==0):
			raise Exception("Heap size out of bound Exception !")
		output = self.heap[0]
		last_item = self.heap.pop()
		self.size -= 1
		if(len(self.heap)>0):
			self.heap[0] = last_item
			self.heapify_down(0)
		return output
	def __str__(self):
		ret = ""
		for i in range(0, (self.size//2)):
			ret += "\n PARENT : "+ str(self.heap[i])+"\n LEFT CHILD : "
			ret += str(self.heap[2 * i+1]) if(len(self.heap)>(2*i+1)) else "-"
			ret +="\n RIGHT CHILD : "+str(self.heap[2 * i + 2]) if(len(self.heap)>(2*i+2)) else " - " +  "\n"
		return ret

if __name__ == "__main__":
	obj = MIN_HEAP()
	obj.add(23)
	obj.add(45)
	obj.add(4345)
	obj.add(1123)
	obj.add(34)
	obj.add(4)
	obj.add(12)
	obj.add(-3)
	print(obj)
	print("**************************************")
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj.pop())
	print(obj)
