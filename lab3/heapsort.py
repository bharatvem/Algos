'''
Created on Sep 22, 2016

@author: Bharat Vemulapalli
'''
from click._compat import raw_input
def left(x):
    return 2*x
def right(x):
    return (2*x)+1
def parent(x):
    return(int(x/2))
def swap(ar,x,y):
    t = ar[x]
    ar[x] = ar[y]
    ar[y] = t
    
def build_max_heap(ar):
    for i in range(int(len(ar)/2),0,-1):
        max_heapify(ar,i)

def max_heapify(arm,j):
    global heap_size
    l = left(j)
    r = right(j)
    largest = j
    if (l<= heap_size):
        if(arm[l-1] > arm[j-1]):
            largest = l
    else:
        largest = j
    if (r <= heap_size):
        if (arm[r-1] > arm[largest-1]):
            largest = r
    if (largest != j):
        swap(arm,j-1,largest-1)
        max_heapify(arm, largest)

def heapsort(armh):
    global heap_size
    build_max_heap(armh)
    for i in range(heap_size,1,-1):
        swap(armh,0,i-1)
        heap_size = heap_size - 1
        max_heapify(armh, 1)
    
if __name__ == '__main__':
#     a = [106,33,44,36,29,309,64]
    a=raw_input("Enter list: ")
    a=eval(a)
    heap_size = len(a)
    print(a)
#     print(parent(9))
#     build_max_heap(a)
    heapsort(a)
    print("sorted array:\n"+str(a))
    