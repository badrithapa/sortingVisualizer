from tkinter import *
from tkinter.font import *
import random

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

    
def heapify(lengthlist, n, i):
    global barlist
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and lengthlist[largest] < lengthlist[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and lengthlist[largest] < lengthlist[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        lengthlist[i], lengthlist[largest] = lengthlist[largest], lengthlist[i]  # swap
        barlist[i], barlist[largest] = barlist[largest], barlist[i]
        swap(barlist[largest],barlist[i])
        heapify(lengthlist, n, largest)
##        heapify(barlist, n, largest) #big mistake why tf would i heapify a bloody canvas object

def heap_sort(lengthlist):
    global barlist
    n = len(lengthlist)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(lengthlist, n, i)
##        heapify(barlist, n, i) #im leaving here to remind myself how stupid i was..
    # One by one extract elements
    for i in range(n-1, 0, -1):
        lengthlist[i], lengthlist[0] = lengthlist[0], lengthlist[i]
        barlist[i], barlist[0] = barlist[0], barlist[i]
        swap(barlist[i],barlist[0])
        heapify(lengthlist, i, 0)
##        heapify(barlist, n, 0) # and how obvious it was.......
        yield
        

def bubble_sort():
    global lengthlist
    global barlist
    for i in range(len(lengthlist)-1):
        for j in range(len(lengthlist)-i-1):
            if lengthlist[j]>lengthlist[j+1]:
                lengthlist[j],lengthlist[j+1] = lengthlist[j+1],lengthlist[j]
                barlist[j],barlist[j+1]=barlist[j+1],barlist[j]
                mycanvas.itemconfig(barlist[j-1],fill="yellow")
                mycanvas.itemconfig(barlist[i],fill="black")
                mycanvas.itemconfig(barlist[j+1],fill="yellow")
                swap(barlist[j],barlist[j+1])
                yield
def selection_sort():
    global lengthlist
    global barlist
    for i in range(len(lengthlist)):
        min=i
        for j in range(i+1,len(lengthlist)):
            if lengthlist[j]<lengthlist[min]:
                min=j
        lengthlist[min],lengthlist[i]=lengthlist[i],lengthlist[min]
        barlist[min],barlist[i]=barlist[i],barlist[min]
        swap(barlist[min],barlist[i])
        yield

    
worker = None 
def swap(bar1,bar2):
    x11,_,y12,_=mycanvas.coords(bar1)
    x21,_,y22,_=mycanvas.coords(bar2)
    mycanvas.move(bar1,x21-x11,0)
    mycanvas.move(bar2,y12-y22,0)

def shuffle():
    global lengthlist
    global barlist
    mycanvas.delete('all')
    barstart=5
    barend=15
    barlist=[]
    lengthlist=[]
    for bar in range(1,79):
        randomY=random.randint(1,530)
        bar=mycanvas.create_rectangle(barstart,randomY,barend,540,outline="black", fill="yellow")
        barlist.append(bar)
        barstart+=10
        barend+=10

    for bar in barlist:
        y=mycanvas.coords(bar)
        length = y[3]-y[1]
        lengthlist.append(length)

    for i in range(len(lengthlist)):
        if lengthlist[i]== min(lengthlist):
            mycanvas.itemconfig(barlist[i],fill="red")
        if lengthlist[i]== max(lengthlist):
            mycanvas.itemconfig(barlist[i],fil="blue")
def color():
    global lengthlist
    global barlist
    for i in range(len(lengthlist)):
        mycanvas.itemconfig(barlist[i],fill="green")
        if lengthlist[i]== min(lengthlist):
            mycanvas.itemconfig(barlist[i],fill="red")
        if lengthlist[i]== max(lengthlist):
            mycanvas.itemconfig(barlist[i],fil="blue")
        
            
    
def animate():
    global worker
    if worker is not None:
       try:
           next(worker)
           win.after(10,animate)
       except StopIteration:
           worker=None
           color()
       finally:
           win.after_cancel(animate)
           
def mergesort():
    global worker
    global lengthlist
    worker=merge_sort(lengthlist)
    animate()
                
def bubblesort():
    global worker
    worker=bubble_sort()
    animate()
    
def selectionsort():
    global worker
    worker=selection_sort()
    animate()
def heapsort():
    global worker
    worker=heap_sort(lengthlist)
    animate()

win=Tk()
win.title('Sorting algorithms')
win.geometry("800x600")
myfont=Font(weight="bold")
mycanvas=Canvas(win, width="800", height="550")
mycanvas.grid(row=0,column=0,columnspan=70)

shuffle =  Button(win, text="Shuffle", bg="blue",fg="white", command=shuffle)

bubble=Button(win, text="Bubble Sort", command=bubblesort)

selection=Button(win, text="Selection Sort", command=selectionsort)

heap=Button(win, text="Heap Sort", command=heapsort)

merge=Button(win, text="Merge Sort", command=mergesort)

merge['font']=myfont
shuffle['font']=myfont
bubble['font']=myfont
selection['font']=myfont
heap['font']=myfont
selection.grid(row=1, column=2)
bubble.grid(row=1, column=1)
shuffle.grid(row=1,column=0)
heap.grid(row=1, column=3)
merge.grid(row=1, column=4)

win.mainloop()

##def merge_sort(lengthlist):
##    global barlist
##    a=lengthlist
##    if len(lengthlist)>2:
##        mid=len(lengthlist)//2
##        l=lengthlist[:mid]
##        r=lengthlist[mid:]
##        
##        #recursion within left and right art of the array
##        merge_sort(l)
##        merge_sort(r)
##        
##        i=j=k=0
##        while i<len(l) and j<len(r):
##            if l[i]<r[j]:
##                lengthlist[k]=l[i]
##                i+=1
##            else:
##                lengthlist[k] = r[j]
##                swap(barlist[k],barlist[j])
##                j += 1
##            k += 1
##            yield
##        while i < len(l):
##            lengthlist[k] = l[i]
##            i += 1
##            k += 1
##            yield
##        while j < len(r):
##            lengthlist[k] = r[j]
##            j += 1
##            k += 1
##            yield

