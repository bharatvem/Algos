'''
Created on Sep 26, 2016

@author: Bharat Vemulapalli
'''

def swap(ay,x,y):
    t = ay[x]
    ay[x] = ay[y]
    ay[y] = t
    
def partition(A,p,r):
    x = A[r]
    i = p-1
    for yy in range(p,r):
        if A[yy] <= x :
            i = i+1
            swap(A,i,yy)
    swap(A,i+1,r)
    return i+1
        
def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

if __name__ == '__main__':
    ar = [22,84,10,37,9,40,34]
    print("before sorting")
    print(ar)
    
    quicksort(ar, 0, (len(ar)-1))
    print("after sorting")
    print(ar)