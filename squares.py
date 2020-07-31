import numpy as np
l=int(input('enter the range of the numbers:'))
sum_of_squares=range(1,l+1)
n1=np.power(sum_of_squares,2)
squares_of_sum=range(1,l+1)
n2=sum(squares_of_sum)**2
print(n2-(sum(n1)))
