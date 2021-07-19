def collatz_repeat(n):
    odd = (3*n)+1
    even = n/2
    one = 0
    count = 0
    
    if n%2==0:
        even_num = even
        one = even_num
        count+=1
    elif (n/2)!=0:
        odd_num = odd
        one = odd_num
        count+=1
            
    while one!=1:
         if one!=1:
             if one%2==0:
                 even_num = one/2
                 one = even_num
                 count+=1
             elif one%2!=0:
                 odd_num = (3*one)+1
                 one = odd_num
                 count+=1
        
    return count
