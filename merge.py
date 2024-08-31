arr = [45,23,11,23,64,4,2,5,6,3,1,2]

def merge(l, mid, h):
    i = l
    j = mid + 1
    tmp = []

    while i <= mid and j <= h:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= h:
        tmp.append(arr[j])
        j += 1

    for k in range(len(tmp)):
        arr[l + k] = tmp[k]

def mergesort(l,h):
	if(l<h):
		mid = (l+h)//2
		mergesort(l,mid)
		mergesort(mid+1,h)
		merge(l,mid,h)


mergesort(0,len(arr)-1)
print(arr)






