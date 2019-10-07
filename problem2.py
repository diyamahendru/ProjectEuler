sum_= 0.0
curr_= 0.0
iter_val= 0
def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+ fibo(n-2)

while(curr_<= 4000000):
    curr_= fibo(iter_val)
    iter_val+= 1
    if(curr_%2== 0):
        sum_+=curr_
    else:
        pass
print(sum_)

