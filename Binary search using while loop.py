def binary_search(listofnumbers, numbertosearch):
    begin_index = 0
    end_index = len(listofnumbers)-1
    '''binary search does the haleving of a list and shortens it down to 1.
    Hence the while loop entails that until the difference between the number at the end of the list 
    and number at the beginning of the list is 1 dont stop the loop and keep halvening it'''
    while((end_index-begin_index)>1):
        #keep finding the middle point
        mid = (begin_index+end_index)//2
        if (listofnumbers[mid]==numbertosearch):
            return 1
        if (listofnumbers[mid]>numbertosearch):
            #change the ending index 
            end_index = mid-1
        if (listofnumbers[mid]<numbertosearch):
            begin_index = mid+1
            
    if listofnumbers[begin_index] == numbertosearch or listofnumbers[end_index] == numbertosearch:
        return 1
    else:
        return 0

