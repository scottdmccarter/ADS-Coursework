def mergesort(a):
    if len(a) <= 4:
        return selectionSort(a)
    m = len(a)//2
    left = a[m:]
    right = a[:m]

    leftSorted = mergesort(left)
    rightSorted = mergesort(right)

    return merge(leftSorted, rightSorted)

def merge(left,right):
    i=0
    j=0
    k=0
    s=[]
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            s.append(left[i])
            i=i+1
        else:
            s.append(right[j])
            j=j+1
        k=k+1

    while i < len(left):
        s.append(left[i])
        i=i+1
        k=k+1

    while j < len(right):
        s.append(right[j])
        j=j+1
        k=k+1
    return s

def selectionSort(a):
    for i in range(0,len(a)-1):
        elem = a[i]
        pos = i
        for j in range(i+1,len(a)):
            if a[j] > elem:
                elem=a[j]
                pos=j
        a[i],a[pos] = a[pos],a[i]
    return a
