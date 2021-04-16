n=int(input())
seive=[1]*(n+1)
seive[0]=0
seive[1]=0
for i in range(2,int(n**0.5+1)):
    if seive[i]==1:
        for j in range(i*i,n+1,i):
            seive[j]=0
prime=[]
sum_prime=0
for i in range(1,n+1):
    if seive[i]==1:
        sum_prime+=i
        prime.append(i)
print(sum_prime)#for sum of primes
print(prime)#to list all primes
