#The function below will determine if an 'n' is present in the 'list' that we enter with it.
#We assume that the list is very large and hence we do not know if it contains 'n'.
#We assume the list to be sorted and hence we use the Binary Search Algorithm or approach to make the search faster.

def BinarySearch(list, n):
    low = 0                                         #The low is indexed to the first index of the entered list.
    high = len(list)-1                              #The high is indexed to the last element of the entered list.
    mid = 0
                           
    while low <= high and list[mid]!=n:  
                    
        #The mid is indexed as the floor value of average of low & high.
        mid = (low+high)//2
           
        #This means that the element if present, is not in the left part of the list.
        if list[mid] < n:
            low = mid + 1
        
        #This means that the element if present, is not in the right part of the list.
        elif list[mid] > n:
            high = mid - 1
        
        #This is the return value when the element is found. 
        else:
            return mid
    
    #This is when element is not present in the list.
    return -1
    


#"The Time Complexity of this code is O(log(len(list))) which is logarithmic."