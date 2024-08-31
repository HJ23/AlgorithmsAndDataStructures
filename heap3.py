

class Heap:
    def __init__(self):
        self.heap = [0,]

    def __swap(self,a,b) -> None:
        tmp = self.heap[a] 
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
    
    def push(self,num: int) -> None:
        self.heap.append(num)
        self.heapify()

    def heapify(self) -> None:
        element_index = len(self.heap)-1
        root = element_index//2
        while(root!=0 and self.heap[root]>self.heap[element_index]):
            self.__swap(root,element_index)
            element_index = root
            root = element_index//2

    def pop(self) -> object:
        main_item = self.heap[1] if(self.heap.__len__()>1) else None
        if(self.heap.__len__()<=2):
            if(self.heap.__len__()==2):
                del self.heap[1]
            return main_item
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        root = self.heap[1]
        index = 1
        while(1):
            mini = root
            tmp_index = index

            if( 2*index<self.heap.__len__() and mini>self.heap[2*index] ):
                mini = self.heap[2*index]
                tmp_index = 2*index
            if( 2*index+1<self.heap.__len__() and mini>self.heap[2*index+1] ):
                mini = self.heap[2*index+1]
                tmp_index = 2*index+1
            if(tmp_index == index):
                break
            
            self.__swap(index,tmp_index)
            index = tmp_index
            root = self.heap[index]
        return main_item
    
def mini(arr=[4,1,3,8,4,9,0,5,6,7]):
    obj = Heap()
    for x in arr:
        obj.push(x)
    print(obj.heap)
    ret = []
    while(1):
        a = obj.pop()
        if(a is None):
            break
        print(obj.heap)
        ret.append(a)
    return ret


print(mini())


