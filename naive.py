k=0
sum=0

for i in range(2,20000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            k=1
            #print(i)
    if k==1:
        sum+=i
    k=0
print(sum)

