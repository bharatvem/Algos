'''
Created on Aug 26, 2016

@author: Beast
'''
def merge(x,begin,mid,end):
    s,b1,e1,b2,e2 = 0,begin,mid,mid+1,end
    t1,t2 = [],[]
    n1,n2 = mid-begin+1,end-mid
    for i in range(0,n1) :
#         print('move' + str(x[i])+ 'to' +str(t1[i]) )
        t1.append(x[begin+i])
    for i in range(0,n2) :
        t2.append(x[mid+1+i])

    p,q,r = 0,0,begin
    
    while(p<n1 and q<n2):
        if(t1[p]<t2[q]):
            x[r] = t1[p]
            p=p+1
        else:
            x[r] = t2[q]
            q=q+1
        r = r+1
        
    while(p<n1):
        x[r] = t1[p]
        p=p+1 
        r=r+1
    while(q<n2):
        x[r] = t2[q]
        q=q+1
        
        
        r=r+1
    
    
def mergesort(x,begin,end):
    mid = 0
    if(begin < end) :
        mid = int((begin+end)/2)
        mergesort(x, begin, mid)
        mergesort(x, mid+1, end)
        merge(x,begin,mid,end)

def main():
    print("you are in main")
    arr = [5,40,3,26,1]
    n = len(arr)
    print(arr)
    mergesort(arr,0,n-1)
    print(arr)


    
if __name__ == '__main__':
    #print("You are in text.py")
    main()