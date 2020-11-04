import os
def calculer(a,x,n):
	res = 0
	i = 0
	while(i<=n):
		res = res + (a*i*x*i)
		i +=1
	return res

b = calculer(2,3,5)
print(b)



