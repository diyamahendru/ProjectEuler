i=0
for a in range(2,1000000000):
    for b in range(2,a):
        if b<a:
            if a%b == 0:
                break
    else:
            i+=1
            if i == 10001:
                print(a)
                break
          
