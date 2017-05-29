def get_fib(position):
    # Write your code here.
    if position==0:
        return 0
    elif position==1:
        return 1
    else:
        fib = [0 for i in range(position+1)]
        fib[0] = 0
        fib[1] = 1
        for j in range(2,position+1):
            fib[j] = fib[j-1]+fib[j-2] 
            
        return fib[position]
    
    
#n = int(raw_input())
print(get_fib(23))

